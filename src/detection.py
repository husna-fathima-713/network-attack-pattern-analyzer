from collections import defaultdict


def detect_port_scan(features, threshold=10):
    scan_alerts = []
    ip_ports = defaultdict(set)

    for f in features:
        src = f.get("src_ip")
        dst_port = f.get("dst_port")

        if src and dst_port:
            ip_ports[src].add(dst_port)

    for ip, ports in ip_ports.items():
        if len(ports) > threshold:
            scan_alerts.append((ip, len(ports)))

    return scan_alerts


def detect_flood(features, threshold=100):
    flood_alerts = []
    ip_count = defaultdict(int)

    for f in features:
        src = f.get("src_ip")
        if src:
            ip_count[src] += 1

    for ip, count in ip_count.items():
        if count > threshold:
            flood_alerts.append((ip, count))

    return flood_alerts