import math
import socket
import struct
import ipaddress


def get_mask(nb_machine):
    return 32 - math.ceil(math.log2(nb_machine))


def pgcd(ri, q):
    if ri < q:
        return 0
    return (ri // q) * q


def dec_mask(mask_length):
    mask = (1 << 32) - (1 << 32 >> mask_length)
    return socket.inet_ntoa(struct.pack(">L", mask))


def assignable_range(ip, mask):
    net4 = ipaddress.ip_network(f'{ip}/{mask}')
    hosts = list(net4.hosts())
    return hosts


def last_and_first_assignable_range(ip, mask):
    hosts = assignable_range(ip, mask)
    return f'{hosts[0]}-{hosts[-1]}'


def get_broadcast(ip, mask):
    net4 = ipaddress.ip_network(f'{ip}/{mask}')
    return str(net4.broadcast_address)


def ip_service(ip, mask):
    ip_service.ip = ip
    ip_service.mask = int(mask)

    ip_service.table = {
        32: 1,
        31: 2,
        30: 4,
        29: 8,
        28: 16,
        27: 32,
        26: 64,
        25: 128,
    }

    ip_service.sub_networks = {}

    def order_network():
        ip_service.sub_networks = dict(sorted(ip_service.sub_networks.items(), key=lambda item: item[1], reverse=True))

    ip_service.order_network = order_network

    def set_sub_network(sub_networks):
        ip_service.sub_networks = sub_networks
        ip_service.order_network()

    ip_service.set_sub_network = set_sub_network

    def get_next_network(ip_, mask_):
        i, q = ip_service.get_q(mask_)
        tab_ip = [int(i) for i in ip_.split(".")][::-1]

        while tab_ip[i] + q > 255:
            tab_ip[i] = 0
            i = i + 1
            q = 1
        tab_ip[i] = pgcd(tab_ip[i], q) + q
        tab_ip = [str(i) for i in tab_ip][::-1]
        return ".".join(tab_ip)

    ip_service.get_next_network = get_next_network

    def is_full(mask_):
        return ip_service.mask > mask_

    ip_service.is_full = is_full

    def get_q(mask__):
        i = 0
        while mask__ < 25:
            mask__ = mask__ + 8
            i = i + 1
        return i, ip_service.table.get(mask__)

    ip_service.get_q = get_q

    def get_base_mask():
        return dict(zip(ip_service.sub_networks.keys(),
                        list(map(get_mask, ip_service.sub_networks.values()))))

    ip_service.get_base_mask = get_base_mask

    def get_base_q_and_position():
        return dict(zip(ip_service.sub_networks.keys(),
                        list(map(ip_service.get_q, ip_service.get_base_mask().values()))))

    ip_service.get_base_q_and_position = get_base_q_and_position

    def sub_all_network():
        first = list(ip_service.sub_networks.values())[0]
        _mask = get_mask(first)

        if not ip_service.is_full(_mask):
            list_n = []
            base_ip = ip_service.ip
            for key, val in ip_service.get_base_mask().items():
                list_n.append({key: [base_ip, val]})
                base_ip = ip_service.get_next_network(base_ip, val)
            return list_n

    ip_service.sub_all_network = sub_all_network

    def get_address(name):
        return [k.get(name) for k in ip_service.sub_all_network() if name in k.keys()][0]

    ip_service.get_address = get_address

    def result():
        subnets = [[
            k,
            s,
            2 ** math.ceil(math.log2(s)),
            *ip_service.get_address(k),
            dec_mask(ip_service.get_base_mask().get(k)),
            last_and_first_assignable_range(*ip_service.get_address(k)),
            get_broadcast(*ip_service.get_address(k))
        ]
            for k, s in ip_service.sub_networks.items()]
        return subnets

    ip_service.result = result


if __name__ == '__main__':
    ip_service('172.16.0.0', 21)
    sub = {
        "ADMIN": 400,
        "GUEST": 200,
        "IMP": 300,
        "ANT": 45,
        "USERS": 120,
        "INVT": 1030
    }

    ip_service.set_sub_network(sub)

    print(ip_service.sub_networks)

    print(ip_service.get_base_mask())

    print(ip_service.get_base_q_and_position())

    print(ip_service.sub_all_network())

    print(ip_service.result())
