if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):

    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    data.columns = data.columns.str.replace('([a-z0-9])([A-Z])', r'\1_\2').str.lower()
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'

    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with zero trip distance'

    assert set(output['vendor_id'].unique()) == {1, 2}, "The 'vendor_id' column should contain only the distinct values [1, 2]"
