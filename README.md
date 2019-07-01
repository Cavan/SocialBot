# SocialBot

The purpose of **SocialBot** is to autonomously manage various social networks, by making posts, follow / unfollow users, and log the activities to track operations and troubleshoot problems, for example: structural changes to the website etc.



## Development Environment

* Language: **Python 3.7**
* Environment: **Anaconda https://www.anaconda.com/distribution/** this allows us to get environments up and running quickly and also to switch between Python versions, and easy package management.
* IDE: **Visual Studio Code**



## Selenium & Webdriver

Selenium and Webdriver allow us to automate browser tasks, and is what is used by Python to navigate a site performing various actions as per program design.

* Navigating to a specific url(s).
* Filling in webforms.
* Logging into accounts.
* Posting content.
* Interacting with other users.
* Sending data back to be further analyzed. 



##  Python Packages 

Below are the required packages that are needed to run SocialBot.

```python
from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
import os
import time
import sys
```





## To-Do 

The software when completed will be able to manage the following social accounts.

- [ ] facebook
- [ ] pinterest
- [ ] twitter
- [ ] instagram - Currently able to login and follow a specified user.



