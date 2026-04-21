import pandas as pd
from database import get_conn, get_funnel

def conversion_rates():
    
    f = get_funnel()
    return {
        
        "sent_to_reply": round(f["replied"] / f["sent"] * 100, 1),
        "reply_to_call": round(f["call"] / f["replied"] * 100, 1),
        "call_to_closed": round(f["closed"] / f["call"] * 100, 1)
        
    }
    
def funnel_dataframe():
    
    f = get_funnel()
    return pd.DataFrame({
        
        "stage": ["Enviadas", "Responderam", "Call", "Fechado"],
        "count": [f["sent"], f["replied"], f["call"], f["closed"]]
            
    })