import os
import logging
import sys
import argparse
import traceback
import json
from importlib import resources
import asyncio

from . import data

import uvicorn
from fastapi import FastAPI, Request, Depends

from fastapi.responses import HTMLResponse, FileResponse

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DESCRIPTION = "Meteogargano web backend"
NAME = "meteogargano_backend"

app = FastAPI()

with open(os.path.join(resources.files(data),
                        "__version__"), "r") as f:
    version = f.readlines()[0].strip()

logging.basicConfig(
    stream=sys.stderr, level="DEBUG",
    format="[%(asctime)s]%(levelname)s %(funcName)s() "
            "%(filename)s:%(lineno)d %(message)s")


config_path = os.environ.get("CONFIG_PATH")

assert config_path is not None, "CONFIG_PATH env variable not set."

try:
    with open(config_path, "r") as f:
        settings_dict = json.load(f)
except BaseException as e:
    logging.error("unable to load config file")
    traceback.print_exc(file=sys.stderr)
    raise e


@app.get("/",  response_class=FileResponse)
def index() -> FileResponse:
    return FileResponse(os.path.join(resources.files(data), "static",
                                        "index.html"), media_type="html")


def main():
    uvicorn.run(app)

if __name__ == "__main__":
    main()

