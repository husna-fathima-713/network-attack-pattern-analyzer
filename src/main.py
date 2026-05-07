import sys
from capture import load_packets
from features import extract_features
from detection import detect_port_scan, detect_flood
from analyzer import log_results


def main():
    # Check CLI argument
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_pcap>")
        return

    pcap_file = sys.argv[1]

    packets = load_packets(pcap_file)

    if not packets:
        print("[INFO] No packets loaded.")
        return

    features = extract_features(packets)

    port_scans = detect_port_scan(features)
    floods = detect_flood(features)

    print("\n[DETECTION RESULTS]")

    if port_scans:
        print("Port Scan Detected:")
        for ip, count in port_scans:
            print(f" - {ip} scanned {count} ports")
    else:
        print("No Port Scan Detected")

    if floods:
        print("Flood Detected:")
        for ip, count in floods:
            print(f" - {ip} sent {count} packets")
    else:
        print("No Flood Detected")

    log_results(port_scans, floods)
    print("\n[INFO] Results saved to logs.txt")


if __name__ == "__main__":
    main()