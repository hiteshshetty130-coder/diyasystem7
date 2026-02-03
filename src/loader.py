import pandas as pd
import logging

logging.basicConfig(level=logging.INFO,filename="logs/billing.log",filemode="w")

#load and create data frame from subscription and usage data
def subscription_loader(file_path):
    try:
        subscription_data=pd.read_csv(file_path)
        return subscription_data
    
    except Exception:
        logging.warning(f"failed to load the subscription file!!")
        return pd.DataFrame()
    
def usage_loader(file_path2):
    try:
        usage_data=pd.read_csv(file_path2)
        return usage_data
    
    except Exception:
        logging.warning(f"failed to load the usage file!!")
        return pd.DataFrame()
    
