import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PHASE 1 - DATASET CONSTRUCTION
# PC simulation of the future F28P55x sensor system
# ============================================================

# -----------------------------
# 1. Sampling configuration
# -----------------------------

fs = 20_000          # 20 kHz sampling rate
duration = 5         # 5 seconds

N = int(fs * duration)

time = np.arange(N) / fs

print("Sampling frequency:", fs, "Hz")
print("Total samples:", N)
print("Duration:", duration, "seconds")


# -----------------------------
# 2. Simulated motor speed
# -----------------------------

speed_rpm = 1500 + 20 * np.sin(2 * np.pi * 0.5 * time)

# This represents our future eQEP ground truth
position = np.cumsum(speed_rpm / 60 * 2 * np.pi / fs)


# -----------------------------
# 3. Three phase currents
# -----------------------------

electrical_frequency = 50

current_amplitude = 5

current_a = current_amplitude * np.sin(
    2 * np.pi * electrical_frequency * time
)

current_b = current_amplitude * np.sin(
    2 * np.pi * electrical_frequency * time
    - 2 * np.pi / 3
)

current_c = current_amplitude * np.sin(
    2 * np.pi * electrical_frequency * time
    + 2 * np.pi / 3
)


# -----------------------------
# 4. DC-link voltage
# -----------------------------

dc_link_voltage = (
    300
    + 5 * np.sin(2 * np.pi * 100 * time)
)


# -----------------------------
# 5. Vibration signal
# -----------------------------

vibration = (
    0.05 * np.sin(2 * np.pi * 120 * time)
)


# -----------------------------
# 6. Temperature signal
# -----------------------------

temperature = 35 + 0.5 * time


# -----------------------------
# 7. Add normal sensor noise
# -----------------------------

current_a += 0.05 * np.random.randn(N)
current_b += 0.05 * np.random.randn(N)
current_c += 0.05 * np.random.randn(N)

dc_link_voltage += 0.5 * np.random.randn(N)

vibration += 0.01 * np.random.randn(N)

temperature += 0.05 * np.random.randn(N)


# ============================================================
# FAULT INJECTION
# ============================================================

fault = np.zeros(N, dtype=int)
fault_type = np.array(["normal"] * N, dtype=object)


# -----------------------------
# 8. Bearing degradation
# -----------------------------

start = int(1.0 * fs)
end = int(2.0 * fs)

vibration[start:end] += (
    0.15 * np.sin(2 * np.pi * 300 * time[start:end])
)

fault[start:end] = 1
fault_type[start:end] = "bearing_degradation"


# -----------------------------
# 9. Arc event
# -----------------------------

start = int(2.2 * fs)
end = int(2.25 * fs)

current_a[start:end] += 3.0 * np.sin(
    2 * np.pi * 1000 * time[start:end]
)

fault[start:end] = 1
fault_type[start:end] = "arc_event"


# -----------------------------
# 10. Load step
# -----------------------------

start = int(3.0 * fs)
end = int(3.5 * fs)

current_a[start:end] *= 1.5
current_b[start:end] *= 1.5
current_c[start:end] *= 1.5

fault[start:end] = 1
fault_type[start:end] = "load_step"


# -----------------------------
# 11. Sensor bias
# -----------------------------

start = int(4.0 * fs)
end = int(4.5 * fs)

dc_link_voltage[start:end] += 15

fault[start:end] = 1
fault_type[start:end] = "sensor_bias"


# ============================================================
# 12. Create synchronized dataset
# ============================================================

dataset = pd.DataFrame({
    "timestamp_s": time,
    "current_a": current_a,
    "current_b": current_b,
    "current_c": current_c,
    "dc_link_voltage": dc_link_voltage,
    "vibration": vibration,
    "temperature": temperature,
    "speed_rpm": speed_rpm,
    "position": position,
    "fault": fault,
    "fault_type": fault_type
})


# -----------------------------
# 13. Save dataset
# -----------------------------

dataset.to_csv(
    "phase1_dataset.csv",
    index=False
)

print("\nDataset created successfully!")
print("Rows:", len(dataset))
print("Columns:", len(dataset.columns))

print("\nFault distribution:")
print(dataset["fault_type"].value_counts())


# ============================================================
# 14. Plot the signals
# ============================================================

plt.figure(figsize=(12, 5))

plt.plot(
    time,
    current_a,
    linewidth=0.5
)

plt.xlabel("Time (seconds)")
plt.ylabel("Current A")

plt.title("Phase A Current")

plt.show()


plt.figure(figsize=(12, 5))

plt.plot(
    time,
    vibration,
    linewidth=0.5
)

plt.xlabel("Time (seconds)")
plt.ylabel("Vibration")

plt.title("Vibration Signal")

plt.show()


plt.figure(figsize=(12, 5))

plt.plot(
    time,
    dc_link_voltage,
    linewidth=0.5
)

plt.xlabel("Time (seconds)")
plt.ylabel("Voltage (V)")

plt.title("DC-Link Voltage")

plt.show()