# Azure Authentication

## Create Application

1. Go to [AAD Registered Applications](https://portal.azure.com/?quickstart=true#view/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/~/RegisteredApps)
2. `New registration`
3. On `Redirect URI (optional)`, select `Public client/native (mobile/desktop)` and `http://localhost` url

Unfortunately, we currently cannot use the CLI to create a native AAD application as the flags were removed: <https://github.com/MicrosoftDocs/azure-docs/issues/102863> .

## Start

Configure `client.py`, and then:

```pwsh
flask --app server run
python client.py
Invoke-RestMethod http://127.0.0.1:5000
Invoke-RestMethod -Headers @{ 'Authorization' = 'Bearer what-a-great-token' } http://127.0.0.1:5000
```

## References

- <https://gist.github.com/darrenjrobinson/4200a28226454b61685891848119da99#file-query-microsoft-graph-with-python-and-decode-aad-access-token-py>
