#!/usr/bin/env python
import json
import duo_client

import pprint

ikey= "DXXX"
skey= "mxxx"
host= "api-XXX.duosecurity.com"

accounts=duo_client.Accounts(ikey, skey, host)
account_info=accounts.get_child_accounts()
pprint.pprint(account_info)
