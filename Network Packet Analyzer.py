from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        payload = packet[Raw].load if packet.haslayer(Raw) else None

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")
        print(f"Protocol: {protocol}")
        if payload:
            print(f"Payload: {payload.hex()}")

sniff(filter="ip", prn=packet_handler)
