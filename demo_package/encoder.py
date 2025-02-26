import pandas as pd
from demo_package.exceptions import OneHotEncodingError
from demo_package.logger import logger 

def one_hot_encode(df: pd.DataFrame, column: str) -> pd.DataFrame:
    try:
        if column not in df.columns:
            raise OneHotEncodingError(f"Column '{column}' not found in DataFrame")
        
        encoded_df = pd.get_dummies(df, columns=[column], drop_first=True)
        #encoded_df = encoded_df.astype(int)
        logger.info(f"Successfully one-hot encoded column: {column}")
        return encoded_df

        
    except OneHotEncodingError as e:
        logger.error(f"OneHotEncodingError: {e.message}")


