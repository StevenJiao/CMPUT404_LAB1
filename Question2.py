import requests

print(requests.__version__)

# Question 7
print(requests.get("http://google.com").content)