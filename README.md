
# Packet Sniffer

A simple packet sniffer built with Python and [Scapy](https://scapy.net/).

## Description
This project is a basic tool for capturing and analyzing network packets.  
The sniffer displays packet information in real time and can be extended with filtering, interface selection, and saving packets to a file for further analysis.

## Features
- Capture packets from a network interface
- Display IP source, destination, and protocol
- Basic output for non-IP packets
- Interface selection with command-line arguments
- Limit number of packets with command-line arguments
- Filtering support (planned)
- Save captured packets to `.pcap` files (planned)

## Requirements
- Python 3.7+
- Scapy

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your_username>/packet-sniffer.git
   cd packet-sniffer
````

2. Install dependencies:

   ```bash
   pip install scapy
   ```

## Usage

Run the sniffer with administrator privileges (required for accessing the network interface).

### Capture packets on the default interface, unlimited:

```bash
sudo python3 sniffer.py
```

### Capture 20 packets on a specific interface (e.g., `en0` on macOS):

```bash
sudo python3 sniffer.py -i en0 -c 20
```

### Capture 50 packets on Linux Wi-Fi interface (`wlan0`):

```bash
sudo python3 sniffer.py -i wlan0 -c 50
```

## Project Structure

```
packet-sniffer/
├── README.md       # Documentation
├── .gitignore      # Ignored files
└── sniffer.py      # Main sniffer code
```

## Roadmap

* Add packet filters (TCP/UDP/HTTP, etc.)
* Save captured packets to `.pcap`
* Show more detailed packet information
* Add colored output for readability

## Disclaimer

This project is created for **educational and research purposes only**.
