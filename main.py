import sys
sys.path.append('latch_sdk_python')
import config.latch
import latch
api = latch.Latch(config.latch.appId, config.latch.secret)
with open('config/accounts.txt', 'r') as f:
    account_ids = f.readlines()
for id in account_ids:
    response = api.status(id)
    responseData = str(response.get_data())
    print(responseData)