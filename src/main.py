import sys

from capture import load_packets
from features import extract_features
from detection import (
    detect_port_scan,
    detect_flood,
    detect_syn_flood
)
from analyzer import log_results


def main():

    # CLI argument check
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pcap>")
        return

    pcap_file = sys.argv[1]

    # Load packets
    packets = load_packets(pcap_file)

    if not packets:
        print("[INFO] No packets loaded.")
        return

    # Extract features
    features = extract_features(packets)

    # Run detections
    port_scans = detect_port_scan(features)
    floods = detect_flood(features)
    syn_floods = detect_syn_flood(features)

    print("\n[DETECTION RESULTS]\n")

    # Port Scan
    if port_scans:
        print("Port Scan Detected:")

        for ip, count in port_scans:
            print(f" - {ip} scanned {count} ports")

    else:
        print("No Port Scan Detected")

    print()

    # Flood Detection
    if floods:
        print("Flood Detected:")

        for ip, count in floods:
            print(f" - {ip} sent {count} packets")

    else:
        print("No Flood Detected")

    print()

    # SYN Flood Detection
    if syn_floods:
        print("SYN Flood Detected:")

        for ip, count in syn_floods:
            print(f" - {ip} sent {count} SYN packets")

    else:
        print("No SYN Flood Detected")

    # Save logs
    log_results(port_scans, floods, syn_floods)

    print("\n[INFO] Results saved to logs.txt")


if __name__ == "__main__":
    main()