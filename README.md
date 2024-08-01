# Check Network Devices

## Description
This is a simple program that will check either all IP addresses on your network, or a
list of specific devices. The program can be configured a few different ways. It can show
all IP addresses on a defined network or it can show a predefined list of newwork devices.
It can also be configured to shoe only devices that are online, or both online and offline. 
If displaying all IP addresses, it will show the status "online" or "offline", the latency 
(time from the machine running the program to the router to the device), and the IP address 
of the device. If displaying a list of predefined known devices, it will show everthing 
previously mentioned, in addition to the device name.

## Requirements
- Python 3.11
- A PC. This program was written and tested using a Linux OS. It may work as is on MacOS. If using Windows, certain things may need to be modified. 

## Cost
Free

## How to Install

1. If it’s not already installed on the PC, download [Python 3.11](https://www.python.org/downloads/release/python-3119/)(The application should work with Python versions 3.8 or higher, but it was built, tested, and only guaranteed to work correctly using Python version 3.11)

Install Python, after a successful installation, continue to the next step.

   - [Install Python on Windows](https://www.geeksforgeeks.org/how-to-install-python-on-windows/)
   - [Install Python on Linux](https://www.geeksforgeeks.org/how-to-install-python-on-linux/)
   - [Install Python on Mac OS](https://docs.python.org/3/using/mac.html)

> [!Tip]
>  - In Windows OS, a command prompt window can be opened by pressing the windows key and typing `cmd`.
>  - In Lunux OS, a command prompt window can be opened by pressing Ctrl + Alt + t.
>  - I Mac OS, a command promt window can be opened by pressing {Comming Soon}.

3. In a command prompt window type: `python –version` or `python3 –version`  to ensure Python version 3.11 is installed and configured.

### How to Use
1. Clone this project to any directory and make note of the path to it.
2. In a command prompt window, navigate to the directory where the project was cloned and go into that directory.
3. In a command prompt type `dir`(windows) or `ls`(unix), and verify that the “ping_test.py”, and “device_data.py” files are there, if either of those files are not present, go back to step 1.
4. If typing `python –version` in the command prompt window displays `Python 3.11.X`, continue to step 4a. If typing `python3 –version` in the command prompt window displays `Python 3.11.X`, continue to step 4b.
    - a. In a command prompt window, type: “python ping_test.py” and ensure the application starts. It should indicate that it is checking connections.
    - b. In a command prompt window, type: “python3 ping_test.py” and ensure the application starts. It should indicate that it is checking connections.
5. Once the application is running simmply wait for the results to be returned.
6. There are a few parameters that can be adjusted to modify the program.
  - In the `device_data.py` file, on lines 5 through 27 there is a 2d dictionery named "devices". This dictionary is used to store specific data for your network. If only seeing the results for certain devices is
    desired, use this method. Only the device name and the last oclet of the devices IP address need to be used when entering a new device. The rest of the code below the dictonary should be commented out if using 
    this method.
  - In the `device_data.py` file, on lines22 through 28, is a loop that populates an empty dictionary with all possible Ipv4 IP addresses on the defined network.If seeing results for all IP addresses on the network
    is desired, use this method. The code for the devices dictionary, on lines 5 through 27 should be commented out if using this method.
  - In the `ping_test.py` file, on lines 124 through 130, the code should be outside of the if statement (same indentation as the `if` statement) if the results for all devices, online and offline, want to be seen.
    If only online devices want to be seen in the results, indent the code on lines 124 through 130 to be inside the if statement (same indentation as the code under the `if` statement).
  - In the `device_data.py` file, on line 2, the `ipaddr_first3` variable can be changed to suit the network being checked, default is `192.168.0`.
  - In the `ping_test.py` file, on line 9, the `NUM_OF_PINGS` variable can be changed to adjust the number of times each ip address is pinged. The more times each IP address is pinged, the better the chance is that the device will be seen if it is online, but it will make the exection time longer. Default is 4. 
  - In the `ping_test.py` file, on line 9, the `TIME_BETWEEN_PINGS` variable can be changed to adjust the time(in seconds) between when each ping is sent. The higher the number is, the longer the time of execution will be. The OS will limit the minimum interval allowed between ping commands, to avoid flooding the network. The minimum interval depends on the OS, user privledges, and the network settings. If this vlue is set too low, all the devices will appear to be offline falsely. The execution tiem between 500ms, 100ms, and 10ms is the dame. The execution time between 1000ms and 500ms is about 3 seconds. Default is 500 ms(0.5 seconds).  

## Visualizations
Coming soon

## Credits/Resources
Coming soon
