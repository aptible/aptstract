from pathlib import Path

import typer

from .engines import postgres
from .services import aptible, heroku

app = typer.Typer()


@app.command()
def migrate():

    heroku_application = typer.prompt("What is the name of the Heroku application?")
    heroku_database = None
    if typer.confirm("Is there more than one database in the application?"):
        heroku_database = typer.prompt("Which database should be moved?")
    aptible_database = typer.prompt("What is the name of the Aptible database to restore to?")

    backup_path = heroku.get_backup(heroku_application, heroku_database)
    with aptible.database_tunnel(aptible_database) as config:
        typer.echo("Restoring backup.")
        postgres.restore(config, Path(backup_path))
        typer.echo(f"Backup successfully migrated to {aptible_database}.")


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
