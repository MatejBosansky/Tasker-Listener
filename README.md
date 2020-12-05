
# Tasker Listener
Simple Python project to emulate media key press on Windows/Mac/Linux... machine with Samsung S-Pen air gestures using Tasker. Anyway tasks can be triggered via any Taskers event. Except emulating of keystrokes, Python programming language offers you to perform infinite amount of actions.
### Demonstration
https://youtu.be/-IYYRy5awp0

## How it works
Tasker on event trigger sends HTTP POST request to defined IP address and port on internal network. On your Windows/Mac/Linux... machine must run Python script to listen HTTP requests and process them. Except Tasker and Python script, no additional application or service is needed.


## Important notes
- Only Python library to install is `pynput`
- [Recommending to set static IP  on machine you want to control](https://portforward.com/networking/static-ip-windows-10.htm)
- Works only with devices connected via internal network
- In Tasker profile redefine target IP address of your machine for all tasks
- Tasker profile included in repo
