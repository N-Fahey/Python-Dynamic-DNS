import include.api as api
from include.config import load_config
from include.data import load_ip, save_ip

def main():
    '''Script to process DNS updates for dynamic IP address'''
    # Configurable settings
    IP_FILENAME = 'data/ip.txt'

    # Get current WAN IP, and check if changed since previous run
    current_ip = api.get_current_ip()
    saved_ip = load_ip(IP_FILENAME)

    if saved_ip == current_ip:
        # Exit if no change to IP
        print("IP unchanged, exiting")
        return

    # Check settings for zones / records to update
    sites = load_config('sites.conf')['sites']

    # Check that zones / records exist in API & key valid
    account_dns_records = api.get_records()
    action_records = {name: details for name, details in account_dns_records.items() if name in sites}

    # Notify if any configured sites weren't found in provided account
    skipped_records = [name for name in sites if name not in action_records]
    if skipped_records:
        print(f"warn: Sites not found in Cloudflare account, skipping: {', '.join(skipped_records)}")

    # Attempt to update Cloudflare configuration to new IP for each configured site
    failed_records = []
    for record in action_records:
        res = api.update_record(action_records[record], current_ip)
        if res['success']:
            print(f"Succesfully updated IP for {record}")
        else:
            failed_records.append(record)

    # If any failed to update, log to console
    if failed_records:
        print(f"Failed to update records: {failed_records}")

    # Log IP change & save new IP as current IP
    save_ip(IP_FILENAME, current_ip)
    print("Update finished.")

if __name__ == '__main__':
    main()