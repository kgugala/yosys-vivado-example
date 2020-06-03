#!/usr/bin/env python3

import edalize
import os
import glob

work_root = 'build'
os.makedirs(work_root, exist_ok=True)

synth_tool = 'yosys'
yosys_synth_options = ['-iopad', '-family xc7']

srcs = glob.glob("*.v", recursive=True)

files = [
    {'name': os.path.realpath('arty.xdc'), 'file_type': 'xdc'},
]

for src in srcs:
      files.append({'name': os.path.realpath(src), 'file_type': 'verilogSource'})

parameters = {}
tool = 'vivado'
incdirs = {}
edam = {
  'files' : files,
  'name'  : 'design',
  'toplevel': 'top',
  'parameters': parameters,
  'tool_options' : {'vivado' : {
    'part' : 'xc7a35ticsg324-1L',
    'synth' : synth_tool,
    'yosys_synth_options' : yosys_synth_options
    }}
}

backend = edalize.get_edatool(tool)(edam=edam, work_root=work_root)
backend.configure("")
backend.build()
