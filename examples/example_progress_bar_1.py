#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
import sys
from time import sleep
from gooey import Gooey, GooeyParser


@Gooey(progress_regex=r"^(Epoch ((\d+)\/(\d+)):)(.*)]$")
def main():
    parser = GooeyParser(prog="example_progress_bar_1")
    _ = parser.parse_args(sys.argv[1:])
    totalNumber = 15
    for i in range(totalNumber):
        print("Epoch {}/{}:  ]".format(i + 1, totalNumber))
        sys.stdout.flush()
        sleep(0.1)


if __name__ == "__main__":
    sys.exit(main())
