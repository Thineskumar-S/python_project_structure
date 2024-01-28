import os
from pathlib import Path


project_name="prac_proj1"

list_of_files=['setup.py',"requirements.txt","Dockerfile","readme.md","app.py","y_files/parmas.yaml","y_files\config.yaml",
               f"src\{project_name}\ __init__.py",
               f"src\{project_name}\logging.py",
               f"src\{project_name}/exception.py",
               f"src\{project_name}/components\ __init__.py",
               f"src\{project_name}/components\Data_ingestion.py",
               f"src\{project_name}/components\Data_Transformation.py",
               f"src\{project_name}/components\Model_trainer.py",
               f"src\{project_name}/components\Model_evaluator.py",
               f"src\{project_name}/config\__init__.py",
               f"src\{project_name}/config\configuration.py",
               f"src\{project_name}/utilities\__init__.py",
               f"src\{project_name}/utilities\common.py",
               f"src\{project_name}/entities/__init__.py",
               f"src\{project_name}/entities\config_enity.py",
               f"src\{project_name}/pipeline/__init__.py",
               f"src\{project_name}/pipeline\stage_1.py",
               f"src\{project_name}/pipeline\stage_2.py",
               f"src\{project_name}/pipeline\stage_3.py",
               f"src\{project_name}/pipeline\stage_4.py",
               f"src\{project_name}\pipeline/predict_pipeline.py",
               "templates/index.html",
               "templates/home.html",
               "notebooks/experiement-1.ipynb",
               "notebooks/EDA.ipynb",
               "notebooks/Data_viz.ipynb"]


for file_path in list_of_files:

    file_path=Path(file_path)

    file_dir,file_name=os.path.split(file_path)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
    
    if (not (os.path.exists(file_path))):
        with open(file_path,"w") :
            pass
    else:
        print(f"the file is created on this path {file_name}")
