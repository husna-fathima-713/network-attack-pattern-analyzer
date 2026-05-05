from capture import load_packets
from features import extract_features

PCAP_FILE = "../data/sample.pcap"

def main():
    packets = load_packets(PCAP_FILE)

    if not packets:
        print("[INFO] No packets loaded.")
        return

    features = extract_features(packets)

    print("[INFO] Feature extraction working.")
    print("Sample Feature:", features[0])


if __name__ == "__main__":
    main()