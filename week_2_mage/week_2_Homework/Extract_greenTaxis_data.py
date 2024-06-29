import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    
    url_2019_10 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz'
    url_2019_11 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz'
    url_2019_12 = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    data_dtypes = {
    'VendorID': pd.Int64Dtype(),
    'passenger_count': pd.Int64Dtype(),
    'trip_distance': 'float',
    'RatecodeID': pd.Int64Dtype(),
    'store_and_fwd_flag': str,
    'PULocationID': pd.Int64Dtype(),
    'DOLocationID': pd.Int64Dtype(),
    'payment_type': pd.Int64Dtype(),
    'fare_amount': 'float',
    'extra': 'float',
    'mta_tax': 'float',
    'tip_amount': 'float',
    'tolls_amount': 'float',
    'improvement_surcharge': 'float',
    'total_amount': 'float',
    'congestion_surcharge':'float'}

    parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']

    df_2019_10 = pd.read_csv(url_2019_10, sep = ",", compression = "gzip", dtype = data_dtypes, parse_dates = parse_dates)
    df_2019_11 = pd.read_csv(url_2019_11, sep = ",", compression = "gzip", dtype = data_dtypes, parse_dates = parse_dates)
    df_2019_12 = pd.read_csv(url_2019_12, sep = ",", compression = "gzip", dtype = data_dtypes, parse_dates = parse_dates)
    
    df_QR_2019 = pd.concat([df_2019_10,df_2019_11,df_2019_12])
    return df_QR_2019


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
