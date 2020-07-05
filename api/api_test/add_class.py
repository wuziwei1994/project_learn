import requests
import api_login
class_url='http://localhost/api/mgr/sq_mgr/'
class_header={'Content-Type':'application/x-www-form-urlencoded'}
class_cookies = {'sessionid':api_login.login('auto','sdfsdfsdf')}
class_body={'action':'add_course',
            'data':"""{
      "name":"Python",
      "desc":"Python自动化课程",
      "display_idx":"10"
            }"""}
addClass=requests.post(class_url,data=class_body,cookies=class_cookies)
addClass.encoding='unicode_escape'
print(addClass.text)