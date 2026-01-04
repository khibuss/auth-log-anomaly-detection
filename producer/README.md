# Auth Log Producer

This component simulates authentication logs and sends them to Kafka.

The producer is implemented in Python and is used to generate both:
- normal authentication traffic
- controlled attack scenarios (e.g. brute force attempts)

Each generated log contains:
- account name
- IP address
- authentication result (success / failure)
- timestamp

The producer is meant to be used only for testing and validation of the
stream processing and anomaly detection pipeline.