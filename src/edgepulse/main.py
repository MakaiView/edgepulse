from time import sleep

import typer

from edgepulse.config.config import Config
from edgepulse.core.status import Status, StatusLevel
from edgepulse.drivers.factory import DriverFactory
from edgepulse.renderers.led_renderer import SingleLEDRenderer

app = typer.Typer(help="EdgePulse - Raspberry Pi status and health agent.")


@app.command()
def version() -> None:
    """Show the EdgePulse version."""
    print("EdgePulse v0.1.0")


@app.command()
def doctor() -> None:
    """Verify the installation."""
    print("✅ EdgePulse is installed correctly.")


@app.command()
def demo() -> None:
    """Run the indicator demonstration."""

    config = Config()

    driver = DriverFactory.create(config)
    renderer = SingleLEDRenderer(driver)

    print("\n=== EdgePulse Demo ===\n")

    for level in StatusLevel:

        print(f"\nStatus: {level.name}")

        renderer.render(
            Status(
                level=level,
                message=level.name,
            )
        )

        sleep(2)

    driver.cleanup()


def main() -> None:
    app()
