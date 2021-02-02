# villaInventorySdk



full docs here https://thanakijwanavit.github.io/villa-inventory-sdk/

## Install

`pip install villaInventorySdk`

## How to use

Uploading a large amount of data

## sample input

```
from villaInventorySdk.inventory import InventorySdk
from random import randrange
import boto3, time, json
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from datetime import datetime
import pandas as pd
from nicHelper.dictUtil import printDict
```

```
sampleInput =  [ 
  { 'cprcode': '0000009', 'brcode': '1000', 'ib_cf_qty': '50', 'new_ib_vs_stock_cv': '27' },
  { 'cprcode': '0000004', 'brcode': '1000', 'ib_cf_qty': '35', 'new_ib_vs_stock_cv': '33' },
  { 'cprcode': '0000003', 'brcode': '1003', 'ib_cf_qty': '36', 'new_ib_vs_stock_cv': '33' }
    ]
df = pd.DataFrame(sampleInput)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cprcode</th>
      <th>brcode</th>
      <th>ib_cf_qty</th>
      <th>new_ib_vs_stock_cv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0000009</td>
      <td>1000</td>
      <td>50</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0000004</td>
      <td>1000</td>
      <td>35</td>
      <td>33</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0000003</td>
      <td>1003</td>
      <td>36</td>
      <td>33</td>
    </tr>
  </tbody>
</table>
</div>



## Upload data

## init sdk

```
%%time
USER=None
PW = None
sdk = InventorySdk(user=USER, pw=PW, branchName = branch)
```

    CPU times: user 36.2 ms, sys: 4.05 ms, total: 40.2 ms
    Wall time: 39.8 ms


## Update inventory 

```
%%time
key = 'test'
r = sdk.uploadDf(df, key = key)
if r.status_code >= 400: raise Exception(r.json())
sdk.ingestData(key = key)
```

    signed url is 
    url : https://in
    fields
     key : test
     AWSAccessKeyId : ASIAVX4Z5T
     x-amz-security-token : IQoJb3JpZ2
     policy : eyJleHBpcm
     signature : JhA/noZmLG
    CPU times: user 58.8 ms, sys: 1.44 ms, total: 60.2 ms
    Wall time: 574 ms





    {'body': '{"cprcode":{"0":"0000009","1":"0000004","2":"0000003"},"brcode":{"0":"1000","1":"1000","2":"1003"},"ib_cf_qty":{"0":"50","1":"35","2":"36"},"new_ib_vs_stock_cv":{"0":"27","1":"33","2":"33"}}',
     'statusCode': 200,
     'headers': {'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': '*'}}



#### test uploading full data 

```
#### test uploading real data 
df = pd.read_csv('sampleData/inventory.csv', index_col=0, dtype=str).reset_index(drop=True)
r = sdk.uploadDf(df, key = key)
if r.status_code >= 400: raise Exception(r.json())
sdk.ingestData(key = key)
```

    signed url is 
    url : https://in
    fields
     key : test
     AWSAccessKeyId : ASIAVX4Z5T
     x-amz-security-token : IQoJb3JpZ2
     policy : eyJleHBpcm
     signature : 7846JjbAR+





    {'body': '{"cprcode":{"0":"0000009","1":"0000012","2":"0000026","3":"0000028","4":"0000033"},"brcode":{"0":"1000","1":"1000","2":"1000","3":"1000","4":"1000"},"ib_cf_qty":{"0":"39","1":"39","2":"9","3":"13","4":"7"},"new_ib_vs_stock_cv":{"0":"39","1":"39","2":"9","3":"13","4":"7"}}',
     'statusCode': 200,
     'headers': {'Access-Control-Allow-Headers': '*',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': '*'}}



## Query single product

```
%%time
sdk.querySingleProduct2(cprcode='1234')
```

    succesfully get url, returning pandas
    CPU times: user 33.8 ms, sys: 9.14 ms, total: 42.9 ms
    Wall time: 3 s





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cprcode</th>
      <th>brcode</th>
      <th>ib_cf_qty</th>
      <th>new_ib_vs_stock_cv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1234</td>
      <td>test</td>
      <td>123</td>
      <td>123</td>
    </tr>
  </tbody>
</table>
</div>



## Query Branch

```
%%time
sdk.branchQuery(brcode='1000', cprcodes = [9])
```

    CPU times: user 15.3 ms, sys: 1.2 ms, total: 16.5 ms
    Wall time: 231 ms





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cprcode</th>
      <th>brcode</th>
      <th>ib_cf_qty</th>
      <th>new_ib_vs_stock_cv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9</td>
      <td>1000</td>
      <td>50</td>
      <td>27</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>1000</td>
      <td>50</td>
      <td>27</td>
    </tr>
  </tbody>
</table>
</div>



## Query All

```
%%time
sdk.queryAll2()
```

    succesfully get url, returning pandas
    CPU times: user 21.4 ms, sys: 15.7 ms, total: 37.1 ms
    Wall time: 420 ms





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cprcode</th>
      <th>brcode</th>
      <th>ib_cf_qty</th>
      <th>new_ib_vs_stock_cv</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1234</td>
      <td>test</td>
      <td>123</td>
      <td>123</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12345</td>
      <td>test</td>
      <td>345</td>
      <td>345</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1000</td>
      <td>35</td>
      <td>33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1000</td>
      <td>35</td>
      <td>33</td>
    </tr>
    <tr>
      <th>4</th>
      <td>9</td>
      <td>1000</td>
      <td>50</td>
      <td>27</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>46978</th>
      <td>244590</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46979</th>
      <td>244591</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46980</th>
      <td>244592</td>
      <td>1000</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>46981</th>
      <td>3</td>
      <td>1003</td>
      <td>36</td>
      <td>33</td>
    </tr>
    <tr>
      <th>46982</th>
      <td>3</td>
      <td>1003</td>
      <td>36</td>
      <td>33</td>
    </tr>
  </tbody>
</table>
<p>46983 rows × 4 columns</p>
</div>


