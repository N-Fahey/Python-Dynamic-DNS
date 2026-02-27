'''include/data.py
Contains functions to manage data files

Functions:
    load_ip: Retrieve saved IP address from previous script run
    save_ip: Save retrieved IP address for next run
'''

def load_ip(filepath: str) -> str:
    '''Retrieve saved IP address from previous script run

    Parameters:
        filepath (String): File path to the saved IP file
    
    Returns:
        IP (String): Saved IP address
    '''
    with open(filepath, 'a+') as ip_file:
        ip_file.seek(0)
        read_ip = ip_file.readline()
    
    return read_ip

def save_ip(filepath: str, ip:str) -> None:
    '''Save IP address for next run

    Parameters:
        filepath (String): File path to the saved IP file
        ip (String): IP address to save
    '''
    with open(filepath, 'w') as ip_file:
        ip_file.write(ip)