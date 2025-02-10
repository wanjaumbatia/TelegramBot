import os
import asyncio
from metaapi_cloud_sdk import MetaApi
from datetime import datetime, timedelta

# Note: for information on how to use this example code please read https://metaapi.cloud/docs/client/usingCodeExamples

token = os.getenv('TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiJmMzRiY2MyMTBlYTc1OTMxNjUwMzY1ZDczYjY2MTY1MSIsInBlcm1pc3Npb25zIjpbXSwiYWNjZXNzUnVsZXMiOlt7ImlkIjoidHJhZGluZy1hY2NvdW50LW1hbmFnZW1lbnQtYXBpIiwibWV0aG9kcyI6WyJ0cmFkaW5nLWFjY291bnQtbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDcwM2VkZTgtZmQ0Yy00YWIxLWJjMjUtYzY2NzY2NDM3NWQzIl19LHsiaWQiOiJtZXRhYXBpLXJlc3QtYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNzAzZWRlOC1mZDRjLTRhYjEtYmMyNS1jNjY3NjY0Mzc1ZDMiXX0seyJpZCI6Im1ldGFhcGktcnBjLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA3MDNlZGU4LWZkNGMtNGFiMS1iYzI1LWM2Njc2NjQzNzVkMyJdfSx7ImlkIjoibWV0YWFwaS1yZWFsLXRpbWUtc3RyZWFtaW5nLWFwaSIsIm1ldGhvZHMiOlsibWV0YWFwaS1hcGk6d3M6cHVibGljOio6KiJdLCJyb2xlcyI6WyJyZWFkZXIiLCJ3cml0ZXIiXSwicmVzb3VyY2VzIjpbImFjY291bnQ6JFVTRVJfSUQkOjA3MDNlZGU4LWZkNGMtNGFiMS1iYzI1LWM2Njc2NjQzNzVkMyJdfSx7ImlkIjoibWV0YXN0YXRzLWFwaSIsIm1ldGhvZHMiOlsibWV0YXN0YXRzLWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNzAzZWRlOC1mZDRjLTRhYjEtYmMyNS1jNjY3NjY0Mzc1ZDMiXX0seyJpZCI6InJpc2stbWFuYWdlbWVudC1hcGkiLCJtZXRob2RzIjpbInJpc2stbWFuYWdlbWVudC1hcGk6cmVzdDpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDcwM2VkZTgtZmQ0Yy00YWIxLWJjMjUtYzY2NzY2NDM3NWQzIl19LHsiaWQiOiJtZXRhYXBpLXJlYWwtdGltZS1zdHJlYW1pbmctYXBpIiwibWV0aG9kcyI6WyJtZXRhYXBpLWFwaTp3czpwdWJsaWM6KjoqIl0sInJvbGVzIjpbInJlYWRlciIsIndyaXRlciJdLCJyZXNvdXJjZXMiOlsiYWNjb3VudDokVVNFUl9JRCQ6MDcwM2VkZTgtZmQ0Yy00YWIxLWJjMjUtYzY2NzY2NDM3NWQzIl19LHsiaWQiOiJjb3B5ZmFjdG9yeS1hcGkiLCJtZXRob2RzIjpbImNvcHlmYWN0b3J5LWFwaTpyZXN0OnB1YmxpYzoqOioiXSwicm9sZXMiOlsicmVhZGVyIiwid3JpdGVyIl0sInJlc291cmNlcyI6WyJhY2NvdW50OiRVU0VSX0lEJDowNzAzZWRlOC1mZDRjLTRhYjEtYmMyNS1jNjY3NjY0Mzc1ZDMiXX1dLCJpZ25vcmVSYXRlTGltaXRzIjpmYWxzZSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaW1wZXJzb25hdGVkIjpmYWxzZSwicmVhbFVzZXJJZCI6ImYzNGJjYzIxMGVhNzU5MzE2NTAzNjVkNzNiNjYxNjUxIiwiaWF0IjoxNzM4ODQ2MjU1LCJleHAiOjE3NDE0MzgyNTV9.cCxeOqACu6wULh_8vGJFmcPtVIBo1bOf2xFm-8xOwGPEaArJi23Sf6GNMj7cukiEpt2UhIM1wawzm6gCGr9isyUZC90Utn6m3TY2JtrG2IkybOUVI_0AAaw_pLNPzCFhca2D9VH12gWiM1h82jp987UW_imJpalLdzGR_xgDgEb_SBmU6aRqvhlCyOAN5-yW8hfNq8gMnwbT8W2xD257FieVMQVTRSsXDdh8G5yK5NOTl0fcN5pzfk-yRC88ZdhA-v97wOYfGqzrFnWAWKkplUZ_lJRT0K3bnT7yrV1nZGlNPEYsFEoAWWEOglm8IBdh3LiV64-oKh4EQBhE9tJJ4k_0uISsv--Qn60gPitbSnoyG3B_e8y-g2V4q4LnFUVyrMWvh2QtR0zJ0VP_0cF-4y7KbpTSbSO5rKcQtV-dwxd4swlaprvMUOYt0xxAf-us9dAifi-j28ciUrbNgPwzoseuhVMN0iY0edIVMzYv_Ilrf-uI9qLrkTyzDNIRGQ5LIZ4BrIfdz91lq2y7S6L1GFOoI2mCxpbNfyDik51C6gg0IYTvRLq24mjWv9_O5uPYzB_ZtOgO8adJhEb9dTxf4QsH9fy-0J1uLO_gobzsbX2h2ht2Eh-0Oi4e3ENFHu_5dIrEKwxG2_cvBUqqHYrIIRtfZNDbz7StSMKLhku4Hfc'
accountId = os.getenv('ACCOUNT_ID') or '0703ede8-fd4c-4ab1-bc25-c667664375d3'


async def test_meta_api_synchronization():
    api = MetaApi(token)
    try:
        account = await api.metatrader_account_api.get_account(accountId)
        initial_state = account.state
        deployed_states = ['DEPLOYING', 'DEPLOYED']

        if initial_state not in deployed_states:
            #  wait until account is deployed and connected to broker
            print('Deploying account')
            await account.deploy()

        print('Waiting for API server to connect to broker (may take couple of minutes)')
        await account.wait_connected()

        # connect to MetaApi API
        connection = account.get_rpc_connection()
        await connection.connect()

        # wait until terminal state synchronized to the local state
        print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
        await connection.wait_synchronized()

        # invoke RPC API (replace ticket numbers with actual ticket numbers which exist in your MT account)
       
        print('server time', await connection.get_server_time())

        # calculate margin required for trade
        print(
            'margin required for trade',
            await connection.calculate_margin(
                {'symbol': 'GBPUSD', 'type': 'ORDER_TYPE_BUY', 'volume': 0.1, 'openPrice': 1.1}
            ),
        )

        # trade
        print('Submitting pending order')
        try:
            result = await connection.create_limit_buy_order(
                'GBPUSD', 0.07, 1.0, 0.9, 2.0, {'comment': 'comm', 'clientId': 'TE_GBPUSD_7hyINWqAlE'}
            )
            print('Trade successful, result code is ' + result['stringCode'])
        except Exception as err:
            print('Trade failed with error:')
            print(api.format_error(err))
        if initial_state not in deployed_states:
            # undeploy account if it was undeployed
            print('Undeploying account')
            await connection.close()
            await account.undeploy()

    except Exception as err:
        print(api.format_error(err))
    exit()


asyncio.run(test_meta_api_synchronization())
