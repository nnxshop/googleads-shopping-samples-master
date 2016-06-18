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

"""Updates the specified datafeed on the specified account."""

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
    'datafeed_id',
    help='The ID of the datafeed to update.')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'content', 'v2', __doc__, __file__, parents=[argparser])
  merchant_id = flags.merchant_id
  datafeed_id = flags.datafeed_id

  try:
    # Changing the scheduled fetch time to 7:00.
    request = service.datafeeds().patch(merchantId=merchant_id,
                                        datafeedId=datafeed_id,
                                        body={'fetchSchedule': {'hour': 7}})

    result = request.execute()
    print ('Datafeed with ID "%s" and fetchSchedule %s was updated.' %
           (result['id'], str(result['fetchSchedule'])))

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)
