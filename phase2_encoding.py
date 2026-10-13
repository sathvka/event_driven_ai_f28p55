import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# PHASE 2 - EVENT / SPIKE ENCODING
# Step 1: Fixed-threshold encoding
# ============================================================


# ------------------------------------------------------------
# 1. Load Phase 1 dataset
# ------------------------------------------------------------

dataset = pd.read_csv("phase1_dataset.csv")

time = dataset["timestamp_s"].to_numpy()
signal = dataset["vibration"].to_numpy()

fs = 20_000


print("Dataset loaded")
print("Number of samples:", len(signal))
print("Sampling frequency:", fs, "Hz")


# ------------------------------------------------------------
# 2. Calculate sample-to-sample change
# ------------------------------------------------------------

change = np.abs(np.diff(signal))


# ------------------------------------------------------------
# 3. Fixed threshold
# ------------------------------------------------------------

threshold = 0.05

events = change > threshold


# ------------------------------------------------------------
# 4. Calculate event statistics
# ------------------------------------------------------------

total_events = np.sum(events)

duration = time[-1] - time[0]

events_per_second = total_events / duration

event_percentage = (
    total_events / len(signal)
) * 100


print("\n--- Event Statistics ---")

print("Threshold:", threshold)

print("Total events:", total_events)

print("Events per second:",
      events_per_second)

print("Event percentage:",
      event_percentage, "%")


# ------------------------------------------------------------
# 5. Plot original vibration signal
# ------------------------------------------------------------

plt.figure(figsize=(12, 5))

plt.plot(time, signal)

plt.xlabel("Time (seconds)")
plt.ylabel("Vibration")

plt.title("Original Vibration Signal")

plt.show()


# ------------------------------------------------------------
# 6. Plot event stream
# ------------------------------------------------------------

plt.figure(figsize=(12, 4))

plt.plot(
    time[1:],
    events.astype(int),
    "."
)

plt.xlabel("Time (seconds)")
plt.ylabel("Event")

plt.title("Fixed-Threshold Event Stream")

plt.yticks([0, 1], ["No Event", "Event"])

plt.show()
# ============================================================
# THRESHOLD EXPERIMENT
# ============================================================

thresholds = [0.01, 0.02, 0.05, 0.10, 0.20]

print("\n--- Threshold Sweep ---")

for threshold in thresholds:

    events = change > threshold

    total_events = np.sum(events)

    events_per_second = total_events / duration

    event_percentage = (
        total_events / len(signal)
    ) * 100

    print(
        "Threshold:", threshold,
        "| Events:", total_events,
        "| Events/sec:", events_per_second,
        "| Event %:", event_percentage
    )
    thresholds = [0.01, 0.02, 0.05, 0.10, 0.20]

print("\n--- Threshold Sweep ---")

for threshold in thresholds:

    events = change > threshold

    total_events = np.sum(events)

    events_per_second = total_events / duration

    event_percentage = (
        total_events / len(signal)
    ) * 100

    print(
        "Threshold:", threshold,
        "| Events:", total_events,
        "| Events/sec:", events_per_second,
        "| Event %:", event_percentage
    )
    # ============================================================
# Bearing fault event analysis
# ============================================================

threshold = 0.05

events = change > threshold

fault_mask = (
    (time[1:] >= 1.0) &
    (time[1:] < 2.0)
)

normal_mask = ~fault_mask

fault_events = np.sum(events[fault_mask])
normal_events = np.sum(events[normal_mask])

fault_duration = 1.0
normal_duration = duration - fault_duration

fault_events_per_second = fault_events / fault_duration
normal_events_per_second = normal_events / normal_duration

print("\n--- Bearing Fault Analysis ---")

print("Events during bearing fault:",
      fault_events)

print("Events/sec during bearing fault:",
      fault_events_per_second)

print("Events during normal periods:",
      normal_events)

print("Events/sec during normal periods:",
      normal_events_per_second)
# ============================================================
# Compare normal operation with bearing fault
# ============================================================

threshold = 0.05

events = change > threshold

# Bearing fault: 1.0 to 2.0 seconds
fault_mask = (
    (time[1:] >= 1.0) &
    (time[1:] < 2.0)
)

normal_mask = ~fault_mask

fault_events = np.sum(events[fault_mask])
normal_events = np.sum(events[normal_mask])

print("\n--- Fault vs Normal ---")

print("Events during bearing fault:", fault_events)
print("Events during normal operation:", normal_events)
