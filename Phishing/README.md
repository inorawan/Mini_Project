# Malicious URL Detection
# Introduction
Phishing is a cyber attack where attackers try to trick individuals into revealing sensitive information such as passwords, credit card numbers, or other personal data. This is usually done by impersonating a trustworthy entity, such as a bank, government agency, or well-known company, through email, text messages, or fraudulent websites.
The phishing messages often contain links to fake websites that look legitimate but are designed to steal your information when you enter it. They may also contain attachments that, when opened, install malware on your device.

# Objective
Implement phishing detection in a simple browser. It can detect malicious URLs based on risk scores using a reputation-based detector API from APIVoid.com.

# Implementation

![implementation](Images/Final.png)

* User initiates the process by requesting a web page from a web server.
* Client (User's Browser) retrieves and displays the web page content.
* Extract all links and store them in a file.
* Calculate the score of the URL. If it is high, then no action will be taken. If score is low then block the URL.


## Installation

To install the project dependencies and set up the environment, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone [https://github.com/htoukour/Mozart.git](https://github.com/htoukour/Mozart.git)
   pip3 install -r requirements.txt
2. Replace Mozart.py file with [mozart.py](mozart.py)

# Output
![implementation](Images/mozart.png)
![implementation](Images/result.png)
