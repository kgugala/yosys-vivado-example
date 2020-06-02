# Simple Yosys -> Vivado example (with Edalize)

## Prepare the environment


### Install prerequisites

```
sudo pip install virtualenv
```

Install Yosys following the guide from https://github.com/YosysHQ/yosys#setup
Install Vivado following the guide from https://www.xilinx.com/products/design-tools/vivado.html

### Prepare env

```
virtualenv env
source env/bin/activate
pip install edalize
```

### Build the example

```
git clone https://gitub.com/kgugala/yosys-vivado-example
cd yosys-vivado-example
python3 yosys-vivado.py
```

The above instructions assume both Vivado and Yosys are installed and in the PATH. 
