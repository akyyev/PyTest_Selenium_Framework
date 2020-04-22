import requests

# rest api
response = requests.get("https://jira.atlassian.com/rest/api/2/issue/JSWSERVER-1")
assert response.status_code == 200
assert response.headers['Content-Type'] == "application/json;charset=UTF-8"
response_body = response.json()
print(response.status_code)
assert response_body["key"] == "JSWSERVER-1"
