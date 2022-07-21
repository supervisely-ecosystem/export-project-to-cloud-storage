import os

import supervisely as sly

import functions as f
import globals as g


@sly.timeit
def export_project_to_cloud_storage(api: sly.Api, task_id):
    local_project_dir = os.path.join(g.STORAGE_DIR, g.PROJECT_NAME)
    g.PROJECT_NAME = f.validate_remote_storage_path(
        api=api, project_name=g.PROJECT_NAME
    )
    f.upload_project_meta_to_remote_bucket(
        api, local_project_dir, g.PROJECT_NAME, g.PROJECT_META_JSON
    )

    datasets = list(api.dataset.get_list(g.PROJECT_ID))
    for dataset in datasets:
        images_infos = api.image.get_list(dataset.id)
        images_ids = [image_info.id for image_info in images_infos]
        images_names = [image_info.name for image_info in images_infos]

        anns_infos = api.annotation.download_batch(dataset.id, images_ids)
        ann_jsons = [ann_info.annotation for ann_info in anns_infos]

        progress = sly.Progress(
            message=f"Uploading images from {dataset.name}", total_cnt=len(images_ids)
        )
        for image_id, image_name, ann_json in zip(images_ids, images_names, ann_jsons):
            f.upload_image_to_remote_bucket(
                api=api,
                local_project_dir=local_project_dir,
                project_name=g.PROJECT_NAME,
                dataset_name=dataset.name,
                image_id=image_id,
                image_name=image_name,
            )
            f.upload_ann_to_remote_bucket(
                api=api,
                local_project_dir=local_project_dir,
                project_name=g.PROJECT_NAME,
                dataset_name=dataset.name,
                ann_json=ann_json,
                image_name=image_name,
            )
            progress.iter_done_report()

    remote_project_dir = os.path.join(g.PROVIDER, g.BUCKET_NAME, g.PROJECT_NAME)
    sly.logger.info(f"Project has been successfully exported to {remote_project_dir} ✅")


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

    export_project_to_cloud_storage(g.api, g.TASK_ID)
    sly.app.fastapi.shutdown()
