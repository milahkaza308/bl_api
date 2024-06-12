import time
from jwt_handeler1 import endcodeJWT, decodeJWT, refreshJWT

user = {'emil': 'xas', 'username':'xxxx', 'id':1}
jwt_token = endcodeJWT(user)
time.sleep(6)
decoded = decodeJWT(jwt_token['access'])

new_jwt_token = refreshJWT(jwt_token['refresh_token'])