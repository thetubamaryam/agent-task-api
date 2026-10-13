import os
from fastapi import Header, HTTPException


def verify_api_key(x_api_key: str = Header(...)):
    valid_keys = os.getenv("API_KEYS", "").split(",")
    if x_api_key not in valid_keys:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return x_api_key