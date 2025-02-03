from pathlib import Path

import supervisely as sly

import sly_globals as g


def validate_remote_storage_path(api: sly.Api, project_name):
    remote_path = api.remote_storage.get_remote_path(
        provider=g.PROVIDER, bucket=g.BUCKET, path_in_bucket="", team_id=g.TEAM_ID
    )
    remote_paths = api.storage.list(
        g.TEAM_ID,
        remote_path,
        include_files=False,
        recursive=False,
        with_metadata=False,
    )
    remote_folders = [item.name for item in remote_paths]
    res_project_name = sly.generate_free_name(used_names=remote_folders, possible_name=project_name)

    if res_project_name != project_name:
        sly.logger.warning(
            f"Project with name: {project_name} already exists in bucket, "
            f"project has been renamed to {res_project_name}"
        )
    return res_project_name
