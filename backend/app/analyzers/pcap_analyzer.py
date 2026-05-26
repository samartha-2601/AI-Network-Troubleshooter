import subprocess

from collections import Counter


def analyze_pcap(file_path):

    protocols = Counter()

    ip_addresses = Counter()

    dns_queries = []

    tcp_syn_packets = 0

    tcp_syn_ack_packets = 0

    packet_count = 0

    # New Intelligence Features
    top_ports = Counter()

    tls_versions = Counter()

    http_hosts = set()

    user_agents = set()

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
            "tcp.flags",

            "-e",
            "tcp.dstport",

            "-e",
            "tls.record.version",

            "-e",
            "http.host",

            "-e",
            "http.user_agent"
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

            dst_port = parts[5] if len(parts) > 5 else None

            tls_version = parts[6] if len(parts) > 6 else None

            http_host = parts[7] if len(parts) > 7 else None

            user_agent = parts[8] if len(parts) > 8 else None

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

            # Port Analysis
            if dst_port:
                top_ports[dst_port] += 1

            # TLS Analysis
            if tls_version:

                versions = tls_version.split(",")

                for version in versions:

                    version = version.strip()

                    if version:

                        tls_versions[version] += 1

            # HTTP Hosts
            if http_host:
                http_hosts.add(http_host)

            # User Agents
            if user_agent:
                user_agents.add(user_agent)

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

        # Port Scan Detection
        if len(top_ports) > 20:

            potential_issues.append(
                "Possible port scanning activity detected"
            )

        def normalize_tls_versions(tls_versions):

            normalized = Counter()

            version_map = {

                "0x0301": "TLS 1.0",
                "0x0302": "TLS 1.1",
                "0x0303": "TLS 1.2",
                "0x0304": "TLS 1.3"
            }

            for version, count in tls_versions.items():

                normalized_name = version_map.get(
                    version,
                    version
                )

                normalized[normalized_name] += count

            return dict(normalized)

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

            # NEW FEATURES

            "top_ports": top_ports.most_common(10),

            "tls_versions": normalize_tls_versions(tls_versions),

            "http_hosts": list(http_hosts)[:20],

            "user_agents": list(user_agents)[:20],

            "potential_issues": potential_issues
        }

    except Exception as e:

        return {
            "error": str(e)
        }