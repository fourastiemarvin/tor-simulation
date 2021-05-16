# Simulation of an instant messaging service on Tor

## How to run it ?
The code works with Python 3. To install the required packages, run the following command:
```
pip3 install -r requirements.txt
```

When the requirements are installed, you have to run these commands on two terminal windows to launch the Alice's and Bob's hidden service:
```
python3 runAlice.py
python3 runBob.py
```
**NOTE:** depending of your installation you may need to use ```pip``` and ```python``` instead ```pip3``` and ```python3```

The servers are now running on your localhost. To connect them, enter the port that Alice and Bob need to connect to chat with each other.
Once this is done, you can simulate an anonymous chat between Alice and Bob by typing the messages in the terminal!
