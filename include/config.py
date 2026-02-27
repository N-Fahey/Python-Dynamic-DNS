'''include/config.py
Contains functions to manage user configuration of sites to update

Functions:
    load_config: Load configured sites to be updated
'''

import json

def load_config(filepath:str):
    '''Load Cloudflare sites to update DNS records for. Site should be configured as an A record
    Parameters:
        filepath (String): Path to sites configuration file
    
    Returns:
        config (Dict): JSON decoded sites configuration
        None: If error loading or decoding configuration
    '''
    try:
        with open(filepath, 'r') as config_file:
            config = json.load(config_file)
        
        return config
    
    except FileNotFoundError:
        print("Unable to load sites configuration file: file doesn't exist")
    except json.JSONDecodeError as e:
        print(f"JSON decode error when importing sites configuration: {e}")