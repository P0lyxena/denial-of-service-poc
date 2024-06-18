# DoS Proof of Concept Testing Script

## Purpose
This script is designed to test the effectiveness of a Denial of Service (DoS) attack in a controlled manner. It performs three types of tests:
1. HTTP Request 
2. Ping 
3. HTTP Client Request 

The script logs response times for each request and ping, and at the end, it analyzes and compares the average response times to detect any significant differences.

## Features
- Multi-threaded execution to simulate concurrent requests
- Detailed logging to both console and a log file (`dos_test.log`)
- Command-line inputs for customizable test parameters
- Response time analysis including average, maximum, minimum, and standard deviation

## Prerequisites
- Python 3.x
- `requests` library (install using `pip install requests`)
- `statistics` module (part of the Python standard library)

## Usage

### Command-Line Arguments
The script accepts the following command-line arguments:
- `--hostname`: Target hostname (e.g., `example.com`) [Required]
- `--http_url`: Target HTTP URL (e.g., `http://example.com`) [Required]
- `--number_of_requests`: Number of HTTP requests (default: 100) [Optional]
- `--delay_between_requests`: Delay between HTTP requests in seconds (default: 0.1) [Optional]
- `--number_of_pings`: Number of pings (default: 50) [Optional]
- `--delay_between_pings`: Delay between pings in seconds (default: 1) [Optional]

### Running the Script
1. **Clone or Download the Script**: Save the script as `main.py` or another unique name.
2. **Install Dependencies**: Ensure you have the `requests` library installed.
   ```sh
   pip install requests
   ```
3. **Run the Script**: Execute the script from the command line with the appropriate arguments.
   ```sh
   python main.py --hostname example.com --http_url http://example.com --number_of_requests 100 --delay_between_requests 0.1 --number_of_pings 50 --delay_between_pings 1
   ```

### Example Command
```sh
python main.py --hostname example.com --http_url http://example.com --number_of_requests 100 --delay_between_requests 0.1 --number_of_pings 50 --delay_between_pings 1
```

### Log Output
- **Console Output**: The script logs progress and results to the console.
- **Log File**: Detailed logs are also saved to `dos_test.log`.

### Analyzing Results
At the end of the script execution, it performs an analysis of the recorded response times and logs the following statistics:
- Average Response Time
- Maximum Response Time
- Minimum Response Time
- Standard Deviation (if more than one data point is available)

### Example Log Entries
```
2024-06-19 12:00:00 - INFO - Starting HTTP requests ...
2024-06-19 12:00:00 - INFO - HTTP Request 1: Status Code 200, Response Time: 0.1234 seconds
2024-06-19 12:00:01 - INFO - HTTP Request 2: Status Code 200, Response Time: 0.1156 seconds
...
2024-06-19 02:09:35 - INFO - HTTP requests  completed.
...
2024-06-19 02:09:35 - INFO - Analyzing response times...
2024-06-19 02:09:35 - INFO - HTTP Requests - Average Response Time: 0.2433 seconds, Max Time: 0.2715 seconds, Min Time: 0.2158 seconds, Std Dev: 0.0144 seconds
2024-06-19 02:09:35 - INFO - Ping Requests - Average Response Time: 0.0201 seconds, Max Time: 0.0330 seconds, Min Time: 0.0100 seconds, Std Dev: 0.0065 seconds
2024-06-19 02:09:35 - INFO - HTTP Client Requests - Average Response Time: 0.2615 seconds, Max Time: 0.2615 seconds, Min Time: 0.2615 seconds
```

## Important Considerations
- **Permissions**: Ensure you have explicit permission from the server owner or the bug bounty program to perform these tests.
- **Rate Limiting**: The script includes delays between requests to minimize the impact on the target server.
- **Ethical Guidelines**: Always follow legal and ethical guidelines when performing security testing.

## Disclaimer
This script is for educational and testing purposes only. Use it responsibly and only on systems where you have explicit permission to perform such tests. Misuse of this script can cause damage and may be illegal.
