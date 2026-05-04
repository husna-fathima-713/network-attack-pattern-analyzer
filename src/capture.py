from scapy.all import rdpcap


def load_packets(file_path):
    try:
        packets = rdpcap(file_path)
        print(f"[INFO] Loaded {len(packets)} packets from {file_path}")
        return packets
    except Exception as e:
        print(f"[ERROR] Failed to load packets: {e}")
        return []