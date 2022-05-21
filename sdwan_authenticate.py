import requests
import json
import urllib3

def sdwan_authenticate():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = "https://sandbox-sdwan-1.cisco.com/j_security_check"

    payload='j_username=devnetuser&j_password=RG!_Yw919_83'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    session = requests.session()
    response = session.post(url, headers=headers, data=payload, verify=False)

    if not response.ok or response.text:
        print('Login Fail')
        import sys
        sys.exit(1)
    else:
        return session

def get_all_device_info(session):

    url = "https://sandbox-sdwan-1.cisco.com/dataservice/device"
    response = session.get(url, verify=False).json()['data']
    system_ip,iphostname = [],{}
    for device in response:
        # system_ip.append(device['system-ip'])
        iphostname[device['system-ip']]= device['host-name']
    
    return iphostname