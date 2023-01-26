#!/usr/bin/env python3
import os
import json

# print("Content-type: application/json")
print("Content-type: text/html")
print()
# print(json.dumps(dict(os.environ)))
print(f"<p>HTTP USER AGENT: { os.environ['HTTP_USER_AGENT'] }<\p>")