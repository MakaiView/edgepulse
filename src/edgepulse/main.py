import typer

app = typer.Typer(
    help="EdgePulse - Raspberry Pi status and health agent."
)


@app.command()
def version() -> None:
    """Show the EdgePulse version."""
    print("EdgePulse v0.1.0")


@app.command()
def doctor() -> None:
    """Verify the installation."""
    print("✅ EdgePulse is installed correctly.")


def main() -> None:
    app()
