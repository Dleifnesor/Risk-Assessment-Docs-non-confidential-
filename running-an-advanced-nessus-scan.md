---
description: Following Host Discovery
---

# Running an Advanced Nessus Scan

## Information Needed

Clients are generally advised to create a temporary domain admin account in order to run a credentialed scan, this allows us to see more devices on a network, as well as see any group policy that would be a cause for concern.

***

## Creating an Advanced Scan

#### **1.** Navigate to and Create a new scan on the Nessus WebUI

![image](https://github.com/user-attachments/assets/3f00ccd1-5686-4518-907c-e85c91c61f18)

***

#### **2.** Select Advanced Scan on the Scan Templates page

![image](https://github.com/user-attachments/assets/d357b322-7cba-4749-a9e3-68f5ea9f930f)

***

#### **3.** Enter The IP targets

(Can be specific IPs and IP ranges notated in the X.X.X.X/CIDR format) ![image](https://github.com/user-attachments/assets/49adafb8-a3fe-4d6f-9487-9082f61f7c04)&#x20;

(you can also schedule a scan in the settings page of the Advanced scan) ![image](https://github.com/user-attachments/assets/1aec0162-ac19-4cb4-bb7b-96c9c8033661)

***

#### **4.** Configure which Ports/Services to scan

In the settings page

&#x20;![image](https://github.com/user-attachments/assets/ff488a42-c7b8-4138-8d48-7faca1bf95a7)&#x20;

(optional) you can also collect identity data from the network scan by using AD DC credentials ![image](https://github.com/user-attachments/assets/57002832-8cd9-4cf6-a907-32f39af4f1fa)

**Navigate to Assessment Tab**

&#x20;![image](https://github.com/user-attachments/assets/ed2c90c3-f343-448d-8aab-7a8d3a739ac2)&#x20;

**Enable web application scanning**

&#x20;![image](https://github.com/user-attachments/assets/763f9b6a-9d26-4c77-b34a-8afa406b99e5)&#x20;

**Enable scanning for malware**

&#x20;![image](https://github.com/user-attachments/assets/7d6c57d4-2029-46bd-a906-a6b02f5e307f)

**Navigate to Credentials Tab**

&#x20;![image](https://github.com/user-attachments/assets/f81c4986-6f1f-4c9a-8ec4-4a4b3cba75b4)

&#x20;If possible find and input the SSH credentials if known

&#x20;**DO NOT USE IF NETWORK VULNERABILITIES ARE UNKNOWN (password can be stolen if a compromised system with SSH enabled is on the same network)**

**Navigate to Windows Tab on Credentials** (Use with client permission as it is not required for a scan, however it can provide valuable information on the state of a clients DNS record and if their AD is susceptible to vulnerabilities that would otherwise be undetected by Nessus) ![image](https://github.com/user-attachments/assets/de3f50a1-d3c7-45e4-b5bf-d23e37ceaa3e)

***

#### **5.** Perform The Scan

Once the parameters are established, run the scan. This will take a lot longer than a Host Discovery scan.

&#x20;![image](https://github.com/user-attachments/assets/033b2ebc-c745-4e15-89ea-1dd7a4e086b6)&#x20;

(in this example only 2 systems were scanned however, in a real environment this will take hours, sometimes **Day(s)**

&#x20;

## Results

When the scan is complete, each host will have its own report, keep in mind that one errant host's vulnerability (like an AD) can cause all connected hosts to display a vulnerability that would otherwise not be present if that system were patched, It is very important that the Reports produced by Nessus are evaluated comprehensively.

![image](https://github.com/user-attachments/assets/4e20f223-82f8-48cc-b0af-12e6017e67f0)&#x20;

Each Hosts vulnerability will have an explanation by Nessus&#x20;

for what it is, what steps can be taken to remediate, and how it can be exploited.

***

In these examples, I purposefully used deprecated web applications out of their service life, real-world enterprises often also have unmaintained Webshells, Databases, and Domain Controls. While the amount of vulnerabilities will seem overwhelming, Tenable Nessus uses [Common Vulnerability Scoring System (CVSS) scores](understanding-cvss-scoring.md) (hopefully CVSSv3) to calculate the severity of the found vulnerabilities.  A score of 8 or higher usually means that these vulnerabilities should be taken seriously as they require less conditions to properly exploit by an attacker.
