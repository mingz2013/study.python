# -*- coding: utf-8 -*-
"""
@FileName: main.py
@Time: 2020/5/29 11:10
@Author: zhaojm

Module Description

"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


def main():
    import app
    app.run()


if __name__ == '__main__':
    main()
