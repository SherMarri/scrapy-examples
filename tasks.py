from typing import Any
from invoke import task


@task
def clean(c: Any) -> None:
    """
    Clean up the project and remove all temporary .pyc files
    and local application logs"
    """
    print("Cleaning up...")
    c.run("find . -name '*.py[co]' -exec rm -f '{}' ';'")
    c.run("find . -name 'application.log*' -exec rm -f '{}' ';'")
    print("Cleaning up succeed")


@task
def start(c: Any) -> None:
    """
    Build and start all services
    """
    c.run(f"scrapy crawl latest_ads", pty=True)


@task
def deploy(c: Any) -> None:
    """
    Deploy function
    """
    c.run(
        """
            cd venv/lib/python3.9/site-packages &&
            zip -r ../../../../deployment-package.zip .
        """,
        pty=True,
    )
    c.run("zip -g deployment-package.zip lambda_function.py", pty=True)
    c.run("zip -r deployment-package.zip pakwheels", pty=True)
    c.run(
        "aws lambda update-function-code --function-name PakwheelsLatestAds --zip-file fileb://deployment-package.zip",
        pty=True,
    )
