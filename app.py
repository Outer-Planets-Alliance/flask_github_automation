from flask import Flask, request
import os
import json
import requests

application = Flask(__name__)

@application.route("/payload", methods=["POST"])
def webhook():
    payload = request.get_json()
    user = "kuhlman-labs"
    creds = os.environ["GH_TOKEN"]
    if payload["action"] == "created":
        branch_protection_payload = {
                "required_status_checks": {"strict": True, "contexts": ["default"]},
                "enforce_admins": True,
                "required_pull_request_reviews": None,
                "restrictions": None,
        }
        repo = payload["repository"]["url"] + "/branches/main/protection"
        session = requests.Session()
        session.auth(user, creds)
        response = session.post(repo, params=branch_protection_payload)
        print(response)
        if response.status_code == 200:
            if payload["repository"]["has_issues"]:
                issues_payload = {
                    "title": "Branch Protection Added",
                    "body": "@" + user + " A new branch protection was added to main branch."
                }
                session = requests.Session()
                session.auth(user, creds)
                response_1 = session.post(payload["repository"]["url"] + "/issues", params=issues_payload)
                print(response_1.status_code)
    return "OK"

if __name__ == "__main__":
    application.run(host='0.0.0.0')