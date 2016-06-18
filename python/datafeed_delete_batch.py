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

"""Deletes several datafeeds from the specified account, in a single batch."""

import argparse
import sys

from apiclient import sample_tools
from apiclient.http import BatchHttpRequest
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'merchant_id',
    help='The ID of the merchant center.')
argparser.add_argument(
    'datafeed_ids', nargs='*',
    help='The IDs of the datafeeds to delete.')


def datafeed_deleted(unused_request_id, unused_response, exception):
  if exception is not None:
    # Do something with the exception.
    print 'There was an error: ' + str(exception)
  else:
    print 'Datafeed was deleted.'


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'content', 'v2', __doc__, __file__, parents=[argparser])
  merchant_id = flags.merchant_id
  datafeed_ids = flags.datafeed_ids

  batch = BatchHttpRequest(callback=datafeed_deleted)

  for datafeed_id in datafeed_ids:
    # Add datafeed deletion to the batch.
    batch.add(service.datafeeds().delete(merchantId=merchant_id,
                                         datafeedId=datafeed_id))
  try:
    batch.execute()
  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
