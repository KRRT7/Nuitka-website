import os
import sys

from invoke import Collection, task

from _docs import bundle, intl, site

# Disable pipenv warning, we run potentially inside the virtualenv already,
# Visual Code e.g. picks it up and there is no harm in that. This is only
# to not confuse people with a pipenv warning that it may not be working.
os.environ["PIPENV_VERBOSITY"] = "-1"
os.environ["PIPENV_IGNORE_VIRTUALENVS"] = "1"


@task
def virtualenv(c):
    """
    Create and install the virtual environment.

    Args:
        c (invoke.Context): The context instance (passed automatically).
    """
    c.run(f"{sys.executable} -m pip install -U pipenv")
    c.run(f"{sys.executable} -m pipenv install --dev")

    # Workaround pipenv failing to pin black version due to it being pre-release
    # always.
    # c.run(f"{sys.executable} -m pipenv run python -m pip install black==24.10.0")


@task
def run(c, target="build-site"):
    """
    Run a specific target task.

    Args:
        c (invoke.Context): The context instance (passed automatically).
        target (str, optional): The target task to run. Defaults to "build-site".
    """
    c.run(f"{sys.executable} -m pipenv run python update.py --{target}")


ns = Collection(intl, site, bundle, run, virtualenv)
