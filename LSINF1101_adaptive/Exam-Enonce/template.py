#! /usr/bin/python3
# -*- coding: utf-8 -*-

#   Copyright (c) Ludovic Taffin - December 2018
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

def func():
    try:
@        @sandbox@@
        return 127
    except Exception as e:
        print(e)
        return -1

if __name__ == '__main__':
    sys.exit(func())
    