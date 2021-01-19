# villaInventorySdk



## Install

`pip install villaInventorySdk`

## How to use

Uploading a large amount of data

## sample input

```
sampleInput = [ 
  {'ib_brcode': '1023', 'ib_cf_qty': '835', 'ib_prcode': '84621', 'new_ib_vs_stock_cv': '839'},
  {'ib_brcode': '1022', 'ib_cf_qty': '24', 'ib_prcode': '12424', 'new_ib_vs_stock_cv': '21'}
]
```

## Upload data

## init sdk

```
%%time
sdk = InventorySdk(user=USER, pw=PW, branchName = branch)
```

    CPU times: user 36.6 ms, sys: 4.73 ms, total: 41.3 ms
    Wall time: 1.05 s


## Update inventory 

```
%%time
sdk.updateWithS3( sampleInput )
```

    CPU times: user 53.4 ms, sys: 2.56 ms, total: 55.9 ms
    Wall time: 322 ms





    {'body': 'true', 'statusCode': 200, 'header': {}}



## Query single product

```
%%time
sdk.querySingleProduct('0000002')
```

    CPU times: user 6.71 ms, sys: 7.73 ms, total: 14.4 ms
    Wall time: 83.5 ms





    {'ib_prcode': '0000002',
     '1000': {'ib_cf_qty': 35,
      'new_ib_bs_stock_cv': 33,
      'lastUpdate': 1600567810.529301,
      'ib_prcode': '0000002',
      'ib_brcode': '1000'},
     '1001': {'ib_cf_qty': 32,
      'new_ib_bs_stock_cv': 30,
      'lastUpdate': 1600567810.529316,
      'ib_prcode': '0000002',
      'ib_brcode': '1001'},
     '1002': {'ib_cf_qty': 34,
      'new_ib_bs_stock_cv': 30,
      'lastUpdate': 1600567810.529318,
      'ib_prcode': '0000002',
      'ib_brcode': '1002'},
     'lastUpdate': 1600567810.529318}



## Query Branch

```
%%time
result = sdk.queryBranch('1000')
#showing the first 2 result
list(iter(result.items()))[:2]
```

    CPU times: user 360 ms, sys: 28.1 ms, total: 388 ms
    Wall time: 600 ms





    [('0000009',
      {'ib_cf_qty': 50,
       'new_ib_bs_stock_cv': 27,
       'lastUpdate': 1602338504.869655,
       'ib_prcode': '0000009',
       'ib_brcode': '1000'}),
     ('0000002',
      {'ib_cf_qty': 35,
       'new_ib_bs_stock_cv': 33,
       'lastUpdate': 1600567810.529301,
       'ib_prcode': '0000002',
       'ib_brcode': '1000'})]



## Query All

```
%%time
result = sdk.queryAll()
list(iter(result.items()))[:2]
```

    CPU times: user 2.34 s, sys: 90.4 ms, total: 2.43 s
    Wall time: 2.77 s





    [('0000009',
      {'ib_prcode': '0000009',
       '1000': {'ib_cf_qty': 50,
        'new_ib_bs_stock_cv': 27,
        'lastUpdate': 1602338504.869655,
        'ib_prcode': '0000009',
        'ib_brcode': '1000'},
       'lastUpdate': 1602338504.869655}),
     ('0000002',
      {'ib_prcode': '0000002',
       '1000': {'ib_cf_qty': 35,
        'new_ib_bs_stock_cv': 33,
        'lastUpdate': 1600567810.529301,
        'ib_prcode': '0000002',
        'ib_brcode': '1000'},
       '1001': {'ib_cf_qty': 32,
        'new_ib_bs_stock_cv': 30,
        'lastUpdate': 1600567810.529316,
        'ib_prcode': '0000002',
        'ib_brcode': '1001'},
       '1002': {'ib_cf_qty': 34,
        'new_ib_bs_stock_cv': 30,
        'lastUpdate': 1600567810.529318,
        'ib_prcode': '0000002',
        'ib_brcode': '1002'},
       'lastUpdate': 1600567810.529318})]


