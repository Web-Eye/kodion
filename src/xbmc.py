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

class Keyboard:

    def __init__(self, default=None, heading=None, hidden=None):
        self._default = default
        self._heading = heading
        self._hidden = hidden

    def setDefault(self, default):
        self._default = default

    def setHeading(self, heading):
        self._heading = heading

    def setHiddenInput(self, hidden):
        self._hidden = hidden

    def doModal(self):
        pass

    def isConfirmed(self):
        return True

    def getText(self):
        return self._default

