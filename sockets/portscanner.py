import socket
import argparse
import ipaddress as ipChecker
import threading


threadLock = threading.Semaphore(value=1)
stop_scan = False


base = argparse.ArgumentParser(prog="Port Scanner", description="Simple python made port scanner.")
port_group = base.add_mutually_exclusive_group(required=False)
ip_group = base.add_mutually_exclusive_group(required=True)

ip_group.add_argument('-t', action='store', type=str, nargs=1, help="Target ip")
ip_group.add_argument('-T', action='store', type=str, nargs=1, help="Target dns")

port_group.add_argument('-p', action='store', nargs='+', help="Port, or list of ports to scan")
port_group.add_argument('-P', action='store', nargs=2, help="Range of Ports to scan")


options = base.parse_args()

def PortScan(target, port):

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    threadLock.acquire()
    try:
        tcp_socket.connect((target, port))
        tcp_socket.send('Random data'.encode('utf-8'))
        tcp_socket.settimeout(0.5)
        rslt = tcp_socket.recv(1024).decode('utf-8')
        print(f"{port}/tcp opened. Service: {rslt}")

    except socket.timeout:
        print(f"{port}/tcp opened. Service Unknown")
    except Exception:
        pass
    finally:
        tcp_socket.close()
        threadLock.release()

def Thread_Scan(target, ports):
    Host_Availability(target)
    thread_list = []
    if stop_scan:
        return
    for port in ports:
        thread = threading.Thread(target=PortScan, args=(target, port))
        thread.start()
        thread_list.append(thread)

    for each_thread in thread_list:
        each_thread.join()


def Host_Availability(target):
    global stop_scan
    test_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        test_sock.connect((target, 8080))
    except OSError as e:
        if e.errno == 113:
            print("[---] Target not found.")
            stop_scan = True
    finally:
        test_sock.close()


if options.t:
    try:
        ipChecker.IPv4Address(options.t[0])
        target = options.t[0]
    except:
        print("[---] Ip address is not a valid IPv4 address.")
elif options.T:
    try:
        target = socket.gethostbyaddr(options.T[0])
        target = target[2][0]
    except:
        print("[---] Host name unknown. Ensure the hostname is accurate.")

if options.p:
    ports = []
    for i in options.p:
        ports.append(int(i))

elif options.P:
    ports = []
    first = int(options.P[0])
    last = int(options.P[1])
    for i in range(first, last+1):
        ports.append(i)



if __name__ == "__main__":
    Thread_Scan(target, ports)