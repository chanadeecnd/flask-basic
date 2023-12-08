import socket


def get_ip_address():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        print("Error to get ip address: ", e)
        return -1