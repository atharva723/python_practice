def ips(path):
        ip=[line.split()[0] for line in open(path)]
        d={i:ip.count(i) for i in ip}
        return print(f"Most visited ip is {sorted(d,key=lambda x:d[x])[-1]}\nLeast visited ip is {sorted(d,key=lambda x:d[x])[0]}")
ips('access-log.txt')
