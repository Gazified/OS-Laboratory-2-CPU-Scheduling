# Optional: draws Gantt charts for all five algorithms -> gantt_charts.png
# Install first (once):  pip install matplotlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from cpu_scheduling import PROCESSES, SRTF_PROCESSES, fcfs, non_preemptive, round_robin, srtf

runs = [
    ("FCFS", fcfs(PROCESSES)[1]),
    ("Non-preemptive SJF", non_preemptive(PROCESSES, "sjf")[1]),
    ("Non-preemptive Priority", non_preemptive(PROCESSES, "priority")[1]),
    ("Round Robin (q = 2)", round_robin(PROCESSES, quantum=2)[1]),
    ("SRTF (separate dataset)", srtf(SRTF_PROCESSES)[1]),
]
colors = {"P1": "#4C78A8", "P2": "#F58518", "P3": "#54A24B", "P4": "#B279A2"}

fig, axes = plt.subplots(len(runs), 1, figsize=(11, 2.0 * len(runs)))
for ax, (title, gantt) in zip(axes, runs):
    for start, end, pid in gantt:
        ax.barh(0, end - start, left=start, color=colors[pid], edgecolor="white", height=0.6)
        ax.text((start + end) / 2, 0, pid, ha="center", va="center", color="white", fontsize=9, fontweight="bold")
    ticks = sorted({s for s, _, _ in gantt} | {e for _, e, _ in gantt})
    ax.set_xticks(ticks)
    ax.set_yticks([])
    ax.set_xlim(0, ticks[-1])
    ax.set_title(title, loc="left", fontsize=10)
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
axes[-1].set_xlabel("Time (ms)")
plt.tight_layout()
plt.savefig("gantt_charts.png", dpi=160)
print("Saved gantt_charts.png")