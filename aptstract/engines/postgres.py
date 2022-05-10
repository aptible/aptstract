from pathlib import Path

from ..paths import get_utility_path
from ..streamrun import subprocess_stream


def restore(config, file: Path):
    PG_RESTORE_PATH = get_utility_path("pg_restore")
    return subprocess_stream(
        [PG_RESTORE_PATH, f"--dbname={config['database']}", str(file.absolute())],
        env={
            "PGPASSWORD": config["password"],
            "PGHOST": config["host"],
            "PGUSER": config["username"],
            "PGPORT": config["port"],
        },
    )
