# OS-Laboratory-2-CPU-Scheduling

Operating Systems Lab 2 - CPU Scheduling Algorithms

## Run

```bash
./.venv/bin/python cpu_scheduling_experiment.py
```

The shared dataset below is used for FCFS, non-preemptive SJF, non-preemptive
Priority, and Round Robin (quantum = 2):

| Process | Arrival time | Burst time | Priority |
|---|---:|---:|---:|
| P1 | 0 | 7 | 3 |
| P2 | 0 | 4 | 1 |
| P3 | 0 | 1 | 4 |
| P4 | 0 | 5 | 2 |

SRTF intentionally uses its own dataset with staggered arrival times so its
preemptive behavior can be observed independently.

## Results

| Algorithm | Average WT | Average TAT | Average RT |
|---|---:|---:|---:|
| FCFS | 7.50 | 11.75 | 7.50 |
| SJF | 4.00 | 8.25 | 4.00 |
| Priority | 7.25 | 11.50 | 7.25 |
| Round Robin | 8.00 | 12.25 | 2.75 |
| SRTF (separate dataset) | 2.75 | 6.50 | 0.25 |
