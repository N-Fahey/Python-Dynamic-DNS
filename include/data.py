def load_ip(filepath: str):
    with open(filepath, 'a+') as ip_file:
        ip_file.seek(0)
        read_ip = ip_file.readline()
    
    return read_ip