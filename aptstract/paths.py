import shutil
import sys

import typer


def get_utility_path(utility):
    path = shutil.which(utility)
    if not path:
        typer.echo(f"The {utility} binary must be installed before this utility can work.")
        sys.exit(1)
    return path
