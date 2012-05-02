# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# OpenBCI - framework for Brain-Computer Interfaces based on EEG signal
# Project was initiated by Magdalena Michalska and Krzysztof Kulewski
# as part of their MSc theses at the University of Warsaw.
# Copyright (C) 2008-2009 Krzysztof Kulewski and Magdalena Michalska
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
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>
#

"""
>>> import os

>>> from ..signal import info_file_proxy as p

>>> px = p.InfoFileWriteProxy('./tescik.obci.svarog.info')

>>> px.set_attributes({'number_of_channels':2, 'sampling_frequency':128, 'channels_names': ['1','2'], 'file':'soufce.obci.dat', 'number_of_samples':3})

>>> px.finish_saving()
'./tescik.obci.svarog.info'

>>> py = p.InfoFileReadProxy('./tescik.obci.svarog.info')

>>> print(py.get_param('number_of_channels'))
2

>>> print(py.get_param('channels_names')[0])
1

>>> os.remove('./tescik.obci.svarog.info')

"""
def run():
    import doctest, sys
    res = doctest.testmod(sys.modules[__name__])
    if res.failed == 0:
        print("All tests succeeded!")

if __name__ == '__main__':
    run()