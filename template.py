import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "disease_cnn_classifier"

file_list = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html"


]


for path in file_list:
    path = Path(path)
    dir, name = os.path.split(path)


    if dir !="":
        os.makedirs(dir, exist_ok=True)
        logging.info(f"Directory {dir} created")

    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w") as f:
            pass
            logging.info(f"Creating new file: {path}")

    else:
        logging.info(f"{name} is already a file")