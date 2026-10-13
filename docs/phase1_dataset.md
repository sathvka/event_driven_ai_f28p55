# Phase 1: Synthetic Dataset Generation

## 1. Purpose

The purpose of Phase 1 is to create a simulated dataset representing sensor measurements from an industrial electrical or motor system.

This dataset will be used to develop and test the event-encoding method before real hardware or physical sensor data are available.

## 2. Code File

`phase1_dataset.py`

## 3. Dataset Details

The script generates 5 seconds of simulated sensor data at a sampling frequency of 20 kHz.

- Sampling frequency: 20,000 samples per second
- Duration: 5 seconds
- Expected number of samples: 100,000
- Data type: Synthetic, generated using Python
- Output file: `phase1_dataset.csv`

## 4. Simulated Sensor Signals

The dataset contains the following signals:

| Signal | Description |
|---|---|
| `timestamp_s` | Time of each sample in seconds |
| `current_a` | Simulated phase A current |
| `current_b` | Simulated phase B current |
| `current_c` | Simulated phase C current |
| `dc_link_voltage` | Simulated DC-link voltage |
| `vibration` | Simulated mechanical vibration |
| `temperature` | Simulated temperature |
| `speed_rpm` | Simulated rotational speed |
| `position` | Estimated position |
| `fault` | Normal or fault indicator |
| `fault_type` | Type of simulated operating condition |

## 5. Simulated Fault Conditions

The script introduces four artificial conditions at different time intervals:

- **Bearing degradation (1.0–2.0 s):** An additional vibration component is introduced.
- **Arc event (2.2–2.25 s):** A short, high-frequency disturbance is added to phase A current.
- **Load step (3.0–3.5 s):** The phase currents are increased.
- **Sensor bias (4.0–4.5 s):** An offset is added to the DC-link voltage.

These are simulated examples, not experimentally measured faults.

## 6. Output

The script saves the generated measurements in `phase1_dataset.csv` and displays plots of selected sensor signals.

## 7. How to Run

Install the required Python libraries:

```bash
pip install numpy pandas matplotlib
```

Run the script:

```bash
python phase1_dataset.py
```

## 8. Current Limitations

- The data are synthetic and have not been validated against real equipment.
- The simulated fault patterns are simplified.
- The dataset is intended for early algorithm development, not real-world fault diagnosis.

## 9. Next Step

Use the generated dataset as input to Phase 2, where changes in a sensor signal are converted into events using a threshold-based event encoder.
