import os

from invoke import task


def print_and_run(c, cmd):
    print("Running cmd:\n$ " + cmd)
    c.run(cmd, pty=True)  #!/bin/bash


@task
def clean(c):
    """
    Clean up the project and remove all temporary .pyc files
    and local application logs"
    """
    print("Cleaning up...")
    c.run("find . -name '*.py[co]' -exec rm -f '{}' ';'")
    c.run("find . -name 'application.log*' -exec rm -f '{}' ';'")
    print("Cleaning up succeed")


@task
def start(c):
    """
    Build and start all services
    """
    c.run(f"scrapy crawl latest_ads", pty=True)


@task
def deploy(c):
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
