mkdir config
echo $'appId = "Enter your App Id here with the quotes"\nsecret = "Enter your secret here with the quotes"' > config/latch.py
touch config/accounts.txt
touch config/accountsEmails.txt
git clone https://github.com/ElevenPaths/latch-sdk-python.git latch_sdk_python
