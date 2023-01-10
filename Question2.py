import requests

# Question 2
print("QUESTION 2: ",requests.__version__, "\n")

# Question 7
print("QUESTION 7:", requests.get("http://google.com").content, "\n")

# Question 8
print("QUESTION 8:",requests.get("https://raw.githubusercontent.com/StevenJiao/CMPUT404_LAB1/master/Question2.py").content, "\n")