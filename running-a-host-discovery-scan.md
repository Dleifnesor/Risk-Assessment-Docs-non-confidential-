---
description: For finding all (online and connected) devices on a network
---

# Running a Host Discovery Scan

## Getting Started

(assuming you have up to date info on the network you are going to scan)

***

First, understand the structure of the network you want to scan

_For example:_

![image](https://github.com/user-attachments/assets/ddb0b5ba-559c-484b-830d-b7c76a47dd87)

this diagram shows the subnets of a LAN, including VLANs and their respective IP ranges

Any kind of documentation showing which IP address ranges are in use and their respective use cases (infrastructure, Databases, Local Services) can prove useful in assessing which vulnerabilities are most critical to an organizations security.

### Running a Basic Host Discovery Scan

(assuming you already have installed Nessus and assigned a license, If not refer to \[insert link here])

**1.** Go to **My Scans**, Then go to **New Scan**

&#x20;![image](https://github.com/user-attachments/assets/8e1707d4-fcf8-485d-9919-fafbf24406c4)

**2.** In Scan Templates, Run the **Host Discovery** Scan

&#x20;![image](https://github.com/user-attachments/assets/b2bd60c0-85ae-4fb0-9527-a7c2a26ced87)

**3.** On the Host Discovery Scan page, Name the scan, put a description and target folder to save the scan, Enter any target IPs and their subnet masks, and **Hit Save** ![image](https://github.com/user-attachments/assets/5585e655-7fb4-4257-b194-12bd41ddfaa2)

**4.** You now have the scan and the respective targets saved, (alternatively you can just run the scan without having to target a specific IP range, but this makes the scan run faster if Nessus knows what IP ranges to target.)

Make sure the box running Nessus is connected to a point in the network that can access **all, if not most** points on the network (like a trunk port on a main switch) Then run **Scan** ![image](https://github.com/user-attachments/assets/6f470be1-7440-4977-9b7b-d3bcf8226ed9)

## Results

Click on the scan that was completed once finished

![image](https://github.com/user-attachments/assets/2dbd9b58-1abb-4a26-ab68-0d5e86fa2323)

This is what the results of the scan should look like:

&#x20;![image](https://github.com/user-attachments/assets/b109ef9e-2828-4ba4-86f3-7ac40c5c7ee4)
