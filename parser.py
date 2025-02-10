import re

def extract_trade_info(text):
    trade_info = {}
    
    # Extract direction (BUY/SELL) and asset (e.g., GOLD)
    direction_match = re.search(r'(BUY|SELL)', text, re.IGNORECASE)
    if direction_match:
        trade_info['Direction'] = direction_match.group().upper()
    
    # Extract SL (Stop Loss)
    sl_match = re.search(r'SL\s*(\d+\.?\d*)', text, re.IGNORECASE)
    if sl_match:
        trade_info['SL'] = float(sl_match.group(1))
    
    # Extract TP levels (Take Profit)
    tp_matches = re.findall(r'TP\d*[:\s]*(\d+\.?\d*)', text, re.IGNORECASE)
    if tp_matches:
        trade_info['TPs'] = [float(tp) for tp in tp_matches]
    
    # Extract price range
    range_match = re.search(r'@?(\d+\.?\d*)-(\d+\.?\d*)', text)
    if range_match:
        trade_info['Entry'] = [float(range_match.group(1)), float(range_match.group(2))]
    
    return trade_info