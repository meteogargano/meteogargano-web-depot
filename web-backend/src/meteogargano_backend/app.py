import os
import logging
import sys
import argparse
import traceback
import json
from importlib import resources

from . import data

DESCRIPTION = "Meteogargano web backend"
NAME = "meteogargano_backend"

class Application:

    def main(self):
        with open(os.path.join(resources.files(data),
                                "static/index2.html"), "r") as f:
            print(f.readlines()[0])

        with open(os.path.join(resources.files(data),
                                "__version__"), "r") as f:
            version = f.readlines()[0].strip()

        logging.basicConfig(
            stream=sys.stderr, level="DEBUG",
            format="[%(asctime)s]%(levelname)s %(funcName)s() "
                    "%(filename)s:%(lineno)d %(message)s")

        parser = argparse.ArgumentParser(
            prog=f"{NAME}",
            description=DESCRIPTION,
            formatter_class=argparse.RawDescriptionHelpFormatter)

        parser.add_argument("-v", "--verbosity",
                            action="count",
                            help="increase output verbosity")
