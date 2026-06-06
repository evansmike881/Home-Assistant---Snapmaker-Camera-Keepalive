#!/usr/bin/env python3
import json
import time
from websocket import create_connection

with open("/data/options.json", "r") as f:
    options = json.load(f)

IP = options["printer_ip"]
TOKEN = options["token"]

while True:
    try:
        ws = create_connection(f"ws://{IP}/websocket?token={TOKEN}", timeout=5)
        ws.send(json.dumps({
            "id": 1,
            "jsonrpc": "2.0",
            "method": "camera.start_monitor",
            "params": {
                "domain": "lan",
                "interval": 0
            }
        }))
        ws.close()
        print(f"[{time.strftime('%H:%M:%S')}] OK", flush=True)
    except Exception as e:
        print(f"Error: {e}", flush=True)

    time.sleep(10)