# Telegraf Configuration

This folder contains the `telegraf.conf` file used to collect authentication logs from Kafka and send them to InfluxDB.

## Example Flux Query
Use this query in the InfluxDB UI to pivot and display the logs in a table with only the important fields:

```bash
from(bucket: "system_logs")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "kafka_consumer")
  |> pivot(
      rowKey:["_time"],
      columnKey: ["_field"],
      valueColumn: "_value"
    )
  |> keep(columns: ["_time", "user", "ip", "status"])
  |> sort(columns: ["_time"], desc: true)

```
