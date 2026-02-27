import requests

from .env import load_env

CF_CONFIG = load_env()
IPV4_REQUEST_URL = 'http://ipv4.icanhazip.com'
API_BASE_URL = 'https://api.cloudflare.com/client/v4'
COMMON_HEADERS = {
    "X-Auth-Email": CF_CONFIG['CF_EMAIL'],
    "X-Auth-Key": CF_CONFIG['CF_KEY'],
    "Content-Type": "application/json"
}

def get_current_ip() -> str:
    res = requests.get(IPV4_REQUEST_URL)
    if not res.ok:
        raise requests.ConnectionError("Error retrieving current IP")
    
    current_ip = res.text.replace('\n', '')
    
    return current_ip

def get_records() -> dict:
    #Query zones owned by configured account
    url = API_BASE_URL+'/zones'
    headers = COMMON_HEADERS
    response = requests.get(url,headers=headers).json()
    if not response['success']:
        print((f"Zone query failed with errors: {response['errors']}"))
        return
    
    records = {}

    #Loop through owned zones, build list of DNS records owned by account & their ids + zone ids
    for zone in response['result']:
        zone_id = zone['id']
        url = API_BASE_URL+f'/zones/{zone_id}/dns_records'
        response = requests.get(url,headers=headers).json()
        if not response['success']:
            print(f"Record query failed with errors: {response['errors']}")
            return
        for record in response['result']:
            records[record['name']] = {
                'record_id':record['id'],
                'zone_id':zone_id
            }

    #Return records dict
    return records

def update_record(ids:dict, new_ip:str) -> dict:
    url = API_BASE_URL + f"/zones/{ids['zone_id']}/dns_records/{ids['record_id']}"
    headers = COMMON_HEADERS
    data = {'content': new_ip}
    
    response = requests.patch(url,headers=headers,json=data).json()
    if response['success']:
        return {'success': True}
    else:
        return {'success': False, 'errors': response['errors']}