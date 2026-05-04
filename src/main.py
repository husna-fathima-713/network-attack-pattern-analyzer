from capture import load_packets

PCAP_FILE = "../data/sample.pcap"

def main():
    packets = load_packets(PCAP_FILE)
    
    if not packets:
        print("[INFO] No packets loaded.")
        return
    
    print("[INFO] Packet capture module working.")


if __name__ == "__main__":
    main()