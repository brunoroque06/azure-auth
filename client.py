import msal
import requests

config = {
    "authority": "https://login.microsoftonline.com/<tenant>",
    "client_id": "<client>",
    "scope": [],
    "username": "<mail>",
    "endpoint": "http://127.0.0.1:5000",
}

app = msal.PublicClientApplication(
    config["client_id"],
    authority=config["authority"],
)

result = None

accounts = app.get_accounts(username=config["username"])
if accounts:
    result = app.acquire_token_silent(config["scope"], account=accounts[0])

if not result:
    result = app.acquire_token_interactive(config["scope"])

if "access_token" in result:
    res = requests.get(
        config["endpoint"],
        headers={"Authorization": "Bearer " + result["access_token"]},
    )
    print(res.text)
else:
    print(result.get("error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))
