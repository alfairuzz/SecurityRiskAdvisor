import pandas as pd



def read_asset_inventory(file):
    
    try:
        df = pd.read_excel(file)
    except:
        df = pd.read_csv(file)
    else:
        print("[Info] Encountered issues reading asset inventory file.")
    
    return df

