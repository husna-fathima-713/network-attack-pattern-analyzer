from scapy.layers.inet import IP, TCP, UDP


def extract_features(packets):
    features = []

    for pkt in packets:
        if IP in pkt:
            ip_layer = pkt[IP]

            feature = {
                "src_ip": ip_layer.src,
                "dst_ip": ip_layer.dst,
                "protocol": ip_layer.proto,
                "packet_size": len(pkt)
            }

            # Add port info if available
            if TCP in pkt:
                feature["src_port"] = pkt[TCP].sport
                feature["dst_port"] = pkt[TCP].dport
                feature["flags"] = str(pkt[TCP].flags)

            elif UDP in pkt:
                feature["src_port"] = pkt[UDP].sport
                feature["dst_port"] = pkt[UDP].dport

            features.append(feature)

    print(f"[INFO] Extracted features from {len(features)} packets")
    return features