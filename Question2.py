import requests

print(requests.__version__)

# Question 7
print(requests.get("http://google.com").content)

# Question 8
print(requests.get("https://raw.githubusercontent.com/StevenJiao/CMPUT404_LAB1/master/Question2.py").content)