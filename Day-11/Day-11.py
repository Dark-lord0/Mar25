#get PR info on repo using python
#k8s
#step-1 use request module
#step-2 make API call
#step-3 convert JSON-Dictionary
#step-4 print O/P
import requests
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = response.json()

for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])



