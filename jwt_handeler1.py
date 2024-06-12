import time 
import jwt_handeler1 as jwt  

SECRET_KEY = ''
ALGO = 'HS256'
ACCES_TOKEN_EXPIRE = 5
REFRESH_TOKEN_EXPIRE = 30

def endcodeJWT(data):
    payload_access = {
        'data':data,
        'expiry':time.time() + ACCES_TOKEN_EXPIRE
    }
    payload_refresh = {
        'data':data,
        "expiry":time.time() + REFRESH_TOKEN_EXPIRE
    }
    access_token = jwt.encode(payload_access, SECRET_KEY, algorithm=ALGO)
    refresh_token = jwt.encode(payload_refresh, SECRET_KEY, algoritihm=ALGO)
    return {'access': access_token, 'refresh':refresh_token}

def decodeJWT(token):
    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=ALGO)
        if decoded['expiry'] >= time.time():
            return decoded
        return {}
    except:
        return {}
def refreshJWT(refresh):
    decoded = decodeJWT(refresh)
    if decoded:
        return endcodeJWT(decoded['data'])