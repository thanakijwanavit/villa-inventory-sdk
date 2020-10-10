# AUTOGENERATED! DO NOT EDIT! File to edit: inventory.ipynb (unless otherwise specified).

__all__ = ['Endpoints', 'InventorySdk']

# Cell
from json.decoder import JSONDecodeError
from botocore.config import Config
from s3bz.s3bz import S3, Requests
from lambdasdk.lambdasdk import Lambda
from awsSchema.apigateway import Event, Response
import bz2, json, boto3, base64, logging

# Cell
class Endpoints:
  '''get endpoint names from branch name'''
  def __init__(self, branchName='manual-dev'):
    self.branchName = branchName
  updateWithS3 = lambda self: f'update-inventory-s3-{self.branchName}'
  inputS3 = lambda self: f'input-bucket-{self.branchName}'
  querySingleProduct = lambda self: f'single-product-query-{self.branchName}'


class InventorySdk:
  ''' interact with villa inventory database '''
  def __init__(self, branchName = 'dev', user = None, pw = None,
               region = 'ap-southeast-1'):
    self.branchName = branchName
    self.lambdaClient = Lambda(user =user, pw=pw, region = region)
    self.user = user; self.pw = pw; self.region = region
    self.endpoint = Endpoints(branchName=branchName)


  def updateWithS3(self, data:dict,
                   key:str = 'allProducts',
                   invocationType:str = 'Event'):

    # save to s3
    S3.save(key = key,
            objectToSave = data ,
            bucket = self.endpoint.inputS3(),
            user=self.user, pw=self.pw)
    logging.info(f'saving to s3 completed')

    lambdaPayload = {
        'inputBucketName': self.endpoint.inputS3(),
        'inputKeyName': key
    }
    logging.info(f'input to lambda is {lambdaPayload}')
    try:
      result = self.lambdaClient.invoke(functionName= self.endpoint.updateWithS3() ,input=lambdaPayload,
                                    invocationType= invocationType )
      if result: return Response.getReturn(result)
    except JSONDecodeError:
      logging.warning('no return from function')
      return True

  def querySingleProduct(self, functionName='single-product-query-dev-manual',
                         ib_prcode= None, user=None, pw=None):
    '''query a single product'''
    input = { 'ib_prcode': ib_prcode }
    return self.lambdaClient.invoke(
        functionName = functionName, input = input )['Payload'].read()
