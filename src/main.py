from capture import load_packets
from features import extract_features
from detection import detect_port_scan, detect_flood

PCAP_FILE = "../data/sample.pcap"

def main():
    packets = load_packets(PCAP_FILE)

    if not packets:
        print("[INFO] No packets loaded.")
        return

    features = extract_features(packets)

    # Detection
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


if __name__ == "__main__":
    main()