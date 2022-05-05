from pathlib import Path

from ..paths import PG_RESTORE_PATH
from ..streamrun import subprocess_stream


def restore(config, file: Path):
    return subprocess_stream(
        [PG_RESTORE_PATH, f"--dbname={config['database']}", str(file.absolute())],
        env={
            "PGPASSWORD": config["password"],
            "PGHOST": config["host"],
            "PGUSER": config["username"],
            "PGPORT": config["port"],
        },
    )
