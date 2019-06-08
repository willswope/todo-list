$env:FLASK_APP = "main.py"
$env:OAUTHLIB_RELAX_TOKEN_SCOPE = "true"
$env:OAUTHLIB_INSECURE_TRANSPORT = "true"

flask run