import argparse
from scapy.all import sniff, IP

def packet_handler(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"[IP] {ip_layer.src} -> {ip_layer.dst} | Protocol: {ip_layer.proto}")
    else:
        print(packet.summary())

def main():
    parser = argparse.ArgumentParser(description="Simple Packet Sniffer with Scapy")
    parser.add_argument("-i", "--iface", help="Network interface to sniff on (default: auto)", default=None)
    parser.add_argument("-c", "--count", help="Number of packets to capture (default: 0 = infinite)", type=int, default=0)
    args = parser.parse_args()

    print("Starting packet sniffer....")
    sniff(iface=args.iface, prn=packet_handler, count=args.count)

if __name__ == "__main__":
    main()
