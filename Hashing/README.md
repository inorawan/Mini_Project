# Ensuring Web Content Integrity using Hashing
# Introduction
Hashing converts input data (message) into a fixed-size string of bytes, typically representing a shorter, unique identifier of the original data. This process uses a hash function, which takes an input (message) and produces a fixed-size string of characters. The most widely used standard hash functions to ensure integrity and authenticity include MD5 (Message Digest 5) and the SHA(Secure Hashing Algorithm) family (SHA-1, SHA-2, and SHA-3).
In this digital era, Web services are based on a client-server architecture. The client-server architecture refers to a system that hosts, delivers, and manages most of the resources and services that the client requests.

# Objective
Maintaining the integrity of web content remains a critical challenge amidst evolving cybersecurity threats. We suggest a server-side approach to ensure the integrity of web content, addressing concerns arising from potential changes at the server. This approach leverages hash functions for content  integrity verification and geographically distributed servers to recover content in case of attack.
# Proposed Method
* Web contents are hosted on the main server, and their hash values are stored there. When a client requests for a web page, the server first calculates the hash value of the content and matches it with the stored hash value. If matched, the server will send the web page to the client. If it is not matched then main server will send request to backup server and backup server also have the web contents and their hash value. Backup server will calculate hash value of the requested data. If it is matched, it send the web page to main server. If it is not matched then it send to other backup server.
* There are many backup server which are located on different geographical location.
