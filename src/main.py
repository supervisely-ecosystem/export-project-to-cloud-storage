import os
import globals as g
import supervisely as sly


@g.app.callback("export-project-to-cloud-storage")
@sly.timeit
def export_project_to_cloud_storage(api: sly.Api, task_id, context, state, app_logger):
    project_dir = os.path.join(g.STORAGE_DIR, g.PROJECT_NAME)
    sly.download_project(api=api, project_id=g.PROJECT_ID, dest_dir=project_dir, dataset_ids=None, log_progress=True)

    # api.remote_storage.download_path()

    g.app.stop()


def main():
    sly.logger.info("Script arguments", extra={
        "task_id": g.TASK_ID,
        "team_id": g.TEAM_ID,
        "workspace_id": g.WORKSPACE_ID,
        "modal.state.slyProjectId": g.PROJECT_ID
    })
    g.app.run(initial_events=[{"command": "export-project-to-cloud-storage"}])


if __name__ == '__main__':
    sly.main_wrapper("main", main)
