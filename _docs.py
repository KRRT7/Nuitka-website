import sys
from pathlib import Path
from shutil import rmtree

from invoke import Collection, task

@task(name="clean")
def _clean(c):
    """
    Clean the build directory by removing the output directory.

    Args:
        c (invoke.Context): The context instance (passed automatically).
    """
    output = Path(c.sphinx.target)
    if output.exists():
        print(f"delete {output}")
        rmtree(output)

@task(
    default=True,
    help={
        "opts": "Extra sphinx-build options/args",
        "nitpick": "Build with stricter warnings/errors enabled",
        "source": "Source directory; overrides config setting",
        "target": "Output directory; overrides config setting",
    },
)
def build(c, opts=None, language=None, source=None, target=None, nitpick=False):
    """
    Build the project's Sphinx documentation.

    Args:
        c (invoke.Context): The context instance (passed automatically).
        opts (str, optional): Extra sphinx-build options/args. Defaults to None.
        language (str, optional): Language to build the documentation in. Defaults to None.
        source (str, optional): Source directory; overrides config setting. Defaults to None.
        target (str, optional): Output directory; overrides config setting. Defaults to None.
        nitpick (bool, optional): Build with stricter warnings/errors enabled. Defaults to False.
    """
    if opts is None:
        opts = ""
    source = source or c.sphinx.source
    target = target or c.sphinx.target
    if language:
        opts = f"-D language={language}"
        target = f"{target}/{language}"
    if nitpick:
        opts += " -n -W -T"
    cmd = f"pipenv run sphinx-build {opts} {source} {target}"
    c.run(cmd)

@task
def update(c, language="en"):
    """
    Update the POT file and invoke the `sphinx-intl` `update` command.

    Args:
        c (invoke.Context): The context instance (passed automatically).
        language (str, optional): Language to update the documentation for. Defaults to "en".

    Only used with `invoke intl.update`.
    """
    opts = "-b gettext"
    target = Path(c.sphinx.target).parent / "output/gettext"
    if language == "en":
        _clean(c)
        build(c, target=target, opts=opts)
    else:
        if not Path(target).exists():
            build(c, target=target, opts=opts)
        c.run(f"pipenv run sphinx-intl update -p {target} -l {language}")
        # for DIR in ['pages', 'posts', 'shop']:
        #     rmtree(f'locales/{language}/LC_MESSAGES/{DIR}/')

def _site(name, help_part):
    """
    Create a collection of tasks for building a specific part of the site.

    Args:
        name (str): The name of the site part.
        help_part (str): The help description for the site part.

    Returns:
        invoke.Collection: A collection of tasks for the specified site part.
    """
    self = sys.modules[__name__]
    coll = Collection.from_module(
        self,
        name=name,
        config={"sphinx": {"source": name, "target": "output"}},
    )
    coll.__doc__ = f"Tasks for building {help_part}"
    coll["build"].__doc__ = f"Build {help_part}"
    return coll

# Sites
intl = _site("intl", "the translations sub-site.")
site = _site("site", "the main site.")
bundle = _site("bundle", "package documentation bundle.")

ns = Collection(intl, site, bundle)
