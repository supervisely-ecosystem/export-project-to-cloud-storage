import asyncio
from pathlib import Path

import supervisely as sly

import functions as f
import sly_globals as g


@sly.timeit
def export_project_to_cloud_storage(api: sly.Api):
    project_info = api.project.get_info_by_id(g.PROJECT_ID)
    batch_size = 50 if project_info.type == sly.ProjectType.IMAGES.value else 10
    if project_info is None:
        raise ValueError(f"Project with ID={g.PROJECT_ID} not found")

    local_dir = str(Path(sly.app.get_data_dir()) / project_info.name)

    project_type_to_cls = {
        sly.ProjectType.IMAGES.value: sly.Project,
        sly.ProjectType.VIDEOS.value: sly.VideoProject,
    }
    project_type_cls = project_type_to_cls.get(project_info.type)
    if project_type_cls is None:
        raise ValueError(f"Exporting project type {project_info.type} is not supported yet")

    if not sly.fs.dir_exists(local_dir):
        with sly.tqdm_sly(total=project_info.items_count, desc="Downloading project") as p:
            loop = sly.utils.get_or_create_event_loop()
            coroutine = project_type_cls.download_async(
                api, g.PROJECT_ID, local_dir, progress_cb=p.update
            )
            if loop.is_running():
                future = asyncio.run_coroutine_threadsafe(coroutine, loop)
                future.result()
            else:
                loop.run_until_complete(coroutine)

    dir_size = sly.fs.get_directory_size(local_dir)
    project_name = f.validate_remote_storage_path(api=api, project_name=project_info.name)
    remote_path: str = api.remote_storage.get_remote_path(g.PROVIDER, g.BUCKET, project_name)
    with sly.tqdm_sly(total=dir_size, desc="Uploading project", unit="B", unit_scale=True) as pbar:
        local_files = sly.fs.list_files_recursively(local_dir)
        remote_files = [f"{remote_path}/{str(Path(f).relative_to(local_dir))}" for f in local_files]

        for local, remote in zip(
            sly.batched(local_files, batch_size=batch_size),
            sly.batched(remote_files, batch_size=batch_size),
        ):
            api.storage.upload_bulk(g.TEAM_ID, local, remote, pbar)

    sly.logger.info(f"✅ Project has been successfully exported to {remote_path}")


if __name__ == "__main__":
    sly.logger.info(
        "Script arguments",
        extra={
            "task_id": g.TASK_ID,
            "team_id": g.TEAM_ID,
            "workspace_id": g.WORKSPACE_ID,
            "modal.state.slyProjectId": g.PROJECT_ID,
        },
    )

    sly.main_wrapper("main", export_project_to_cloud_storage, api=g.api)
