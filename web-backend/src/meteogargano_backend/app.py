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

class Application:

    def __init__(self):
        with open(os.path.join(resources.files(data),
                                "static/index.html"), "r") as f:
            print(f.readlines()[0])

        with open(os.path.join(resources.files(data),
                                "__version__"), "r") as f:
            version = f.readlines()[0].strip()

        parser = argparse.ArgumentParser(
            prog=f"{NAME}",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter)

        parser.add_argument("-v", "--verbosity",
                            action="count",
                            help="increase output verbosity")

        parser.add_argument(dest="config",
                            help="config file path")

        args = parser.parse_args()

        logging.basicConfig(
            stream=sys.stderr, level="DEBUG",
            format="[%(asctime)s]%(levelname)s %(funcName)s() "
                    "%(filename)s:%(lineno)d %(message)s")

        try:
            with open(args.config, "r") as f:
                settings_dict = json.load(f)
        except BaseException as e:
            logging.error("unable to load config file")
            traceback.print_exc(file=sys.stderr)
            raise e

        self.app = FastAPI()

    async def serve(self):
        app: FastAPI = self.app

        @app.get("/",  response_class=FileResponse)
        def index() -> FileResponse:
            return FileResponse(os.path.join(resources.files(data), "static",
                                             "index.html"), media_type="html")

        # serve
        config = uvicorn.Config(app, host="127.0.0.1", port=8000)
        server = uvicorn.Server(config)
        await server.serve()

    @app.get("/")
    def read_root():
        return {"Hello": "World"}

def main():
    instance = Application()
    asyncio.run(instance.serve())

if __name__ == "__main__":
    main()

