import subprocess
from collections import Counter


def analyze_pcap(file_path):

    protocols = Counter()

    ip_addresses = Counter()

    packet_count = 0

    try:

        command = [
            "tshark",
            "-r",
            file_path,
            "-T",
            "fields",
            "-e",
            "_ws.col.Protocol",
            "-e",
            "ip.src",
            "-e",
            "ip.dst"
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True
        )

        output = result.stdout.splitlines()

        for line in output:

            packet_count += 1

            parts = line.split("\t")

            protocol = parts[0] if len(parts) > 0 else "UNKNOWN"

            src_ip = parts[1] if len(parts) > 1 else None

            dst_ip = parts[2] if len(parts) > 2 else None

            protocols[protocol] += 1

            if src_ip:
                ip_addresses[src_ip] += 1

            if dst_ip:
                ip_addresses[dst_ip] += 1

        return {

            "packet_count": packet_count,

            "protocols": dict(protocols),

            "top_talkers": ip_addresses.most_common(5)
        }

    except Exception as e:

        return {
            "error": str(e)
        }