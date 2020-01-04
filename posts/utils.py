import secrets

def get_slug(length=7):
    return secrets.token_urlsafe()[:length]




