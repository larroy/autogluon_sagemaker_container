#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Description"""

import logging
import os
import sys
from autogluon_container import common
from autogluon_container.train import train
import argparse
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


def main():
    config_logging()
    print(os.getcwd())
    print(sys.argv)
    check_call("pwd")
    execution_context = common.create_execution_context()
    arg_parser: argparse.ArgumentParser = common.setup_arg_parser()
    args = arg_parser.parse_args()
    print(args.cmd)
    print(str(execution_context))
    if args.cmd == 'train':
        train(execution_context)
    elif args.cmd == 'serve':
        serve(execution_context)
    return 0

if __name__ == '__main__':
    sys.exit(main())


