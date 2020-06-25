import sys
sys.path.append('latch_sdk_python')
import config.latch
import latch
api = latch.Latch(config.latch.appId, config.latch.secret)
token = input("Click \"Add Latch\" in the Latch app and give me your pairing code: ")
response = api.pair(token)
responseData = str(response.get_data())
while response.get_data()['accountId'] == None:
    response = api.pair(token)
    responseData = str(response.get_data())
    print('Error while pairing: ', response.get_error())
    print("Retrying...")
accountId = responseData[15:-2]
with open('config/accounts.txt', 'a') as f:
    f.write(accountId)
