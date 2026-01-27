import time
import json
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

REGULAR_USERS_MAP = {
    "alice": "10.0.0.1",
    "bob": "10.0.0.2",
    "eric": "10.0.0.3",
    "john": "10.0.0.4",
    "mark": "10.0.0.5",
    "stephen": "10.0.0.6",
    "ted": "10.0.0.7",
    "mike": "10.0.0.8",
    "nade": "10.0.0.9",
    "lucas": "10.0.0.10",
    "anna": "10.0.0.11",
    "paul": "10.0.0.12",
    "charlie": "192.168.1.10",
    "emma": "192.168.1.11",
    "oliver": "192.168.1.12",
    "sophia": "192.168.1.13",
    "david": "172.16.0.5",
    "kevin": "172.16.0.6",
    "rachel": "172.16.0.7",
    "linda": "172.16.0.8"
}


def generate_regular_log():
    #Generate a single authentication log event
    user = random.choice(list(REGULAR_USERS_MAP.keys()))
    return {
        "user": user,
        "ip": REGULAR_USERS_MAP[user],
        "status": random.choices(
            ["success", "failed"],
            weights=[0.8, 0.2]   # mostly normal behavior
        )[0],
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

def send_logs(producer, topic):
    while True:
        log = generate_regular_log()
        producer.send(topic, value=log)
        producer.flush()

        print(f"Sent log: {log}")
        time.sleep(5)

if __name__ == "__main__":
    producer = KafkaProducer(
        bootstrap_servers="localhost:9093",
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

    try:
        send_logs(producer, "auth_logs")
    except KeyboardInterrupt:
        print("Stopping producer...")
    finally:
        producer.close()
