# NS-3 Simulator for SRNIC (NSDI'23)
This is the simulation code for NSDI'23 paper:
- [SRNIC: A Scalable Architecture for RDMA NICs](https://cse.hkust.edu.hk/~kaichen/papers/srnic-nsdi23.pdf). 


This repository is developed based on [HPCC simulation code](https://github.com/alibaba-edu/High-Precision-Congestion-Control) (base repo). The original HPCC ns3 code is lossless. We integrate an **[IRN-like](https://people.eecs.berkeley.edu/~radhika/irn.pdf) selective retransmission** into this code. In addition, we add a timeout checking to retransmit a long-term non-acked packet to handle the last packet loss event.

**Note:** We didn't simulate the SRNIC's SW-HW co-design architecture here; we evaluate it in testbed experiments.

# Quick Start
You can write your experiment setting in `run.sh`, and use `myrun.py` to simultaneously start them. It is `run.py` that physically compiles and runs this repo. 
```
$ cd simulation
$ python myrun.py
```

# Modifications
## simulation
The modified src code files compared with the base repo mainly consist of below:
* simulation/src/point-to-point/rdma-queue-pair.cc
* simulation/src/point-to-point/switch-node.cc
* simulation/src/point-to-point/switch-mmu.cc
* simulation/src/point-to-point/rdma-hw.cc
* simulation/src/point-to-point/qbb-net-device.cc
## analysis
You can use the `fct_analysis.py` to analyze the result files in `simulation/mix`.
## traffic_gen 
You can use `gene.sh` to generate workload files for specific topology and traffic distribution. We have provided the CacheFollower distribution.