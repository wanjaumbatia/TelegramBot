from metaapi_cloud_sdk import MetaApi

# Replace with your MetaAPI credentials
API_KEY = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmMzRiY2MyMTBlYTc1OTMxNjUwMzY1ZDczYjY2MTY1MSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZXN0LWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1ycGMtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6Im1ldGFzdGF0cy1hcGkiLCJtZXRob2RzIjpbIm1ldGFzdGF0cy1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiKjokVVNFUl9JRCQ6KiJdfSx7ImlkIjoicmlzay1tYW5hZ2VtZW50LWFwaSIsIm1ldGhvZHMiOlsicmlzay1tYW5hZ2VtZW50LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19LHsiaWQiOiJtdC1tYW5hZ2VyLWFwaSIsIm1ldGhvZHMiOlsibXQtbWFuYWdlci1hcGk6cmVzdDpkZWFsaW5nOio6KiIsIm10LW1hbmFnZXItYXBpOnJlc3Q6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbIio6JFVTRVJfSUQkOioiXX0seyJpZCI6ImJpbGxpbmctYXBpIiwibWV0aG9kcyI6WyJiaWxsaW5nLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyIqOiRVU0VSX0lEJDoqIl19XSwiaWdub3JlUmF0ZUxpbWl0cyI6ZmFsc2UsInRva2VuSWQiOiIyMDIxMDIxMyIsImltcGVyc29uYXRlZCI6ZmFsc2UsInJlYWxVc2VySWQiOiJmMzRiY2MyMTBlYTc1OTMxNjUwMzY1ZDczYjY2MTY1MSIsImlhdCI6MTczODg0NjIxMywiZXhwIjoxNzQ2NjIyMjEzfQ.cXcLk83eka7DDFOTP9FqEIPQctrtFOtMW0rAe2omCcK5lr4sW3Gmo6cLKOgvtiCE0m_cviWmHzcKMBBr-UKNvvmNUovc_jh4s72iteDzC5tjspfHGlykP-nHyEvFoaubJn0UcS6XgpholWVbh_-FT0BlmgZn9qbCbs2ztSLTVpTejt1NmywR8JFWT4DjsBDslU5uOjZLQ2kBL8IJfyHE1_mDWwOki2enX3cUc2YjiZBvc0-cHsVhIox7_rrg34rwGuKk1QQ-OGQadg-eZaNqgMPzzGbfFQI1U1o2exR716sfg1o-YEXDIFqEUfO_SUUgmzbvNM8HOJmDogjlTf_bHksQV2cDS61VNiYweDQcMWWsye8sYMRzEFHUCIHXB2wDlJlJRl7U8-K1A2Dmv9RA8wOUL6suE_Ezoqw1YL9rdsciYI2iCzjoxOSbVUPeVwUP4G00XoCg7Vz11lkzLOmP-SW8NR7dzaYVrQmMrRvPdDFPlDWhPVAT6zdyiTthtHxM6jHxnweAL-ypOnhWWP50hNj_lGZqsVLMmdKrP4qbsqmaRJmU--WIdK9xN_4Nzg-juqqLVA4hxhZXNwScJ_hgWEJKZGQ8EdWXl5HLbWZcsuM2R_aV4TsR_5-inQgc0VjsRdswhCuUM1B6uA5HFk_x58fx0ZBsAEgXx4APYR8_yTI"
ACCOUNT_ID = "0703ede8-fd4c-4ab1-bc25-c667664375d3"
PIP_SIZE = 0.1  
TP_PIPS = 40  
SL_PIPS = 30
LOST_SIZE = 0.01


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
    
   
