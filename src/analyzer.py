from datetime import datetime

LOG_FILE = "../outputs/logs.txt"


def log_results(port_scans, floods, syn_floods):
    with open(LOG_FILE, "a") as f:

        f.write("\n===== Analysis Report =====\n")
        f.write(f"Time: {datetime.now()}\n\n")

        # Port Scan
        if port_scans:
            f.write("Port Scan Detected:\n")

            for ip, count in port_scans:
                f.write(f" - {ip} scanned {count} ports\n")

        else:
            f.write("No Port Scan Detected\n")

        f.write("\n")

        # Flood Detection
        if floods:
            f.write("Flood Detected:\n")

            for ip, count in floods:
                f.write(f" - {ip} sent {count} packets\n")

        else:
            f.write("No Flood Detected\n")

        f.write("\n")

        # SYN Flood Detection
        if syn_floods:
            f.write("SYN Flood Detected:\n")

            for ip, count in syn_floods:
                f.write(f" - {ip} sent {count} SYN packets\n")

        else:
            f.write("No SYN Flood Detected\n")

        f.write("\n===========================\n")