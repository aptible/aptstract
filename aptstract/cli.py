from pathlib import Path

import typer

from .engines import postgres
from .services import aptible, heroku

app = typer.Typer()


@app.command()
def fetch_database(application: str, database: str = None):
    heroku.get_backup(application, database)


@app.command()
def restore_file(database: str, backup: Path):
    with aptible.database_tunnel(database) as config:
        typer.echo("Restoring backup.")
        postgres.restore(config, backup)
    typer.echo("Backup restored.")


@app.command()
def test_tunnel(database: str):
    with aptible.database_tunnel(database) as config:
        for k, v in config.items():
            typer.echo(f"{k}: {v}")
        typer.echo()
        input("Press enter to close tunnel. ")


if __name__ == "__main__":
    app()
