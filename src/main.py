from pathlib import Path

import functions as f
import sly_globals as g
import supervisely as sly


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
            sly.download_fast(
                api=api, 
                project_id=g.PROJECT_ID, 
                dest_dir=local_dir, 
                progress_cb=p.update, 
                save_images=False, 
                project_info=project_info,
                save_images=g.DOWNLOAD_IMAGES,
                save_image_info=g.INCLUDE_INFO,
                skip_create_readme=g.EXCLUDE_README,
            )
    dir_size = sly.fs.get_directory_size(local_dir)
    project_name = f.validate_remote_storage_path(api=api, project_name=project_info.name)
    remote_path: str = api.remote_storage.get_remote_path(g.PROVIDER, g.BUCKET, project_name)
    with sly.tqdm_sly(total=dir_size, desc="Uploading project", unit="B", unit_scale=True) as pbar:
        local_files = sly.fs.list_files_recursively(local_dir)
        rel_paths = [str(Path(f).relative_to(local_dir)) for f in local_files]
        remote_files = [f"{remote_path}/{f.clean_remote_path(rel_path)}" for rel_path in rel_paths]

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
            "project_id": g.PROJECT_ID,
            "provider": g.PROVIDER,
            "bucket_name": g.BUCKET,
            "annotations_only": g.ONLY_ANNOTATIONS,
            "include_info": g.INCLUDE_INFO,
            "exclude_readme": g.EXCLUDE_README,
        },
    )

    sly.main_wrapper("main", export_project_to_cloud_storage, api=g.api)
