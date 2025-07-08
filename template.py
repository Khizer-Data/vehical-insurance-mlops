import os
import pathlib as Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/data_trainer.py",
    f"{project_name}/components/data_evaluation.py",
    f"{project_name}/components/data_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/gdrive_connection.py",
    f"{project_name}/cloudstorage/__init__.py",
    f"{project_name}/cloudstorage/gdrive_storage",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/gdrive_estimator.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "requirements.txt",
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "demo.py",
    "setup.py",
    "pyproject.toml",
    "config/model.yaml",
    "config/schema.yaml"
]

for filepath in list_of_files:
    filepath = Path.Path(filepath)
    filedr,filename = os.path.split(filepath)
    if filedr != "":
        os.makedirs(filedr,exist_ok=True)
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)) == 0 ):
        with open(filepath,"w") as f:
            pass
    else:
        print(f"File is already present at :{filepath}")
