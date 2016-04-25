import json
import hmac
import base64
import hashlib

def load_signed_request(signed_request, secret_key):
    def base64_url_decode(data):
        data = data.encode('ascii')
        data += '='.encode('ascii') * (4 - (len(data) % 4))
        return base64.urlsafe_b64decode(data)

    try:
        sig, payload = signed_request.split('.', 1)
    except ValueError:
        pass  # ignore if can't split on dot
    else:
        sig = base64_url_decode(sig)
        payload_json_bytes = base64_url_decode(payload)
        data = json.loads(payload_json_bytes.decode('utf-8', 'replace'))
        expected_sig = hmac.new(secret_key.encode('ascii'),
                                msg=payload.encode('ascii'),
                                digestmod=hashlib.sha256).digest()
        # allow the signed_request to function for upto 1 day
        return data