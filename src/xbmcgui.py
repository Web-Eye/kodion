# -*- coding: utf-8 -*-
# Copyright 2022 WebEye
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def getScreenHeight():
    return 1080


def getScreenWidth():
    return 1920


class ListItem:

    def __init__(self, title):
        self.__title = title

    def setArt(self, value):
        print(f'listItem "{self.__title}": setArt({value})')

    def setProperty(self, _property, value):
        print(f'listItem "{self.__title}": setProperty({_property}, {value})')

    def setInfo(self, type, infoLabels):
        print(f'listItem "{self.__title}": setInfo({type}, {infoLabels})')

    def addContextMenuItems(self, contextMenu):
        print(f'listItem "{self.__title}": addContextMenuItems({contextMenu})')

