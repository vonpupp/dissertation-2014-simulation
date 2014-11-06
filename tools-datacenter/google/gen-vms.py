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
Tool to generate a VMs file with Google workloads to be used with pyCloudSim
"""
__version__ = "0.1"
__author__ = "Albert De La Fuente Vigliotti"


import time
import json
import argparse
import csv


class VMsGenerator():
    def __init__(self):
        self.host_count = 0

    def get_default_arg(self, default_value, arg):
        if arg is None:
            return default_value
        else:
            return arg

    def save_json(self, filename, data):
        with open(filename, 'w') as outfile:
            json.dump(data, outfile, indent=4, sort_keys=True)

    def load_input_file(self, filename):
        fh = open(filename, 'r')
        return csv.reader(fh)
        #for row in reader:
        #print(" ".join(row))

#    def clean_prefix(self, filename):
#        r = filename.split(self.remove_prefix)[1]
#        r = r.replace('\r', '')
#        r = r.replace('\n', '')
#        return r



    def parse_args(self):
        parser = argparse.ArgumentParser(
            description='A VMs config file generation tool.')
        parser.add_argument('-vm', '--vmcount',
                            help='Number of virtual machines', required=False)
        parser.add_argument('-i', '--infile',
                            help='Input filename (use tracegen.py tool)',
                            required=False)
        parser.add_argument('-o', '--outfile',
                            help='Output filename', required=False)
        args = parser.parse_args()

        #self.remove_prefix = "/home/vagrant/research/static-simulation/tools-traces/../"
        self.vmcount = int(self.get_default_arg(128, args.vmcount))
        filtered_file = '../../google-workload-traces/filtered.csv'
        self.infile = self.get_default_arg(filtered_file, args.infile)
        self.outfile = self.get_default_arg('vms.json', args.outfile)

    def run(self):
        self.parse_args()
        f = self.load_input_file(self.infile)
        f.next()
        vms = []
        id = 1
        for row in f:
            trace = {}
            job_id = row[1]  # job_id
            task_index= row[2]  # task_index
            prefix = 'google-workload-traces/task_usage-job_id_{}-task_index_{}'\
                .format(job_id, task_index)
            prefix += '_{}.txt'
            for resource in ['cpu', 'mem', 'disk', 'net']:
                trace[resource]  = prefix.format(resource)

            vm = {}
            vm['id'] = str(id)
            vm['flavor'] = 'small'
            vm['trace'] = trace
            vms += [vm]
            if id == self.vmcount:
                break
            id += 1
        data = {}
        data['vms'] = vms
        self.save_json(self.outfile, data)


def run():
    start_time = time.time()
    main = VMsGenerator()
    try:
        main.run()
    except KeyboardInterrupt:
        print('Canceled by user')
    print("--- {} seconds ---".format(time.time() - start_time))

if __name__ == "__main__":
    run()
