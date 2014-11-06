#!/usr/bin/python
# vim:ts=4:sts=4:sw=4:et:wrap:ai:fileencoding=utf-8:
#
# Copyright 2014 Albert De La Fuente Vigliotti
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
Tool to generate a servers file to be used with pyCloudSim
> gen-servers.py <count>
"""
__version__ = "0.1"
__author__ = "Albert De La Fuente Vigliotti"


import time
import json
import argparse


class HostsGenerator():
    def __init__(self):
        self.host_count = 0

    def get_default_arg(self, default_value, arg):
        if arg is None:
            return default_value
        else:
            return arg

    def save_json(self, filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='A servers config file generation tool.')
        parser.add_argument('-pm', '--pmcount',
                            help='Number of physical machines', required=False)
        parser.add_argument('-spec', '--specpower',
                            help='SPECpower profile to use \
                            (string filename without path)',
                            required=False)
        parser.add_argument('-o', '--outfile',
                            help='Output filename', required=False)
        args = parser.parse_args()

        self.pmcount = int(self.get_default_arg(100, args.pmcount))
        default_spec = "power_ssj2008-20140615-00658.html"
        self.specpower = self.get_default_arg(default_spec, args.specpower)
        self.outfile = self.get_default_arg("servers.json", args.outfile)

    def run(self):
        self.parse_args()
        hosts = []
        for id in range(1, self.pmcount+1):
            host = {}
            host['id'] = str(id)
            host['specpower'] = self.specpower
            hosts += [host]
        data = {}
        data['pms'] = hosts
        self.save_json(self.outfile, data)


def run():
    start_time = time.time()
    main = HostsGenerator()
    try:
        main.run()
    except KeyboardInterrupt:
        print('Canceled by user')
    print("--- {} seconds ---".format(time.time() - start_time))

if __name__ == "__main__":
    run()

