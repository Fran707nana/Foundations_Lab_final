# TITAN SMALL BUSINESS SERVICES: SECURITY ARCHITECTURE DOCUMENT (SAD)
**Operator:** [Franklin G]
**Date:** [4-18-2026]

## 1. Perimeter Hardening (UFW & SSH)
* **SSH Status:** [Step 1-sudo nano /etc/ssh/sshd_congif, step 2-disabled PermitRootLogin no/PasswordAuthentication no, step 3-Sudo systemctl restart sshd]
* **Firewall Logic:** [sudo ufw default deny incoming,sudo ufw default allow outgoing,sudo ufw allow 22,sudo ufw allow 8080,sudo ufw enable,sudo ufw status]

## 2. The Automated Auditor (Python)
* **Script Logic:** [dc_ip = "Windows DC IP",
log_file = "/var/log/dc_audit.log"
response = os.system(f"ping -c 4 {dc_ip} > /dev/null 2>&1")
with open(log_file, "a") as f:
    if response == 0:
        f.write("DC is UP\n")
    else:
        f.write("DC is DOWN\n")
* **Telemetry Path:** `/var/log/sys_audit.log`

## 3. Containerized App (Docker)
* **Network Isolation:** [db container placed exclusively on internal backend network (internal: true), making it unreachable from the host. wiki and wordpress on frontend.]
* **Stack Health:** [
NAME                   IMAGE              COMMAND                  SERVICE     CREATED              STATUS              PORTS
vboxuser-db-1          mysql:5.7          "docker-entrypoint.s…"   db          12 days ago          Up 9 minutes        3306/tcp, 33060/tcp
vboxuser-wiki-1        nginx              "/docker-entrypoint.…"   wiki        About a minute ago   Up About a minute   0.0.0.0:8082->80/tcp, [::]:8082->80/tcp
vboxuser-wordpress-1   wordpress:latest   "docker-entrypoint.s…"   wordpress   12 days ago          Up 9 minutes        0.0.0.0:8081->80/tcp, [::]:8081->80/tcp]

## 4. Executive Summary
[I locked the front door of the server by running UFW to build a firewall that blocks all incoming traffic. Root log & and password ahthentications were disable, removing the risk of brute force attacks. A python scrip was created to monitor the windows DC by pinging it every time ir runs recording whether it is online or offline to a log file for review. The database container is deployed on a isolated internal network with no host access, meaning it can only be reached by authorized application containers and never directly from the internet. ]
