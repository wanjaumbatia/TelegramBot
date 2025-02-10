from metaapi_cloud_sdk import MetaApi
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your MetaAPI credentials
API_KEY = os.environ.get('METATAPI_API_KEY')
ACCOUNT_ID = os.environ.get('METAAPI_ACCOUNT_ID')
PIP_SIZE = 0.1  
TP_PIPS = 40  
SL_PIPS = 30
LOST_SIZE = 0.01

async def get_connection():
    api = MetaApi(API_KEY)
    account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
    initial_state = account.state
    deployed_states = ['DEPLOYING', 'DEPLOYED']

    if initial_state not in deployed_states:        
        print('Deploying account')
        await account.deploy()

    await account.wait_connected()

    connection = account.get_rpc_connection()
    await connection.connect()

    await connection.wait_synchronized()

    return connection

async def get_market_prices(connection, symbol):
    """Fetches the latest bid and ask price for a given symbol."""
    quote = await connection.get_symbol_price(symbol)
    bid, ask = quote['bid'], quote['ask']
    return bid, ask



async def place_trade(direction):
    symbol = "XAUUSDm"
    api = MetaApi(API_KEY)
    account = await api.metatrader_account_api.get_account(ACCOUNT_ID)
    initial_state = account.state
    deployed_states = ['DEPLOYING', 'DEPLOYED']

    if initial_state not in deployed_states:        
        print('Deploying account')
        await account.deploy()

    await account.wait_connected()

    connection = account.get_rpc_connection()
    await connection.connect()

    await connection.wait_synchronized()

    
    try:  
        bid, ask = await get_market_prices(connection, symbol)
        if direction == "BUY":
            sl = ask - (SL_PIPS * PIP_SIZE)  # SL below entry
            tp = ask + (TP_PIPS * PIP_SIZE)  # TP above entry
            result = await connection.create_market_buy_order(symbol=symbol, volume=LOST_SIZE, stop_loss=sl, take_profit=tp, options={'comment': 'WROOT_AI', 'clientId': 'TE_GBPUSD_7hyINWqAl'})
            
        elif direction == "SELL":            
            tp = bid - (TP_PIPS * PIP_SIZE)
            sl = bid + (SL_PIPS * PIP_SIZE)
            result = await connection.create_market_sell_order(symbol=symbol, volume=LOST_SIZE, stop_loss=sl, take_profit=tp, options={'comment': 'WROOT_AI', 'clientId': 'TE_GBPUSD_7hyINWqAl'})
            
        return result['stringCode']
    except Exception as e:
        print(api.format_error(e))
    

   