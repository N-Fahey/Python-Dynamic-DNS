from dotenv import load_dotenv
from os import getenv

def load_env():
    load_dotenv()

    env_dict = {
        'CF_KEY': getenv('CF_KEY'),
        'CF_EMAIL': getenv('CF_EMAIL')
    }

    missing_envs = [k for k, v in env_dict.items() if v is None]
    if missing_envs:
        raise EnvironmentError(f"Missing environment variables: [{', '.join(missing_envs)}]")
    
    return env_dict