import os 
from box.exceptions import BoxValueError
import yaml
from RedWineQualityPrediction import logger
import json
import joblib 
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns configBox
    
    Args: 
        path_to_yaml (str): path like input
    
    Raises: 
        ValueError: if yaml file is empty or not valid
        e: empty file
      
    Returns:
        configBox: configBox object
    """
    try:
        with open (path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates directories
    
    Args: 
        path_to_directories (list): list of path of directories 
        ignore_log(bool, optional): ignore if multiple dirs is created. Defaults to False  
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"directory: {path} created successfully")
 

@ensure_annotations
def save_json(path:Path, data:dict):
    """saves json file
    
    Args: 
        path (str): path to save json file
        data (dict): data to save
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file: {path} saved successfully")


@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    """loads json file and returns configBox
    
    Args: 
        path (str): path to load json file
    
    Returns:
        configBox: configBox object
    """
    with open(path) as f:
        data = json.load(f)
        logger.info(f"json file: {path} loaded successfully")
        return ConfigBox(data)
    

@ensure_annotations
def save_bin(data:Any, path:Path):
    """saves binary file
    
    Args: 
        data (Any): data to save as binary 
        path (str): path to save binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file: {path} saved successfully")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """loads binary file and returns data
    
    Args: 
        path (str): path to load binary file
    """
    data = joblib.load(path)
    logger.info(f"binary file: {path} loaded successfully")
    return data


@ensure_annotations
def get_size(path:Path) -> str:
    """get size in KB
    
    Args: 
        path (str): path to file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

@ensure_annotations
def decodeImage(imgstring, filename):
    """decodes image from base64 string
    
    Args: 
        imgstring (str): base64 string of image
        filename (str): filename of image
    
    Returns:
        str: decoded image
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


@ensure_annotations
def encodeImageIntoBase64(croppedImagePath):
    """encodes image to base64 string
    
    Args: 
        filename (str): filename of image
    
    Returns:
        str: base64 string of image
    """
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())