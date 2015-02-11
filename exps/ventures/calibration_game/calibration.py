# -*- coding: utf-8 -*-
#!/usr/bin/env python
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
# Author:
#     Anna Chabuda <anna.chabuda@gmail.com>
#

import pygame
from pygame.locals import *
pygame.mixer.init()

from obci.exps.ventures.calibration_game.calibration_screen import CalibrationScreen
from obci.exps.ventures import logic_queue

class Calibration(logic_queue.LogicQueue):
    def __init__(self):
        super(Calibration, self).__init__()
        self._screen = CalibrationScreen()

    def run(self):
        done = False
        while not done:
            for event in pygame.event.get():                  
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.finish_calibration()
                    done = True
            sample = self.get_message()
            if sample is not None:
                self._screen.update_block(sample.key, sample.value)

    def finish_calibration(self):
        pass

if __name__ == '__main__':
    Calibration().run()

        
