#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:
#
# Copyright 2013-2014 Albert De La Fuente Vigliotti
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
2014 Simulations
"""
__version__ = "0.2"
__author__ = "Albert De La Fuente Vigliotti"


import os
import scenariosvars
import sys
import time


class Simulate():
    def __init__(self):
        self.seu          = 1
        self.sksp         = 1
        self.skspmem      = 1
        self.sec          = 1
        self.secnet       = 1
        # Not used
        self.skspnetgraph = 0
        self.secnetgraph  = 0

    def gen_params(self):

        params = ''
        if self.seu == 1:
            params += '-seu 1 '
        if self.sksp == 1:
            params += '-sksp 1 '
        if self.skspmem == 1:
            params += '-skspmem 1 '
        if self.skspnetgraph == 1:
            params += '-skspnetgraph 1 '
        if self.sec == 1:
            params += '-sec 1 '
        if self.secnet == 1:
            params += '-secnet 1 '
        if self.secnetgraph == 1:
            params += '-secnetgraph 1 '
        self.params = params

    def change_cwd(self):
        # Get CWD
        self.abspath = os.path.abspath(__file__)
        self.dname = os.path.dirname(self.abspath)
        self.pycloudsim_path = os.path.join(self.dname, 'pyCloudSim')

        # Import and initialize the logging facility
    #    sys.path.append(pycloudsim_path)
    #    import pycloudsim.common as common
    #    config = common.read_and_validate_config()
    #    common.init_logging(
    #        config['log_directory'],
    #        'simulation.log',
    #        int(config['log_level']))

        # Change current directory
        os.chdir(self.pycloudsim_path)

    def parse_args(self):
        self.conf = 'pycloudsim.conf'
        if len(sys.argv) > 1:
            self.conf = os.path.join(self.dname, sys.argv[1])

    def run(self):
        self.gen_params()
        self.change_cwd()
        self.parse_args()

        for host in scenariosvars.host_scenarios:
            command = []
            for simulation in scenariosvars.simulation_scenarios:
                #import ipdb; ipdb.set_trace() # BREAKPOINT
                command = 'python pycloudsim.py -c {} -pm {} -vma {} -vmo {} -vme {} {}'\
                    .format(self.conf, host,
                            scenariosvars.vms_start,
                            scenariosvars.vms_stop,
                            scenariosvars.vms_step,
                            self.params)
                os.system(command)


if __name__ == "__main__":
    start_time = time.time()
    s = Simulate()
    try:
        s.run()
    except KeyboardInterrupt:
        print('Canceled by user')
    print("--- {} seconds ---".format(time.time() - start_time))
