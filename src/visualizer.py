import matplotlib.pyplot as plt
from collections import defaultdict


def visualize_attacks(features):

    ip_count = defaultdict(int)

    for f in features:
        src = f.get("src_ip")

        if src:
            ip_count[src] += 1

    # Get top 5 IPs
    top_ips = sorted(
        ip_count.items(),
        key=lambda x: x[1],
        reverse=True
    )[:5]

    ips = [x[0] for x in top_ips]
    counts = [x[1] for x in top_ips]

    plt.figure(figsize=(10, 5))

    plt.bar(ips, counts)

    plt.xlabel("Source IP")
    plt.ylabel("Packet Count")
    plt.title("Top Suspicious IP Addresses")

    plt.xticks(rotation=15)

    plt.tight_layout()

    plt.savefig("../outputs/attack_visualization.png")

    print("[INFO] Visualization saved as attack_visualization.png")