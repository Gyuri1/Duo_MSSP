#!/usr/bin/env python
import json
import duo_client
import sys
import pprint

ikey= "Dxxx"
skey= "xx"
host= "api-xx.duosecurity.com"


account_name=sys.argv[1]
print(account_name)
accounts=duo_client.Accounts(ikey, skey, host)
account_create_info=accounts.create_account(account_name)
print(account_create_info)