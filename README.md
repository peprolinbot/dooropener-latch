# dooropener-latch
Opens a door(actions a relay on a RPI) with Latch(https://latch.elevenpaths.com) when someones unlocks the latch.
This is made with python3 and latch's SDK for python.
That's practically everything.
## Setup
For setting up you need a Latch's developer account create it on it's webpage.
Now create an application with the "Block after conuslting" option in mandatory.
Copy your appId and secret into their respectives strings in the file config/latch.py, create it if it doesn't exist.
For adding or removing accounts use the accountAdder script. I suggest you to disable notifications for this service in the app once you add it if you don't want a notification per second ;)
For starting the service and wait for someone to unlock this latch run main.py
