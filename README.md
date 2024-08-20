# Flower Federated Learning Server

This project runs a Flower Federated Learning server using the `FedAvg` strategy.

## Setup

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python3 server.py
   ```

## Requirements

- Python 3.7+
- flwr



## Set Up an AWS EC2 Instance

1. Use the SSH key pair to connect to your instance
```bash
   ssh -i your-key.pem ubuntu@your-ec2-public-ip
```
2. Update the Package List:
```bash
   sudo apt-get update
```
3. Install Python and Pip:
```bash
   sudo apt-get install python3 python3-pip
```
4. Install Flower and Other Required Packages:
```bash
   pip3 install flwr
```
5. Optionally, Set Up a Virtual Environment:
```bash
    sudo apt-get install python3-venv
    python3 -m venv venv
    source venv/bin/activate
    pip install flwr
```
6. Use the requirements.txt File
```bash
    pip install -r requirements.txt
```
7. Run the Flower Server on AWS
```bash
    python3 server.py
```
