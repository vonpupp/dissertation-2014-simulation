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
2014 Globecom Simulations
"""
__version__ = "0.2"
__author__ = "Albert De La Fuente Vigliotti"


import os


def eval_os_var(default_value, var_name):
    result = default_value
    value = os.environ.get(var_name)
    if value is not None:
        result = eval(value)
    return result

#def str_os_var(default_value, var_name):
#    result = default_value
#    value = os.environ.get(var_name)
#    if value is not None:
#        result = value.lower()
#    return result

def bool_os_var(default_value, var_name):
    result = default_value
    value = os.environ.get(var_name)
    if value is not None:
        result = value.lower() == 'true'
    return result

algorithm_scenarios = [
    'EnergyUnawareStrategyPlacement',
    'OpenOptStrategyPlacement',
    'EvolutionaryComputationStrategyPlacement',
    'OpenOptStrategyPlacementMem',
#    'EvolutionaryComputationStrategyPlacementNet',
]

# Setup the scenarios
host_scenarios = [100]
simulation_scenarios = range(1, 31)
vms_start = 16
vms_stop = 144
vms_step = 16


# Variable override with the OS variables
host_scenarios = eval_os_var(host_scenarios, 'HOST_SCENARIOS')
simulation_scenarios = eval_os_var(simulation_scenarios, 'SIMULATION_SCENARIOS')
vms_start = eval_os_var(vms_start, 'VMS_START')
vms_stop  = eval_os_var(vms_stop, 'VMS_STOP')
vms_step  = eval_os_var(vms_step, 'VMS_STEP')

seu = bool_os_var(False, 'SIMULATE_EU')
if seu:
    algorithm_scenarios += ['EnergyUnawareStrategyPlacement']

sksp = bool_os_var(False, 'SIMULATE_KSP')
if sksp:
    algorithm_scenarios += ['OpenOptStrategyPlacement']

sec = bool_os_var(False, 'SIMULATE_EC')
if sec:
    algorithm_scenarios += ['EvolutionaryComputationStrategyPlacement']

skspmem = bool_os_var(False, 'SIMULATE_KSP_MEM')
if skspmem:
    algorithm_scenarios += ['OpenOptStrategyPlacementMem']

secnet = bool_os_var(False, 'SIMULATE_EC_NET')
if secnet:
    algorithm_scenarios += ['EvolutionaryComputationStrategyPlacementNet']
