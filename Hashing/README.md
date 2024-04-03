# Ensuring Web Content Integrity using Hashing
# Introduction
Hashing converts input data (message) into a fixed-size string of bytes, typically representing a shorter, unique identifier of the original data. This process uses a hash function, which takes an input (message) and produces a fixed-size string of characters. The most widely used standard hash functions to ensure integrity and authenticity include MD5 (Message Digest 5) and the SHA(Secure Hashing Algorithm) family (SHA-1, SHA-2, and SHA-3).
In this digital era, Web services are based on a client-server architecture. The client-server architecture refers to a system that hosts, delivers, and manages most of the resources and services that the client requests.

# Objective
Maintaining the integrity of web content remains a critical challenge amidst evolving cybersecurity threats. We suggest a server-side approach to ensure the integrity of web content, addressing concerns arising from potential changes at the server. This approach leverages hash functions for content  integrity verification and geographically distributed servers to recover content in case of attack.
# Proposed Method

* Web contents are hosted on the main server, along with their corresponding hash values stored there.
* When a client requests a web page, the server initiates the process by calculating the hash value of the requested content.
* The server then compares the calculated hash value with the stored hash value of the content.
* If the hash values match, indicating the content integrity, the server proceeds to send the web page to the client.
* However, if the hash values do not match, suggesting potential tampering or corruption, the main server sends a request to the backup server.
* The backup server, which also contains the web contents and their hash values, receives the request and calculates the hash value of the requested data.
* If the calculated hash value matches the stored hash value, indicating content integrity, the backup server sends the web page back to the main server.
* In the event of a mismatch, indicating potential data inconsistency, the backup server forwards the request to another backup server.
* This process continues until a backup server with matching hash values is found or until all backup servers are exhausted.
* The presence of multiple backup servers distributed across different geographical locations ensures redundancy and reliability in data retrieval, enhancing overall system resilience and availability.


# Implementation
Hosted two servers named serverA and serverB. And also created a client. Both servers and client are runing in a same syatem on different port. For creating serverA [serverA](serverA.py)
