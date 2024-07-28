import concurrent.futures
import subprocess
import time

ipaddr_first3 = '192.168.0.'
num_of_pings = 4
time_between_pings = 0.1
LINE_WIDTH = 58

devices = {
    'Router': {'ip': '1', 'status': '', 'latency': ''},
    'ESP32-1': {'ip': '22', 'status': '', 'latency': ''},
    'ESP32-2': {'ip': '23', 'status': '', 'latency': ''},
    'ESP32-Master Bed': {'ip': '24', 'status': '', 'latency': ''},
    'ESP32-4': {'ip': '26', 'status': '', 'latency': ''},
    'RPi3': {'ip': '91', 'status': '', 'latency': ''},
    'RPi-Zero': {'ip': '221', 'status': '', 'latency': ''},
    'HomeAssistant': {'ip': '37', 'status': '', 'latency': ''},
    'TrueNAS': {'ip': '174', 'status': '', 'latency': ''},
    'RP5180': {'ip': '55', 'status': '', 'latency': ''},
}


def horizontal_line(width):
    """
    This function simply prints a horizontal line of the defined width.

    Parameters:
        width(int): The width of the line.

    Returns: None
    """

    print('-' * width)


def check_network(device_name, ip):
    """
    This function send the ping command to the OS and then gets the output and used string manipulation to get the
    desired data from the string.

    Parameters:
        device_name(str): The device name that is being checked.
        ip(int): The last oclet in the IP Address being checked.

    Returns: None
    """

    # Complete IP Address
    ipaddr = ipaddr_first3 + str(ip)

    # Linux CMD ping command
    cmd = ['ping', ipaddr, f'-c {num_of_pings}', f'-i {time_between_pings}', '-q']

    # Subprocess command to send the cmd command to the OS
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Get the cmd result and save it to variables
    o, e = proc.communicate()

    # The expected output is something like: 4 packets transmitted, 4 received, 0% packet loss, time 303ms
    output = o.decode('ascii')

    # Get the index of the word "received" and add 10, which as can be seen in the expected output above, the % loss
    # value.
    percent_loss_start_index = output.find('received') + 10
    percent_loss_end_index = output.find('%')
    latency_index = output.find('ms')
    device_latency = str(f'{output[latency_index - 3:latency_index]}ms')

    # Error codes are stored in this variable.
    error = e.decode('ascii')

    # A return code of 0 mean the command has no errors, a return code > 0 indicates errors were encountered.
    rtn_code = str(proc.returncode)

    # Check if the percent loss and the return code are both 0, and the error variable is nothing.
    if output[percent_loss_start_index:percent_loss_end_index] == '0' and rtn_code == '0' and error == '':
        devices[device_name]['status'] = 'Online'
        devices[device_name]['latency'] = device_latency
        return ipaddr
    else:
        devices[device_name]['status'] = 'Offline'
        devices[device_name]['latency'] = '#' * 5


# Define a start time for the process.
start_time = time.time()

print('Checking Connections...')
with concurrent.futures.ThreadPoolExecutor(max_workers=500) as ex:
    for x, obj in devices.items():
        for y in obj:
            if y == 'ip':
                ex.submit(check_network, x, obj[y])

# Define an end time for the process.
end_time = time.time()

# Formatted output
horizontal_line(LINE_WIDTH)
print('|',
      'Status of Devices'.center(54),
      '|')
horizontal_line(LINE_WIDTH)
print('| Device Name'.ljust(20),
      '| Status'.ljust(9),
      '| Latency'.ljust(9),
      '| IP Address'.ljust(15),
      '|')
horizontal_line(LINE_WIDTH)
for name, online in devices.items():
    print(f'| {name}'.ljust(20),
          f'| {online["status"]}'.ljust(9),
          f'| {online["latency"]}'.ljust(9),
          f'| {ipaddr_first3}{online["ip"]}'.ljust(15),
          f'|')
horizontal_line(LINE_WIDTH)
print('|',
      f'The time of execution is: {round((end_time-start_time), 2)} seconds'.center(54),
      '|')
horizontal_line(LINE_WIDTH)
