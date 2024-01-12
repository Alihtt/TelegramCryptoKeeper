from pyrogram import Client
import config
import logging

app = Client(name='CryptoKeeper',
             api_id=config.api_id,
             api_hash=config.api_hash,
             phone_number=config.phone_number,
             plugins=dict(root='plugins'))

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)
logging.info('Bot started...')
print('Bot started...')
app.run()
