import contextlib
import signal
import subprocess
import sys
import time

import typer

from ..paths import APTIBLE_CLI_PATH
from ..streamrun import subprocess_stream

# These are the keys we need to extract from the
db_config = ["host", "port", "username", "password", "database"]


@contextlib.contextmanager
def database_tunnel(database: str):
    results = subprocess_stream(
        [APTIBLE_CLI_PATH, "db:tunnel", database],
        "Connected. Ctrl-C to close connection.",
        stderr=subprocess.PIPE,
        quiet=True,
    )

    if "returncode" in results:
        typer.echo("Unable to establish tunnel.")
        sys.exit(1)

    typer.echo("Tunnel Established.")

    config = {}
    for line in results["stderr"].splitlines():
        line_tuples = line.strip(" *").split(":", maxsplit=1)
        if line_tuples[0].lower() in db_config:
            config[line_tuples[0].lower()] = line_tuples[1].strip()

    yield config

    typer.echo("Closing Tunnel.")
    results["process"].send_signal(signal.SIGINT)
    time.sleep(5)
    results["process"].kill()
