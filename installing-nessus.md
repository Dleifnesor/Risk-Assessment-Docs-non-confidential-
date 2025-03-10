# Installing Nessus

## Nessus-Vulnerability-Scanner

How to Install Nessus and Run Vulnerability Scans

![Tenable-Logo2021-Reversed](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/b2c48121-85a4-41f0-9fdd-6baac4a14775)

## Overview

Nessus is a tool developed by Tenable that scans for security vulnerabilites that can be found in devices, operating systems, clound-based services, applications and other network-related components. Nessus conducts vurnerability assessments that aid endpoint users in hardening security infranstructures by identify system flaws, missing patches, malware and misconfigurations, etc..

```
This README.md will give a general overview of Teanable Nessus.
```

## Registration

We will be using Nessus Essential because it is Tenable's free vulnerability assessment solution. After pressing "Get Started" to register, an activation code will be sent to the submitted email.

The next page will prompt to press the download button to enter the Download page.

```
https://www.tenable.com/products/nessus/nessus-essentials
```

![Screenshot 2023-11-11 at 8 36 04 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/4b5a0917-4013-457f-b809-5b0447be4a01) ![Screenshot 2023-11-11 at 8 51 36 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/dd391e47-99ff-4cc5-a24d-8df32eb1cafd)

## Download and installation

Select your version and platform/flavor of Nessus to download and install.

![Screenshot 2023-11-11 at 8 52 19 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/853aaf91-434f-4810-895e-da31707d4e53)

## Connect to server

1.) After installation, the browser will open up a localhost SSL server page that uses port 8834.

```
-Note: It is a good idea to bookmark or save the address in a safe place because it is easy to forgot.
```

![Screenshot 2023-11-11 at 8 54 55 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/6d510552-5487-46fb-94f5-886899416056)

2.) Connect via SSL and the service will start to initialize.

![Screenshot 2023-11-11 at 8 55 26 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/ed3f7914-3765-4740-bbb4-021bcb66210a)

3.) Select "Nessus Essentials"

![Screenshot 2023-11-12 at 7 48 42 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/8a0851ba-3bc0-4fd8-8211-ab4906e99f07)

4.) After entering contact infomation, select "Skip" since we already recived an acivation code via email.

![Screenshot 2023-11-12 at 7 49 08 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/7d63f202-ab44-4985-8fc9-032314cbac5d)

5.) Enter the activation code and continue.

![Screenshot 2023-11-12 at 7 49 41 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/28474c09-59ef-458e-aa2e-e06792ada939)

6.) Create a username/password for your account and then press submit. Nessus will finish up configurations.

![Screenshot 2023-11-12 at 7 49 58 PM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/1fcf369d-b9a9-44f4-a45e-8c9c85ca5035)

## Featured detections

This is the main page of Nessus Essentials. All scans are placed here unless moved in a folder.

![Screenshot 2023-11-12 at 5 21 14 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/3f3af2b8-395d-46e5-83ca-4c0483728f9d)

Nessus offers different templetes that cover 3 vulnerability scanner categories: Discovery, Vulnerabilities, and Compliance.

![Screenshot 2023-11-12 at 5 23 27 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/7c8b85fd-3699-4eb4-bb14-fbf4c94d4e2a)

## Types of Network Scans

* Uncredential: Does not utilize privleged credentials. Limited in scope but can still identify basic vulerabilities.
*   Credential: Utilizes privleged credentials to provide a more in-depth anlysis with accurate resilts.

    **I have attached examples of conducted scans from my MacOS device. It showcases how much more information can be acquired from a credentialed scan compared to a uncredentialed scan.**

    ```
      Note: Scans took place a month apart from each other to show how quickly vulnerabilities can manifest. 
    ```

### Uncredential

**Configurations**

![Screenshot 2023-11-12 at 5 31 19 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/21c04612-a004-40f6-afaa-de2adcd3d712)

#### Vulnerabilities

* Found vulnerabilities: 49
  * 2 CVSS
  * 47 of the vulnerabilities are infomational, which are actually facts rather than vulnerabilities.

![Screenshot 2023-11-12 at 5 31 41 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/222cbce7-c9db-4dae-b057-c973597002e7) ![Screenshot 2023-11-12 at 5 39 59 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/e9ecb7af-6c61-444b-a3e5-12db81745ed7)

### Credentialed

**Configurations**

![Screenshot 2023-11-12 at 5 25 51 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/5b369ff7-e9bb-4982-a8b1-d5511d64875a) ![Screenshot 2023-11-12 at 5 26 55 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/59e98af1-2b1a-4da5-acc2-a87292366551)

#### Vulnerabilities

* Found vulnerabilities: 52
  * 5 CVSS
  * 47 of the vulnerabilities are infomational, which are actually facts rather than vulnerabilities.

![Screenshot 2023-11-12 at 5 29 00 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/daa25041-e385-44ff-9ddb-5bac4ee1f437) ![Screenshot 2023-11-12 at 5 30 00 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/17b1f471-0c60-4a2c-959b-f8960421c7db)

#### Remediations

Credential scans have a leg up on uncredential scans due to the privleged access it has to machines. Nessus provides remediations for known CVEs when credentialed scans are conducted.

![Screenshot 2023-11-12 at 5 30 19 AM](https://github.com/RodMo97/Nessus-Vulnerability-Scanner/assets/124803297/7c79cf02-7e91-457e-acc9-7afdf5dc7e5a)

## Conclusion

Tenable Nessus is one of the many vulnerabilty scanners services available on the market. No matter if it personal or business-related, scanners are essensial for protecting assets. Risk, threat, and vulnerability management is a key element in the world of security.
