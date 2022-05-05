# Aptstract

Aptstract is a CLI used to migrate databases from Heroku to Aptible.

## Prerequisites

The Aptible and Heroku CLIs need to be installed, and both should be logged in.

```bash
brew install libpq
echo 'export PATH="/opt/homebrew/opt/libpq/bin:$PATH"' >> ~/.zshrc
```

## Install

Run `make install` and then activate the virtual environment source.

```
make install
source ./venv/bin/activate
```

Now the `aptstract` cli will be available in your shell.

## Usage

### Get your Data

First fetch your backup.

If your application only has a single database it will be selected by default.

```bash
aptstract fetch-database rph-test-app
```

Otherwise you can specify the database directly.

```bash
aptstract fetch-database rph-test-app customer-database
```

### Restore your Data

Now you can restore the data from the previous command to restore the data to Aptible.

```bash
aptstract restore-data my-aptible-database ./backups/rph-test-app.dump
```

### Interactive Mode

This can also be done with a single interactive command.

```text
$ aptstract migrate
What is the name of the Heroku application?: rph-test-app
Is there more than one database in the application? [y/N]:
What is the name of the Aptible database to restore to?: restore-sandbox

Backing up DATABASE to b013... done
Getting backup from rph-test-app... done, #13
Downloading backups/rph-test-app.dump... ████████████████████████▏  100% 00:00 868.00B
Opening secure tunnel to Aptible Database.
Aptible Database Tunnel Established.
Restoring backup.
Backup successfully migrated to restore-sandbox.
Closing Database Tunnel.
```
