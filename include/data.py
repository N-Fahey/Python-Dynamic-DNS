def load_ip(filepath: str) -> str:
    with open(filepath, 'a+') as ip_file:
        ip_file.seek(0)
        read_ip = ip_file.readline()
    
    return read_ip

def save_ip(filepath: str, ip:str) -> None:
    with open(filepath, 'w') as ip_file:
        ip_file.write(ip)