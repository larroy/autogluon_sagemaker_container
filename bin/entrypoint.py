#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Description"""

import logging
import os
import sys
import fire
from subprocess import check_call

logger = logging.getLogger(__name__)


def script_name() -> str:
    """:returns: script name with leading paths removed"""
    return os.path.split(sys.argv[0])[1]

def config_logging(level: int=logging.INFO):
    import time
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format="{}: %(asctime)sZ %(levelname)s %(message)s".format(script_name()))
    logging.Formatter.converter = time.gmtime


class Command:
    def train(self) -> None:
        logger.info("train")

    def serve(self) -> None:
        logger.info("serve")


def main():
    config_logging()
    print(os.getcwd())
    print(sys.argv)
    check_call("pwd")
    fire.Fire(Command)
    return 0

if __name__ == '__main__':
    sys.exit(main())


