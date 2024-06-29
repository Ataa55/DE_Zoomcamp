import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = data
    df = df[(df["passenger_count"] > 0) & (df["trip_distance"] > 0)]
    df = df.rename(columns = {"RatecodeID":"ratecode_id","PULocationID":"pulocation_id","DOLocationID":"dolocation_id"})
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date

    print(df)
    return df

@test
def test_passenger_count(output, *args):
    """
    Template code for testing the output of the block.
    """
    assert output["passenger_count"].isin([0]).sum() == 0, "passenger count sholud be greater than 0"

def test_trip_distance(output, *args):
    """
    Template code for testing the output of the block.
    """
    assert output["trip_distance"].isin([0]).sum() == 0, "trip_distance sholud be greater than 0"
            
def test_vendor_id(output, *args):
    """
    Template code for testing the output of the block.
    """
    assert output["VendorID"] in output.columns, "VendorID sholud be in the columns"
    

