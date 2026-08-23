import numpy as np
import matplotlib.pyplot as plt

# 1. Create a time axis
t = np.linspace(0, 10, 1000)

# 2. Create a simple signal
signal = np.sin(t)

# 3. Add a sudden change to simulate an event
signal[500:550] += 2

# 4. Set the event threshold
threshold = 0.2

# 5. Calculate change between consecutive samples
change = np.abs(np.diff(signal))

# 6. Generate an event when the change exceeds threshold
events = change > threshold

print("Total samples:", len(signal))
print("Total events:", np.sum(events))
# Plot the signal
plt.figure(figsize=(12, 5))

plt.plot(signal, label="Signal")

# Find where events occurred
event_indices = np.where(events)[0]

# Mark the events
plt.scatter(
    event_indices,
    signal[event_indices],
    color="red",
    label="Events"
)

plt.xlabel("Sample")
plt.ylabel("Signal value")
plt.title("Basic Event Encoding")
plt.legend()
plt.show()
