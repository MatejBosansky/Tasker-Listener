
# Tasker Listener
Simple Python project to emulate Windows media keys with Samsung S-Pen air gestures using Tasker. Anyway Tasks can be triggered via any Taskers event. Except emulating of keystrokes, Python programming language offers you to perform infinite amount of actions.
### Demonstration
https://youtu.be/-IYYRy5awp0

## How it works
Tasker on event trigger sends HTTP Post request to defined IP address and Port on internal network. On your Windows/Mac/Linux... machine must run Python script to listen HTTP requests and process them. Except Tasker, no additional application or service is needed.


## Important notes
- Only Python library to install is `pynput`
- [Recommending to set static IP  on machine you want to control](https://portforward.com/networking/static-ip-windows-10.htm)
- Works only with devices connected via internal network
- In Tasker profile redefine target IP address of your machine for all Tasks
