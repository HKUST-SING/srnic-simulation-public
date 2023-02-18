import sys
import random
import math
import heapq
from optparse import OptionParser
from custom_rand import CustomRand

random.seed(3)

class Flow:
	def __init__(self, src, dst, size, t):
		self.src, self.dst, self.size, self.t = src, dst, size, t
	def __str__(self):
		return "%d %d 3 100 %d %.9f"%(self.src, self.dst, self.size, self.t)

def translate_bandwidth(b):
	if b == None:
		return None
	if type(b)!=str:
		return None
	if b[-1] == 'G':
		return float(b[:-1])*1e9
	if b[-1] == 'M':
		return float(b[:-1])*1e6
	if b[-1] == 'K':
		return float(b[:-1])*1e3
	return float(b)

def poisson(lam):
	return -math.log(1-random.random())*lam

if __name__ == "__main__":
	port = 80
	parser = OptionParser()
	parser.add_option("-c", "--cdf", dest = "cdf_file", help = "the file of the traffic size cdf", default = "uniform_distribution.txt")
	parser.add_option("-n", "--nhost", dest = "nhost", help = "number of hosts")
	parser.add_option("-l", "--load", dest = "load", help = "the percentage of the traffic load to the network capacity, by default 0.3", default = "0.3")
	parser.add_option("-b", "--bandwidth", dest = "bandwidth", help = "the bandwidth of host link (G/M/K), by default 10G", default = "10G")
	parser.add_option("-t", "--time", dest = "time", help = "the total run time (s), by default 10", default = "10")
	parser.add_option("-o", "--output", dest = "output", help = "the output file", default = "tmp_traffic.txt")
	parser.add_option("--incastdegree", dest = "incastDegree", help = "the incast degree", default = "60")
	parser.add_option("--incastload", dest = "incastLoad", help = "the incast load", default = "0.02")
	parser.add_option("--incastsize", dest = "incastSize", help = "the incast size", default = "500000")

	options,args = parser.parse_args()

	base_t = 2000000000

	if not options.nhost:
		print "please use -n to enter number of hosts"
		sys.exit(0)
	nhost = int(options.nhost)
	load = float(options.load)
	bandwidth = translate_bandwidth(options.bandwidth)
	time = float(options.time)*1e9 # translates to ns
	output = options.output
	if bandwidth == None:
		print "bandwidth format incorrect"
		sys.exit(0)

	fileName = options.cdf_file
	file = open(fileName,"r")
	lines = file.readlines()
	# read the cdf, save in cdf as [[x_i, cdf_i] ...]
	cdf = []
	for line in lines:
		x,y = map(float, line.strip().split(' '))
		cdf.append([x,y])

	# create a custom random generator, which takes a cdf, and generate number according to the cdf
	customRand = CustomRand()
	if not customRand.setCdf(cdf):
		print "Error: Not valid cdf"
		sys.exit(0)

	ofile = open(output, "w")

	# generate flows
	avg = customRand.getAvg()
	avg_inter_arrival = 1/(bandwidth*load/8./avg)*1000000000
	n_flow_estimate = int(time / avg_inter_arrival * nhost)

	incast_size = int(options.incastSize) # 500KB
	n_incast_host = int(options.incastDegree) # incast scale
	incast_load = float(options.incastLoad)
	incast_load = incast_load * (nhost * 1.0 / n_incast_host)
	print(incast_load)
	if options.incastLoad == "0":
		avg_inter_arrival_incast = "infinit"
		n_incast_time_estimate = 0
	else:
		avg_inter_arrival_incast = 1/(bandwidth*incast_load/8./incast_size)*1000000000 # incast_interval 
		n_incast_time_estimate = int(time / avg_inter_arrival_incast) # how many incast
	
	incast_over_total = (n_incast_time_estimate * 1.0) / n_flow_estimate # ratio
	total_host_list = [i for i in range(nhost)] # host list
	print("incast_size", incast_size, "incast_load", incast_load, "incast time estimate", n_incast_time_estimate)
	print("n_incast_host", n_incast_host, "avg_inter_arrival_incast", avg_inter_arrival_incast, "incast_over_total", incast_over_total)

	n_flow = 0
	total_flow_estimate = n_flow_estimate + n_incast_time_estimate * n_incast_host
	ofile.write("%d \n"%total_flow_estimate)
	# ofile.write("%d \n"%n_flow_estimate)
	host_list = [(base_t + int(poisson(avg_inter_arrival)), i) for i in range(nhost)]
	heapq.heapify(host_list)
	while len(host_list) > 0:
		t,src = host_list[0]
		inter_t = int(poisson(avg_inter_arrival))
		new_tuple = (src, t + inter_t)
		dst = random.randint(0, nhost-1)
		while (dst == src):
			dst = random.randint(0, nhost-1)
		if (t + inter_t > time + base_t):
			heapq.heappop(host_list)
		else:
			size = int(customRand.rand())
			if size <= 0:
				size = 1
			n_flow += 1;
			ofile.write("%d %d 3 100 %d %.9f\n"%(src, dst, size, t * 1e-9))
			heapq.heapreplace(host_list, (t + inter_t, src))
			# for incast traffic
			ratio = random.random()
			if ratio < incast_over_total: # insert incast traffic
				incast_list = random.sample(total_host_list, n_incast_host)
				print(incast_list)
				incast_dst = random.randint(0, nhost-1)
				while incast_dst in incast_list:
					incast_dst = random.randint(0, nhost-1)
				n_flow += 60
				for i in range(n_incast_host):
					ofile.write("%d %d 3 100 %d %.9f\n"%(incast_list[i], incast_dst, incast_size, t * 1e-9))
	ofile.seek(0)
	ofile.write("%d"%n_flow)
	ofile.close()

'''
	f_list = []
	avg = customRand.getAvg()
	avg_inter_arrival = 1/(bandwidth*load/8./avg)*1000000000
	# print avg_inter_arrival
	for i in range(nhost):
		t = base_t
		while True:
			inter_t = int(poisson(avg_inter_arrival))
			t += inter_t
			dst = random.randint(0, nhost-1)
			while (dst == i):
				dst = random.randint(0, nhost-1)
			if (t > time + base_t):
				break
			size = int(customRand.rand())
			if size <= 0:
				size = 1
			f_list.append(Flow(i, dst, size, t * 1e-9))

	f_list.sort(key = lambda x: x.t)

	print len(f_list)
	for f in f_list:
		print f
'''
