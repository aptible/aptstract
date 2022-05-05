import subprocess
from collections.abc import Callable

from ..paths import HEROKU_CLI_PATH
from ..streamrun import subprocess_stream


def get_backup(application: str, database: str = None):
    backup_command = [HEROKU_CLI_PATH, "pg:backups:capture", "--app", application]
    if database:
        backup_command.append(database)
    backup_results = subprocess_stream(backup_command, stdout=subprocess.PIPE)

    if backup_results["returncode"] != 0:
        raise Exception("Unable to run backup.")

    if database:
        save_path = f"backups/{application}.{database}.dump"
    else:
        save_path = f"backups/{application}.dump"

    download_command = [HEROKU_CLI_PATH, "pg:backups:download", "--app", application, "--output", save_path]
    download_results = subprocess_stream(download_command, stdout=subprocess.PIPE)
    if download_results["returncode"] != 0:
        raise Exception("Unable to download backup.")
