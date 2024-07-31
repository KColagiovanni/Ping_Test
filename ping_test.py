import concurrent.futures
import subprocess
import time
import device_data

ipaddr_first3 = device_data.ipaddr_first3
devices = device_data.devices

NUM_OF_PINGS = 4
TIME_BETWEEN_PINGS = .5  # Seconds (Note: 1 second is 1000ms and 0.5 seconds is 500ms)

LINE_WIDTH = 61
CENTER_WIDTH = LINE_WIDTH - 4
LEFT_JUSTIFT_NAME = 20
LEFT_JUSTIFY_STATUS = 9
LEFT_JUSTIFY_LATENCY = 12
LEFT_JUSTIFY_IP = 15

def horizontal_line(width):
    """
    This function simply prints a horizontal line of the defined width.

    Parameters:
        width(int): The width of the line.

    Returns: None
    """

    print('-' * width)


def check_network(device_dict_object):
    """
    This function send the ping command to the OS and then gets the output and used string manipulation to get the
    desired data from the string.

    Parameters:
        device_dict_object(dictionary): The dictionary device object that is being checked.

    Returns: None
    """

    # Complete IP Address
    ipaddr = f'{ipaddr_first3}{device_dict_object["ip"]}'

    # Linux CMD ping command
    cmd = ['ping', ipaddr, f'-c {NUM_OF_PINGS}', f'-i {TIME_BETWEEN_PINGS}', '-q']

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
    find_avg_latency1 = output.find('=')
    start_index = output[find_avg_latency1:].find("/") + 1
    end_index = output[find_avg_latency1:].find("/", output[find_avg_latency1:].find("/") + 1)
    device_latency = str(f'{output[find_avg_latency1:][start_index:end_index]}ms')

    # Error codes are stored in this variable.
    error = e.decode('ascii')

    # A return code of 0 mean the command has no errors, a return code > 0 indicates errors were encountered.
    return_code = str(proc.returncode)

    # # Check if the percent loss and the return code are both 0, and the error variable is nothing.
    if output[percent_loss_start_index:percent_loss_end_index] == '0' and return_code == '0' and error == '':
        device_dict_object['status'] = 'Online'
        device_dict_object['latency'] = device_latency
    else:
        device_dict_object['status'] = 'Offline'
        device_dict_object['latency'] = '#' * 10


def thread_pool_executer(device_dict):
    """
    This function that uses a pool of at most max_workers threads to execute ping calls asynchronously.

    Parameters:
        device_dict(dictionary): A dictionary that holds the data for the network information.

    Returns:
        execution_time(float): The time, in milliseconds that it took to check all device connections.
    """

    # Define a start time for the process.
    start_time = time.time()

    print('Checking Connections...')
    with concurrent.futures.ThreadPoolExecutor(max_workers=255) as ex:
        for x, obj in device_dict.items():
            ex.submit(check_network, obj)

    # Define an end time for the process.
    end_time = time.time()

    return round((end_time-start_time), 2)

def print_output(device_dict, execution_time):

    up_count = 0
    # Formatted output
    horizontal_line(LINE_WIDTH)
    print('|',
          'Status of Devices'.center(CENTER_WIDTH),
          '|')
    horizontal_line(LINE_WIDTH)
    print('| Device Name'.ljust(LEFT_JUSTIFT_NAME),
          '| Status'.ljust(LEFT_JUSTIFY_STATUS),
          '| Latency'.ljust(LEFT_JUSTIFY_LATENCY),
          '| IP Address'.ljust(LEFT_JUSTIFY_IP),
          '|')
    horizontal_line(LINE_WIDTH)
    for name, online in device_dict.items():
        if online["status"] == 'Online':
            up_count += 1

        # When this print statement is outside of the if statement it will display all devices, online of offline,
        # if it is inside of the if statement, it will only show devices that are online.
        print(f'| {name}'.ljust(LEFT_JUSTIFT_NAME),
              f'| {online["status"]}'.ljust(LEFT_JUSTIFY_STATUS),
              f'| {online["latency"]}'.ljust(LEFT_JUSTIFY_LATENCY),
              f'| {ipaddr_first3}{online["ip"]}'.ljust(LEFT_JUSTIFY_IP),
              f'|')
    horizontal_line(LINE_WIDTH)
    print('|',
          f'Execution Time: {execution_time} seconds | Devices Online: {up_count}'.center(CENTER_WIDTH),
          '|')
    horizontal_line(LINE_WIDTH)


def main():

    execution_time = thread_pool_executer(devices)
    print_output(devices, execution_time)


if main() == '__name__':
    main()