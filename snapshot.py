#!/usr/bin/env python
import json
import psutil
import time
from datetime import datetime


class config:
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)
    output = (data['output'])
    interval = int(data['interval']) * 60  # since method time.sleep() use secs instead of minute


class psstats:
    def cpu(self):
        return psutil.cpu_percent(interval=1)

    def disk(self):
        return psutil.disk_usage('/')

    def vm(self):
        return psutil.virtual_memory()

    def io(self):
        return psutil.net_io_counters()


def output():
    i = 0
    j = 1
    p = psstats()
    if config.output == "txt":
        while True:
            now = datetime.now()
            current = now.strftime("%d/%m/%Y %H:%M:%S")
            f = open("data.txt", "a+")
            f.write("SNAPSHOT %d" % (i + 1))
            f.write(": TIMESTAMP: %s\r\n" % current)
            f.write("cpu: %s\n" % str(p.cpu()))
            f.write("disk: %s\n" % str(p.disk().percent))
            f.write("memory: %s\n" % str(p.vm().percent))
            f.write("network: %s\n" % str(p.io().packets_sent))
            time.sleep(config.interval)

    elif config.output == "json":
        data = {}
        data["SNAPSHOTS"] = []
        while True:
            now = datetime.now()
            current = now.strftime("%d/%m/%Y %H:%M:%S")
            data["SNAPSHOTS"].append({
                "SNAPSHOT": j,
                "TIMESTAMP": current,
                "cpu": str(p.cpu()),
                "disk": str(p.disk().percent),
                "memory": str(p.vm().percent),
                "network": str(p.io().packets_sent)
            })
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile, indent=True)
            j += 1
            time.sleep(config.interval)

    else:
        print("Invalid output type")


if __name__ == "__main__":
    output()
