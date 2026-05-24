import subprocess

from collections import Counter


def analyze_pcap(file_path):

    protocols = Counter()

    ip_addresses = Counter()

    dns_queries = []

    tcp_syn_packets = 0

    tcp_syn_ack_packets = 0

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
            "ip.dst",

            "-e",
            "dns.qry.name",

            "-e",
            "tcp.flags"
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

            dns_query = parts[3] if len(parts) > 3 else None

            tcp_flags = parts[4] if len(parts) > 4 else None

            # Protocol statistics
            protocols[protocol] += 1

            # IP tracking
            if src_ip:
                ip_addresses[src_ip] += 1

            if dst_ip:
                ip_addresses[dst_ip] += 1

            # DNS extraction
            if dns_query:
                dns_queries.append(dns_query)

            # TCP handshake analysis
            if tcp_flags:

                try:

                    flags = int(tcp_flags, 16)

                    SYN = 0x02
                    ACK = 0x10

                    is_syn = flags & SYN
                    is_ack = flags & ACK

                    if is_syn and not is_ack:

                        tcp_syn_packets += 1

                    if is_syn and is_ack:

                        tcp_syn_ack_packets += 1

                except:

                    pass

        # Potential issue detection
        potential_issues = []

        if protocols.get("ICMP", 0) > 20:

            potential_issues.append(
                "High ICMP activity detected"
            )

        failed_connections = (
            tcp_syn_packets - tcp_syn_ack_packets
        )

        if failed_connections > 5:

            potential_issues.append(
                "Possible failed TCP connections detected"
            )

        return {

            "packet_count": packet_count,

            "protocols": dict(protocols),

            "top_talkers": ip_addresses.most_common(5),

            "dns_queries": list(set(dns_queries))[:10],

            "tcp_analysis": {

                "syn_packets": tcp_syn_packets,

                "syn_ack_packets": tcp_syn_ack_packets,

                "possible_failed_connections": failed_connections
            },

            "potential_issues": potential_issues
        }

    except Exception as e:

        return {
            "error": str(e)
        }