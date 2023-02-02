'''
from tecton import RequestSource, on_demand_feature_view
from tecton.types import Field, Float64, Int64

# Define the request schema
transaction_request = RequestSource(schema=[Field("amt", Float64)])

# Define the output schema
output_schema = [Field("transaction_amount_is_high", Int64)]

# This On-Demand Feature View evaluates a transaction amount and declares it as "high", if it's higher than 10,000
@on_demand_feature_view(
    sources=[transaction_request],
    mode='python',
    schema=output_schema,
    owner='matt@tecton.ai',
    tags={'release': 'production', 'prevent-destroy': 'true', 'prevent-recreate': 'true'},
    description='Whether the transaction amount is considered high (over $100)'
)

def transaction_amount_is_high(transaction_request):
    result = {}
    result['transaction_amount_is_high'] = int(transaction_request['amt'] >= 100)
    return result
'''