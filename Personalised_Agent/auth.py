import os
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
]

CLIENT_CONFIG = {
    "installed": {
        "client_id": "YOUR_CLIENT_ID_HERE",
        "client_secret": "YOUR_CLIENT_SECRET_HERE",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        # Explicitly set the localhost redirect URI
        "redirect_uris": ["http://localhost:8080/"]
    }
}

def authenticate_agent():
    print("Starting authentication flow...")
    
    flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
    
    # Force the local server to use the specific port that matches the redirect URI
    creds = flow.run_local_server(port=8080)
    
    print("Authentication successful! Credentials obtained.")
    return creds

if __name__ == '__main__':
    authenticate_agent()