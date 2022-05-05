import subprocess

import typer


def subprocess_stream(command, return_on_string: str = False, quiet=False, **kwargs):
    process = subprocess.Popen(
        command,
        universal_newlines=True,
        encoding="utf-8",
        bufsize=1,
        **kwargs,
    )
    stdout = ""
    stderr = ""
    while True:
        had_output = False

        # Check for stdout changes.
        if process.stdout != None:
            for output in process.stdout:
                stdout += output
                if not quiet:
                    typer.echo(output)
                if output == return_on_string:
                    return dict(stdout=stdout, stderr=stderr, process=process)

        # Check for stderr changes.
        if process.stderr != None:
            for output in process.stderr:
                had_output = True
                stderr += output
                if not quiet:
                    typer.echo(output)
                if output.strip() == return_on_string:
                    return dict(stdout=stdout, stderr=stderr, process=process)

        # Process is closed and we've read all of the outputs.
        if process.poll() is not None:
            if not had_output:
                break

    # Match the return object of subprocess.run.
    return dict(returncode=process.poll(), stdout=stdout, stderr=stderr)
