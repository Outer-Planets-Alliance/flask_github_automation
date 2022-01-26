# GitHub Branch Protection

## Purpose

This repository is meant to provide a sample of how to utilize the GitHub API and Organization Webhooks to automate the protection of the `main` branch whenever a repository is created within your GitHub Organization.

## How to use


#### Software Dependencies

* [python 3.9](https://www.python.org/downloads/)
* [pip3](https://pip.pypa.io/en/stable/installation/)

#### Platform Dependencies

* [Create an Azure web app service](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask)
* [Create a GitHub Organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch)

### Deploying Locally

* Set environment variable for `GH_TOKEN`.
* run `pip install -r requirements.txt`.
* run  `flask run`.
* expose local service to internet using [ngrok](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks#exposing-localhost-to-the-internet).
* create a [webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks#setting-up-a-webhook) in your organization and set the payload URL to the ngrok address.

### Deploying to Azure 
* set enviornment variable for `GH_TOKEN` in your web app Application settings.
* Use the [deployment center](https://docs.microsoft.com/en-us/azure/app-service/deploy-continuous-deployment?tabs=github#configure-the-deployment-source) to setup the deployment source.
* create a [webhook](https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks#setting-up-a-webhook) in your organization and set the payload URL to the web applicaiton's URL.

### Refrences used and Attribution
- https://github.com/github/platform-samples/tree/master/hooks/python/flask-github-webhooks
- https://github.com/zkoppert/Auto-branch-protect
- https://docs.github.com/en/rest/reference/branches#update-branch-protection
- https://docs.github.com/en/developers/webhooks-and-events/webhooks/creating-webhooks
- https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository
- https://docs.github.com/en/developers/webhooks-and-events/webhooks/testing-webhooks