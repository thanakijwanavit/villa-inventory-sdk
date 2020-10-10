# villaInventorySdk
> read and write inventory in real time


## Install

`pip install villaInventorySdk`

## How to use

Uploading a large amount of data

## sample input

```python
input = [
    {'ib_brcode': '1023',
     'ib_cf_qty': '835',
     'ib_prcode': '84621',
     'new_ib_vs_stock_cv': '839'},
    {'ib_brcode': '1022',
     'ib_cf_qty': '24',
     'ib_prcode': '12424',
     'new_ib_vs_stock_cv': '21'}
]
```

## Upload data

```python
@timeit
def upload(input):
  print(f'uploading {len(input)} items')
  sdk = InventorySdk(user=USER, pw=PW)
  return sdk.updateWithS3(
      input,
      inputBucketName= inputBucketName, 
      functionName= functionName,
      invocationType = invocationType
    )

json.loads(json.loads(upload(input)['Payload'].read()))
```

    uploading 2 items
    data was saved to s3
    data is saved to s3, invoking ingestion function
    input to lambda is {'inputBucketName': 'input-bucket-dev-manual', 'inputKeyName': 'input-data-name'}
    'upload' took 1014.23 ms





    {'statusCode': 200,
     'result': {'success': 2, 'failure': 0, 'failureMessage': [], 'timeTaken': 0}}



## Query single product

```python
import json
sdk = InventorySdk(user=USER, pw=PW)
result = sdk.querySingleProduct(ib_prcode = '84621')
inventory = json.loads(result)['inventory']
json.loads(inventory)
```




    {'ib_prcode': '84621',
     '1023': {'ib_cf_qty': 835,
      'new_ib_bs_stock_cv': 839,
      'lastUpdate': 1601548526.868942},
     'lastUpdate': 1601548526.868942}


