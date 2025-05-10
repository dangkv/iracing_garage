import base64
import hashlib

from datetime import datetime, timezone


def get_current_utc_time():
    current_time_utc = datetime.now(timezone.utc)

    # Format the UTC time as a string in ISO 8601 format
    timestamp_utc = current_time_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    return timestamp_utc


def encode_pw(username, password):
    initialHash = hashlib.sha256(
        (password + username.lower()).encode("utf-8")
    ).digest()
    hashInBase64 = base64.b64encode(initialHash).decode("utf-8")

    return hashInBase64
