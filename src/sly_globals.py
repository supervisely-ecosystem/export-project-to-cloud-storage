import os

import supervisely as sly
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))


def validate_bucket_name(bucket_name):
    import re

    if bucket_name == "" or bucket_name is None:
        raise ValueError("Bucket name is undefined")

    # Regex: one or more non-slash, then (slash and one or more non-slash) repeated, no leading/trailing/consecutive slashes
    pattern = r'^[^/]+(?:/[^/]+)+$'
    if not re.match(pattern, bucket_name):
        raise ValueError(
            "Bucket name must be in the format 'bucket/folder' or 'bucket/folder/subfolder', with no leading, trailing, or consecutive slashes"
        )
    return bucket_name

api = sly.Api.from_env()

TASK_ID = sly.env.task_id()
TEAM_ID = sly.env.team_id()
WORKSPACE_ID = sly.env.workspace_id()
PROJECT_ID = sly.env.project_id()

PROVIDER = os.environ.get("modal.state.provider")
BUCKET = validate_bucket_name(os.environ.get("modal.state.bucketName"))


STORAGE_DIR = sly.app.get_data_dir()
STORAGE_DIR = sly.app.get_data_dir()