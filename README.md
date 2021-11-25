# Duo_MSSP examples

1. duo_mssp.py  
This script lists the Duo MSSP tenants.

More info:
https://duo.com/docs/accountsapi
Please create the Accounts API credentials as a 1st step.


Example output:

[{'account_id': 'DAXX1',  
  'api_hostname': 'api-demoxxx.duosecurity.com',  
  'name': 'Company A'},  
{'account_id': 'DAXX2',  
  'api_hostname': 'api-demoxxx.duosecurity.com',  
  'name': 'Company B'}]  

2. duo_mssp_create.py

This script creates a tenant in Duo MSSP environment.
1st argument is the name of the tenant, like:

python duo_mssp_create.py New_Tenant



