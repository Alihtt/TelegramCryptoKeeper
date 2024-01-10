# Telegram Crypto Keeper

This script is designed receive cheques and tokens like wallet token from joined channels

### Installation

To install the required packages, you can use the `requirements.txt` file provided. Make sure you have Python and pip
installed on your system.

Install the required packages:

```bash
pip install -r requirements.txt
```

### Configuration

Before running the script, you need to set up your Telegram API credentials (api_id and api_hash and phone_number) in
the `config.py` file. Additionally, you can define your default timezone in the same file.

```python
# config.py
api_id = '<your_api_id>'
api_hash = '<your_api_hash>'
phone_number = 'your_phone_number'
```

### Execution

To run the script, execute the `main.py` file. Afterward, your Telegram profile status will be updated every minute,
showing the time along with the selected timezone.

```bash
python main.py
```

### Stopping Execution

To stop the script's execution, you can use the Ctrl + C keys in the terminal.

### Note

- Ensure that your Telegram API authentication details are correctly set up in the `config.py` file and never share them
  with others.

### Warning

Continuous and unauthorized use of this script might violate Telegram API terms of service and lead to issues with your
account. Please use this script with caution and in compliance with the regulations. The script author bears no
responsibility for improper use of this script.
