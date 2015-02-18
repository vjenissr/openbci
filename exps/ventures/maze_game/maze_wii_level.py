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
from constants.constants_wii_levels import AREA_SIZE, STEP_UP, STEP_DOWN

class MazeWiiLevel(object):
    def __init__(self, session_type, wii_level_params):
        super(MazeWiiLevel, self).__init__()
        self.session_type = session_type
        self._init_wii_level_params(wii_level_params)

    def _get_area_value(self, level, motor_step, motor_initial, session_number):
        level = level + (motor_initial + session_number - 1) * motor_step
        return level-(AREA_SIZE/2), (level+AREA_SIZE/2), level

    def _init_wii_level_params(self, wii_level_params):
        self.level_params = {'right':{'step_up':STEP_UP, 'step_down':STEP_DOWN},
                             'left' :{'step_up':STEP_UP, 'step_down':STEP_DOWN},
                             'down' :{'step_up':STEP_UP, 'step_down':STEP_DOWN},
                             'up'   :{'step_up':STEP_UP, 'step_down':STEP_DOWN}}
        for direction in ['right', 'left', 'up', 'down']:
            area_start_value, area_end_value, level = self._get_area_value(wii_level_params[direction], 
                                                                           wii_level_params['motor_step'],
                                                                           wii_level_params['motor_initial'], 
                                                                           wii_level_params['session_number'])    
            self.level_params[direction]['area_start_value'] = area_start_value
            self.level_params[direction]['area_end_value'] = area_end_value
            self.level_params[direction]['level'] = level

    def get_level(self, direction):
        return (self.level_params[direction]['step_up'], 
                self.level_params[direction]['step_down'], 
                self.level_params[direction]['area_start_value'],
                self.level_params[direction]['area_end_value'])

    def load_level(self, direction, level):
        pass