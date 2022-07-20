import os

import supervisely as sly
from supervisely.io.fs import mkdir
from supervisely.io.json import dump_json_file

import globals as g


def upload_image_to_remote_bucket(
    api: sly.Api,
    local_project_dir: str,
    project_name: str,
    dataset_name: str,
    image_id: int,
    image_name: str,
):
    local_img_dir = os.path.join(local_project_dir, dataset_name, "img")
    if not os.path.exists(local_img_dir):
        mkdir(local_img_dir)
    local_image_path = os.path.join(local_img_dir, image_name)
    remote_image_path = os.path.join(project_name, dataset_name, "img", image_name)
    remote_image_path = api.remote_storage.get_remote_path(
        provider=g.PROVIDER, bucket=g.BUCKET_NAME, path_in_bucket=remote_image_path
    )
    api.image.download_path(id=image_id, path=local_image_path)
    api.remote_storage.upload_path(
        local_path=local_image_path, remote_path=remote_image_path
    )


def upload_ann_to_remote_bucket(
    api: sly.Api,
    local_project_dir: str,
    project_name: str,
    dataset_name: str,
    ann_json: dict,
    image_name: str,
):
    local_ann_dir = os.path.join(local_project_dir, dataset_name, "ann")
    if not os.path.exists(local_ann_dir):
        mkdir(local_ann_dir)
    local_ann_path = os.path.join(local_ann_dir, f"{image_name}.json")
    remote_ann_path = os.path.join(
        project_name, dataset_name, "ann", f"{image_name}.json"
    )
    remote_ann_path = api.remote_storage.get_remote_path(
        provider=g.PROVIDER, bucket=g.BUCKET_NAME, path_in_bucket=remote_ann_path
    )
    dump_json_file(ann_json, local_ann_path)
    api.remote_storage.upload_path(
        local_path=local_ann_path, remote_path=remote_ann_path
    )


def upload_project_meta_to_remote_bucket(
    api: sly.Api, local_project_dir: str, project_name: str, project_meta_json: dict
):
    if not os.path.exists(local_project_dir):
        mkdir(local_project_dir)
    local_project_meta_json_path = os.path.join(local_project_dir, "meta.json")
    remote_project_meta_json_path = os.path.join(project_name, "meta.json")
    remote_project_meta_json_path = api.remote_storage.get_remote_path(
        provider=g.PROVIDER,
        bucket=g.BUCKET_NAME,
        path_in_bucket=remote_project_meta_json_path,
    )
    dump_json_file(project_meta_json, local_project_meta_json_path)
    api.remote_storage.upload_path(
        local_path=local_project_meta_json_path,
        remote_path=remote_project_meta_json_path,
    )


def shutdown_app():
    try:
        sly.app.fastapi.shutdown()
    except KeyboardInterrupt:
        sly.logger.info("Application shutdown successfully")
