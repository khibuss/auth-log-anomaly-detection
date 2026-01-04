# auth-log-anomaly-detection
## Project Description

This project aims to develop a system capable of managing authentication logs in real time and automatically detecting anomalous behaviors potentially associated with malicious activities, such as brute force attacks or account compromise attempts.

The system simulates the operation of a large-scale service, characterized by a high number of authentication requests coming from different users and IP addresses.

Each login attempt generates a log event containing the following information:
- account name
- IP address
- authentication result (success or failure)
- event timestamp

---

## Objectives

The goal of this project is to leverage a **stream processing pipeline** to efficiently handle authentication logs, in particular to:

- collect and store logs in real time
- perform temporal aggregations on the data (e.g., count of failed login attempts per IP address or per account)
- detect anomalies based on rules and temporal thresholds
- notify anomalies via a monitoring system

---

## Considered Anomalies

The main anomalies detected by the system are:

- **Brute force from a single IP**  
  A high number of failed login attempts originating from the same IP address within a short time window.

- **Brute force on an account**  
  Repeated authentication failures associated with the same account (also from multiple IP addresses).

- **Suspicious login hours**  
  Successful logins occurring during unusual hours (e.g., between 00:00 and 06:00).

---

## Data Simulation

The project includes the development of a Python script to simulate the generation and sending of authentication logs.

The script allows reproducing:
- normal service operation
- controlled attack scenarios

This ensures that the entire processing pipeline can be properly tested.

---

## System Architecture

The system architecture consists of the following components:

- **Python**  
  Generates and simulates authentication logs.

- **Apache Kafka**  
  Collects and transports logs through a distributed messaging system.

- **Telegraf**  
  Consumes logs from Kafka topics and performs temporal aggregations on the data.

- **InfluxDB**  
  Time-series database used to store events and aggregated metrics.

- **Grafana**  
  Monitoring dashboard for visualizing metrics and generating alerts in case of anomalous behaviors.

