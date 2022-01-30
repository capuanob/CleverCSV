# -*- coding: utf-8 -*-

"""
CleverCSV Command line application.

"""

from cleo import Application

from .. import __version__
from .commands import CodeCommand
from .commands import DetectCommand
from .commands import ExploreCommand
from .commands import StandardizeCommand
from .commands import ViewCommand
from .config import Config


def build_application():
    config = Config("clevercsv", __version__)
    app = Application(config=config, complete=False)
    app.add(ViewCommand())
    app.add(DetectCommand())
    app.add(StandardizeCommand())
    app.add(CodeCommand())
    app.add(ExploreCommand())
    return app
