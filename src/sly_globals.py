import os

import supervisely as sly
from dotenv import load_dotenv
from functions import validate_bucket_name

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()

TASK_ID = sly.env.task_id()
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()
PROJECT_ID = sly.env.project_id()

PROVIDER = os.environ.get("modal.state.provider")
BUCKET = validate_bucket_name(os.environ.get("modal.state.bucketName"))


STORAGE_DIR = sly.app.get_data_dir()
STORAGE_DIR = sly.app.get_data_dir()