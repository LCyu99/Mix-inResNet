# Pytorch-orthopedics

practice on orthopedics using pytorch

## Requirements

This is my experiment eviroument
- python3.6
- pytorch1.6.0+cu101
- tensorboard 2.2.2(optional)


## Usage

### 1. enter directory
```bash
$ cd pytorch-orthopedics
```

### 2. dataset
I will use orthopedics dataset from torchvision since it's more convenient, but I also
kept the sample code for writing your own dataset module in dataset folder, as an
example for people don't know how to write it.

### 3. run tensorbard(optional)
Install tensorboard
```bash
$ pip install tensorboard
$ mkdir runs
Run tensorboard
$ tensorboard --logdir='runs' --port=6006 --host='localhost'
```

### 4. train the model
You need to specify the net you want to train using arg -net

```bash
# use gpu to train vgg16
$ python train.py -net vgg16 -gpu
```



