import ipaddress as ip

CLASS_C_ADDR = '192.168.0.0'

if __name__ == "__main__":
	not_configured = True
	while not_configured:
		prefix = input("Enter the prefixlen (24-30): ")
		prefix = int(prefix)
		if prefix not in range(23,31):
			raise Exception("Prefixlen must be betweek 24 and 30")
		net_addr = CLASS_C_ADDR + "/" + str(prefix)
		print("Using network address: %s " %net_addr)
		try:
			network = ip.ip_network(net_addr)
		except:
			raise Exception("Failed to create network object")
		print("This prefix will give %s IP Addresses"%(network.num_addresses))
		print("The network configuration will be")
		print("\t network address: %s" %str(network.network_address))
		print("\t netmask: %s" %str(network.netmask))
		print("\t broadcast_address: %s" %str(network.broadcast_address))
		first_ip, last_ip = list(network.hosts())[0], list(network.hosts())[-1]
		print("\t host IP Addresses: from %s to %s "%(first_ip, last_ip))
		ok = input("Is this configuration OK [y/n]?")
		ok = ok.lower()
		if ok.strip() == 'y':
			not_configured = False
