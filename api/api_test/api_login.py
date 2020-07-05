import requests
def login(username,password):
    R_url='http://localhost/api/mgr/loginReq'
    api_header={"Content-Type":"application/x-www-form-urlencoded"}
    api_body={"username":username,"password":password}
    api=requests.post(url=R_url,data=api_body,headers=api_header)
    return api.cookies['sessionid']

