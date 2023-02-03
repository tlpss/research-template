import os 
import pathlib
from shutil import rmtree

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ROOT_DIR = pathlib.Path(PROJECT_DIRECTORY).parent

REMOVE_PATHS = []

if '{{cookiecutter.use_mypy}}' != "y":
    REMOVE_PATHS.append(".github/workflows/mypy.yaml")
    REMOVE_PATHS.append("mypy.ini")


for path in REMOVE_PATHS:
    path = path.strip()
    path = os.path.join(PROJECT_DIRECTORY, path)
    print(path)
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)


if os.path.exists(ROOT_DIR / ".git"):
    print("test")
    # was created in a git repo, so we should remove the template
    print("heh")
    #os.rmdir(os.path.join(ROOT_DIR,"{" + "{" + "cookiecutter.repo_name}}"))
    rmtree(ROOT_DIR / "test")
    rmtree(ROOT_DIR  /"hooks")
    rmtree(ROOT_DIR  /".vscode")

