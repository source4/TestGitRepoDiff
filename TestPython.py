# -*- coding: utf-8 -*-

"""
  Created by Stanislav Khvalinskyi on 9/25/17.
  Copyright © 2017 Atlassian. All rights reserved.
"""

from subprocess import Popen, PIPE
from re import split


class Proc(object):
    """Data structure for a processes . The class properties are process attributes"""

    def __init__(self, proc_info):
        self.user = proc_info[0]
        self.pid = proc_info[1]
        self.cpu = proc_info[2]
        self.mem = proc_info[3]
        self.vsz = proc_info[4]
        self.rss = proc_info[5]
        self.tty = proc_info[6]
        self.stat = proc_info[7]
        self.start = proc_info[8]
        self.time = proc_info[9]
        self.cmd = proc_info[10]

    def to_str(self):
        """ Returns a string containing minimalistic info
        about the process : user, pid, and command """
        return '%s %s %s' % (self.user, self.pid, self.cmd)

    @staticmethod
    def get_proc_list():
        """ Retrieves a list [] of Proc objects representing the active
        process list list """
        proc_list = []
        sub_proc = Popen(['ps', 'aux'], shell=False, stdout=PIPE)
        # Discard the first line (ps aux header)
        sub_proc.stdout.readline()
        for line in sub_proc.stdout:
            # The separator for splitting is 'variable number of spaces'
            proc_info = split(" *", line.strip())
            proc_list.append(Proc(proc_info))
        return proc_list
