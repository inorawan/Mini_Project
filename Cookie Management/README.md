# Cookie Management
## Introduction
A cookie is a small piece of data that a website stores on your web browser when you visit it.
When you visit a website, the website may want to remember some information about you, such as your preferences. Your web browser then stores this cookie on your computer. It's like the website leaving a little note on your computer for later. The next time you visit the same website, your web browser sends the cookie back to the website. This helps the website remember your preferences or previous actions.
cookies are used to enhance your browsing experience by allowing websites to remember certain information about you. They are commonly used for purposes such as maintaining sessions, tracking user behavior, and personalizing content.

## Objective 
Add the cookie module to the simple browser to manage cookies easily. Whenever a user visits a website that sends a cookie, the user can respond to it depending on the legitimacy of the website. However, this project aims to allow the user to add the website to the safe list so that the browser will not ask whether the user wants to accept the cookie or not.

## Implementation
This diagram represents the project's approach.


![Cookie_flow_diagram](Images/Cookie_flow_diagram.png)

* The user initiates the process by accessing a webpage.
* Browser asks users if they want to add the website to their preferred list.
* If the user presses the accept button, it is saved in the preferred list, and the webpage is returned.
* If the user presses no, the webpage is returned.

This project used [Mozart browser](https://github.com/htoukour/Mozart.git), which uses the PyQt5 Python library to develop a simple browser. In this browser, we added cookie management to it. In this folder, you can see [main](main.py), which is a modified version of the Mozart browser with the added cookie management feature.

## Steps to run

To install the project dependencies and set up the environment, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/htoukour/Mozart.git
   pip3 install -r requirements.txt
2. Replace Mozart.py file with [main.py](main.py) and download [scratch.py](scrach.py) in the Mozart folder.
3. Run the following command
6. ```bash
   python3 mozart.py

## Output

![Mozart Preferred list](Images/Preferred_list.png)
![Mozart Preferred list](Images/Mozart_popup.png)
![Mozart Preferred list](Images/Mozart_popup2.png)
