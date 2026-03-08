# sample-data

login_logs = [
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
    {"ip": "192.168.1.15", "user": "root", "status": "failed"},
    {"ip": "172.16.0.5", "user": "ubuntu", "status": "success"},
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "admin", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"}
]

# Step 2
def block_ip(ip_address):
    firewall = 1
    while firewall <= 3:
        print(f"Blocking {ip_address} on Firewall {firewall}...")
        firewall += 1


# Step 3
def analyze_logs(logs):

    failed_counts = {}

    # Step 4
    for log in logs:

        if log["status"] == "failed":

            ip = log["ip"]

            if ip in failed_counts:
                failed_counts[ip] += 1
            else:
                failed_counts[ip] = 1

    banned_ips = []

    # Step 5
    for ip, count in failed_counts.items():

        if count >= 3:
            banned_ips.append(ip)
            block_ip(ip)

    return banned_ips


# Step 6
analyze_logs(login_logs)