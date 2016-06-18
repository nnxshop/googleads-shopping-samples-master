#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Updates the specified product on the specified account.

Uses the inventory collection. If you're updating any of the supported
properties in a product, be sure to use the inventory.set method
for performance reasons.
"""

import argparse
import sys

from apiclient import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'merchant_id',
    help='The ID of the merchant center.')
argparser.add_argument(
    'product_id',
    help='The ID of the product to update.')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'content', 'v2', __doc__, __file__, parents=[argparser])
  merchant_id = flags.merchant_id
  product_id = flags.product_id

  new_status = {
      'availability': 'out of stock',
      'price': {'value': 3.00, 'currency': 'USD'}}

  request = service.inventory().set(
      merchantId=merchant_id,
      storeCode=product_id.split(':')[0],
      productId=product_id,
      body=new_status)

  try:
    unused_result = request.execute()

    print 'Product with ID "%s" was updated.' % (product_id,)

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
