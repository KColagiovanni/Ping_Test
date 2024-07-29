# Router first three oclets
ipaddr_first3 = '192.168.0.'

# Network devices of interest
devices = {
    'Router': {'ip': 1, 'status': '', 'latency': ''},
    'Temp-Master': {'ip': 150, 'status': '', 'latency': ''},
    'K-Side': {'ip': 22, 'status': '', 'latency': ''},
    'Big Light': {'ip': 23, 'status': '', 'latency': ''},
    'Small Light': {'ip': 24, 'status': '', 'latency': ''},
    'J-Side': {'ip': 26, 'status': '', 'latency': ''},
    'RPi3': {'ip': 91, 'status': '', 'latency': ''},
    'RPi-Zero': {'ip': 221, 'status': '', 'latency': ''},
    'HomeAssistant': {'ip': 37, 'status': '', 'latency': ''},
    'TrueNAS': {'ip': 174, 'status': '', 'latency': ''},
    'RP5180': {'ip': 55, 'status': '', 'latency': ''},
}

# Check every ip address connected to the router
# devices = {}
#
# for i in range(1, 255):
#     if i == 1:
#         devices.update({f'Router': {'ip': i, 'status': '', 'latency': ''}})
#     else:
#         devices.update({f'device_{i}': {'ip': i, 'status': '', 'latency': ''}})
