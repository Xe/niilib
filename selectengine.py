"""
Copyright (c) 2014, Christine Dodrill
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

from select import select

class SelectEngine:
    def __init__(self):
        self.socks = []
        self.callbacks = {}
        self.argpass = {}

    def go(self):
        if len(socks) > 0:
            _go()
        else:
            raise IndexError

    def _go():
        while True:
            inputready, outputready, execeptready = select(self.socks,[],[])

            for s in inputready:
                self.callbacks[s]([s, self, self.argpass[s]])

            if len(self.socks) == 0:
                break

    def add_callback(self, socket, callback, args):
        self.socks.append(socket)
        self.callbacks[socket] = callback
        self.argpass[socket] = args

    def del_callback(self, socket):
        self.socks.remove(socket)
        self.callbacks.pop(socket)
        self.argpass.pop(socket)

