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


class Window:

    def __init__(self, existingWindowId: int = -1) -> None:
        pass

    def setProperty(self, key: str, value: str) -> None:
        pass

class ListItem:

    def __init__(self, label, label2=None, path=None, offscreen=None):
        self.__label = label

    def setArt(self, value):
        print(f'listItem "{self.__label}": setArt({value})')

    def setProperty(self, _property, value):
        print(f'listItem "{self.__label}": setProperty({_property}, {value})')

    def setInfo(self, type, infoLabels):
        print(f'listItem "{self.__label}": setInfo({type}, {infoLabels})')

    def addContextMenuItems(self, contextMenu):
        print(f'listItem "{self.__label}": addContextMenuItems({contextMenu})')

class Dialog:

    @staticmethod
    def yesno(heading, message, nolabel = None, yeslabel = None, autoclose = None):
        print(f'yesno({heading}, {message}, {nolabel}, {yeslabel}, {autoclose})')
        return True

    @staticmethod
    def notification(heading, message, icon = None, time = 5000, sound = True):
        print(f'notification({heading}, {message}, {icon}, {time}, {sound})')
