# -*- coding: utf-8 -*- 
import logging
import sys

from rich.console import Console
from rich.logging import RichHandler

# configure logging here because some other later imported library does it first otherwise
# TODO: use a fileconfig
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=Console(file=sys.stderr))]
)

from .version import __version__  # noqa
from .ffsubsync import main  # noqa

