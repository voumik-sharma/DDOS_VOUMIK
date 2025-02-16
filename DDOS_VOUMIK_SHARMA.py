
import requests
import threading
import time

# Logo and credits
def display_logo():
    print("""

___________________________
[___VOUMIk SHARMA™____]

    Script by: VOUMIK SHARMA
    """)

# Authorization function
def authorize():
    valid_username = "VOUMIK"  # Set your username here
    valid_password = "VOUMIK SHARMA"  # Set your password here

    print("Authentication required.")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username == valid_username and password == valid_passwor>
        print("Access granted. Proceeding...\n")
        return True
    else:
                print("Access denied. Invalid credentials.\n")
        return False

# Function to perform GET requests
def perform_request(url, thread_id):
    try:
        response = requests.get(url, timeout=5)
        print(f"[Thread-{thread_id}] Status Code: {response.sta>
    except requests.exceptions.RequestException as e:
        print(f"[Thread-{thread_id}] Error: {e}")

# Function to initiate load test
def load_test(url, num_threads):
    threads = []
    print(f"Starting load test on: {url} with {num_threads} thr>
    start_time = time.time()

    for i in range(num_threads):
        thread = threading.Thread(target=perform_request, args=>
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Load test completed in {end_time - start_time:.2f} >
    

# Main function
if __name__ == "__main__":
    display_logo()

    # Check for valid credentials
    if not authorize():
        exit(1)  # Exit if authentication fails

    # Get target URL and number of threads
    target_url = input("Enter the URL to test: ").strip()
    num_threads = int(input("Enter the number of threads to sim>

    if target_url:
        load_test(target_url, num_threads)
    else:
        print("Please ent