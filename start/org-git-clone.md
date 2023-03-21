### Clone Organization Git Repository into local using Terminal

1. Generate Personal Access Tokens here: `https://github.com/settings/tokens` Settings / Developer settings / Personal access tokens

* Fine-grained tokens
``` sh Fine-grained tokens
vijay.pavan@<HOST> ~ % git clone https://oauth2:github_pat_<TOKEN>@github.com/<org>/repo_name 
Cloning into 'repo_name'...
***remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/<org>/repo_name/': The requested URL returned error: 403***
```

* Tokens classic
``` sh Tokens (classic)
vijay.pavan@<HOST> ~ % git clone https://oauth2:ghp_<TOKEN>@github.com/<org>/repo_name
Cloning into 'repo_name'...
remote: The `<org>' organization has enabled or enforced SAML SSO. To access
remote: this repository, visit ** https://github.com/orgs/<org>/sso?authorization_request=AU<CODE> **
remote: and try your request again.
fatal: unable to access 'https://github.com/<org>/repo_name/': The requested URL returned error: 403
```

2. Open the above repository URL in the browser, it authorizes the Client to access the Repo

``` sh Run the previous command 
vijay.pavan@<HOST> ~ % git clone https://oauth2:ghp_<TOKEN>@github.com/<org>/repo_name
Cloning into 'repo_name'...
remote: Enumerating objects: 236, done.
remote: Counting objects: 100% (236/236), done.
remote: Compressing objects: 100% (194/194), done.
remote: Total 236 (delta 28), reused 207 (delta 23), pack-reused 0
Receiving objects: 100% (236/236), 164.59 KiB | 2.46 MiB/s, done.
Resolving deltas: 100% (28/28), done.
```