"""
Copyright (c) 2013-2014, Sam Dodrill
All rights reserved.

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

    1. The origin of this software must not be misrepresented; you must not
    claim that you wrote the original software. If you use this software
    in a product, an acknowledgment in the product documentation would be
    appreciated but is not required.

    2. Altered source versions must be plainly marked as such, and must not be
    misrepresented as being the original software.

    3. This notice may not be removed or altered from any source
    distribution.
"""

import time

class Logger():
    def __init__(self, logpath=None, lbufmax=15):
        self.fout = None
        self._linebufnum = 0
        self._lbufmax = lbufmax

        if not logpath == None:
            self.fout = open(logpath, "a")

    def log(self, line):
        if self.fout == None:
            print line
        else:
            self.fout.write(str(time.ctime()) + " " + str(line) + "\n")

        if self._linebufnum == self._lbufmax:
            self.fout.flush()
            self._linebufnum = 0
        else:
            self._linebufnum += 1
