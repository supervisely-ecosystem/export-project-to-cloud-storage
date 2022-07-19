import os
import sys
from pathlib import Path

import supervisely as sly
from supervisely.app.v1.app_service import AppService
from supervisely.sly_logger import logger

app_root_directory = str(Path(__file__).parent.absolute().parents[0])
logger.info(f"App root directory: {app_root_directory}")
sys.path.append(app_root_directory)
sys.path.append(os.path.join(app_root_directory, "src"))
logger.info(f'PYTHONPATH={os.environ.get("PYTHONPATH", "")}')

# order matters
from dotenv import load_dotenv
load_dotenv(os.path.join(app_root_directory, "secret_debug.env"))
load_dotenv(os.path.join(app_root_directory, "debug.env"))

app = AppService()
api = sly.Api.from_env()

TASK_ID = int(os.environ.get("TASK_ID"))
TEAM_ID = int(os.environ.get("context.teamId"))
WORKSPACE_ID = int(os.environ.get("context.workspaceId"))
PROJECT_ID = int(os.environ.get("modal.state.slyProjectId"))

PROVIDER = os.environ.get("modal.state.provider")
BUCKET_NAME = os.environ.get("modal.state.bucketName")

STORAGE_DIR = app.data_dir
