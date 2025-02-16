from dotenv import load_dotenv
from telethon import TelegramClient, events
from metaapi import place_trade
from parser import extract_trade_info
import asyncio
from datetime import datetime
import os 
load_dotenv()

api_id = os.environ.get('TELEGARM_ID')
api_hash = os.environ.get('TELEGRAM_HASH_ID')
channel_usernames = [
    'ForexScalping_Signalsfree',
    'garrysignals',
    'wroot_bot',
]

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=channel_usernames))
async def new_message_listener(event):
    try:
        channel = await event.get_chat()
        raw_message = event.message.text
        parsed_data = {}
        # check if message has sl, tp
        lower_raw = raw_message.lower()
        if 'tp' in lower_raw and 'sl' in lower_raw:
            if 'xauusd' in lower_raw or 'gold' in lower_raw:
                if channel.username == 'wroot_bot':
                    print('Wroot Bot signal received')
                    trade_details = extract_trade_info(raw_message)
                elif channel.username == 'garrysignals':
                    print('Garry Signals received')
                    trade_details = extract_trade_info(raw_message)
                elif channel.username == 'ForexScalping_Signalsfree':
                    print('Forex Scalping signal')
                    trade_details = extract_trade_info(raw_message)
                else:
                    print('Unknown Channel')
                    return
                
                if trade_details:       
                    result = await place_trade(trade_details["Direction"])
                    if result == "TRADE_RETCODE_DONE":
                        print("Trade executed completely...")

    except Exception as e:
        print(f"Error: {str(e)}")

@client.on(events.MessageEdited(chats=channel_usernames))
async def edit_message_handler(event):
    try:
        channel = await event.get_chat()
        raw_message = event.message.text
        parsed_data = {}
        # check if message has sl, tp
        lower_raw = raw_message.lower()
        if 'tp' in lower_raw and 'sl' in lower_raw:
            if 'xauusd' in lower_raw or 'gold' in lower_raw:
                if channel.username == 'wroot_bot':
                    print('Wroot Bot signal received')
                    trade_details = extract_trade_info(raw_message)
                elif channel.username == 'garrysignals':
                    print('Garry Signals received')
                    trade_details = extract_trade_info(raw_message)
                elif channel.username == 'ForexScalping_Signalsfree':
                    print('Forex Scalping signal')
                    trade_details = extract_trade_info(raw_message)
                else:
                    print('Unknown Channel')
                    return
                
                if trade_details:       
                    result = await place_trade(trade_details["Direction"])
                    if result == "TRADE_RETCODE_DONE":
                        print("Trade executed completely...")

    except Exception as e:
        print(f"Edit Error: {str(e)}")

async def main():
    await client.start()
    print("Listening for messages... Press Ctrl+C to stop.")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())