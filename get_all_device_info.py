import requests
import json
import urllib3
import math

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
    print('Login Worked!')


url = "https://sandbox-sdwan-1.cisco.com/dataservice/device"

response = session.get(url, verify=False).json()['data']
system_ip,iphostname = [],{}
for device in response:
    # system_ip.append(device['system-ip'])
    iphostname[device['system-ip']]= device['host-name']

# print(system_ip)
# for _ in system_ip:
for key,value in iphostname.items():
    url = "https://sandbox-sdwan-1.cisco.com/dataservice/device/system/status?deviceId="+ key
    system_status = session.get(url, verify=False).json()['data'][0]
    # print(_, system_status['cpu_user'], system_status['cpu_system'])
    print('DEVICE NAME: {0:15} CPU UTILIZATION: {1:3} '.format(value,math.trunc((100-float(system_status['cpu_idle']))*100)/100))
    # print('DEVICE NAME: ',value , 'CPU UTILIZATION: ', (100 - float(system_status['cpu_idle'])))