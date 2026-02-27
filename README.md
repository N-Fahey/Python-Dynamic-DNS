# Python-Dynamic-DNS
Lightweight dynamic DNS update script for Cloudflare

## Requirements
- Python version 3.8 or higher
- Cloudflare account with API access configured

## Dependencies
- requests (2.32.5): Library for making required HTTP requests.
- python-dotenv (1.2.1): Library for loading environment variables.

## Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:N-Fahey/Python-Dynamic-DNS.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Python-Dynamic-DNS
    ```
3. Create and activate a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
1. Copy `sites.conf.default` to `sites.conf`:
    ```bash
    cp sites.conf.default sites.conf
    ```
2. Edit `sites.conf` to add your domains to update.

3. Copy `.env.default` to `.env`:
    ```bash
    cp .env.default .env
    ```
4. Edit `.env` to add your Cloudflare API credentials and other settings:
    ```
    CF_KEY=your_cloudflare_api_key
    CF_EMAIL=your_cloudflare_email@example.com
    ```

## Usage
Activate the virtual environment and run the script:
```bash
source .venv/bin/activate
python app.py
```

Alternatively, you can set up a cron job to run the script at regular intervals (e.g., every 5 minutes):
```bash
*/5 * * * * /path/to/venv/bin/python /path/to/app.py >> /path/to/logfile.log 2>&1
```
*Note: Replace `/path/to/venv/bin/python`, `/path/to/app.py` and `/path/to/logfile.log` with the actual paths on your system.*

## License
MIT License.