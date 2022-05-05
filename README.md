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
