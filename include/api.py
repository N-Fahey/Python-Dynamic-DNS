'''include/api.py
Contains functions including networks requests to interact with Cloudflare API & retrieve IP settings

Functions:
    get_current_ip: Retrieve internet IPv4 of current connection
    get_records: Retrieve all DNS records of the configured Cloudflare account
    update_record: Update a single DNS record to a provided IP
'''

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
    '''Retrieve current internet IPv4 address
    
    Returns:
        Current IP (string): Current IPv4 if retrieved
    
    Raises:
        ConnectionError: If error occured while retrieving IP
    '''
    # Get response
    res = requests.get(IPV4_REQUEST_URL)
    if not res.ok:
        raise requests.ConnectionError("Error retrieving current IP")
    
    # Remove newline char
    current_ip = res.text.replace('\n', '')
    
    return current_ip

def get_records() -> dict:
    '''Retrieve all DNS records of the configured Cloudflare account
    
    Returns:
        Records (Dict): Dictionary containing zone & record IDs for each returned site
    
    Raises:
        ConnectionError: If error occured while retrieving records
    '''
    #Query zones owned by configured account
    url = API_BASE_URL+'/zones'
    headers = COMMON_HEADERS
    response = requests.get(url,headers=headers).json()

    if not response['success']:
        raise requests.ConnectionError(f"Zone query failed with errors: {response['errors']}")
    
    records = {}

    #Loop through owned zones, build list of DNS records owned by account & their ids + zone ids
    for zone in response['result']:
        zone_id = zone['id']
        url = API_BASE_URL+f'/zones/{zone_id}/dns_records'
        response = requests.get(url,headers=headers).json()
        if not response['success']:
            raise requests.ConnectionError(f"Record query failed with errors: {response['errors']}")
        for record in response['result']:
            records[record['name']] = {
                'record_id':record['id'],
                'zone_id':zone_id
            }

    #Return records dict
    return records

def update_record(ids:dict, new_ip:str) -> dict:
    '''Update a single DNS record to a provided IP

    Parameters:
        ids (Dict): Dictionary containing zone_id, record_id to update
        new_ip (String): New IP address to update
    
    Returns:
        Records (Dict): Dictionary containing response details (success: bool, errors)
    '''
    url = API_BASE_URL + f"/zones/{ids['zone_id']}/dns_records/{ids['record_id']}"
    headers = COMMON_HEADERS
    data = {'content': new_ip}
    
    # Patch DNS record with new IP
    response = requests.patch(url,headers=headers,json=data).json()
    if response['success']:
        return {'success': True}
    else:
        # Return errors if failed
        return {'success': False, 'errors': response['errors']}