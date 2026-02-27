'''include/env.py
Contains functions to manage environment variables

Functions:
    load_env: Retrieve expected enviroment variables
'''

from dotenv import load_dotenv
from os import getenv

def load_env():
    '''Retrieve expected enviroment variables
    
    Returns:
        Values (Dict): Key & value of required environment variables
    
    Raises:
        EnvironmentError: If any required environment variables are missing or not set
    '''
    # Retrieve environment variables
    load_dotenv()

    # Attempt to load required variables
    env_dict = {
        'CF_KEY': getenv('CF_KEY'),
        'CF_EMAIL': getenv('CF_EMAIL')
    }

    # If any missing, raise error
    missing_envs = [k for k, v in env_dict.items() if v is None]
    if missing_envs:
        raise EnvironmentError(f"Missing environment variables: [{', '.join(missing_envs)}]")
    
    return env_dict