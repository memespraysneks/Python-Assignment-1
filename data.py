import matplotlib.pyplot as plt
from math import *

alpha_size = [16, 32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536]
alpha_time = [0.089,0.242,0.608,2.367,8.886,37.183,146.544,590.168,2310.044,9224.905,36771.744,139134.832,515482.254]

bravo_size = [16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304]
bravo_time = [0.052, 0.078, 0.132, 0.233, 0.47, 1.069, 1.899, 3.896, 7.303, 14.903, 29.307, 56.426, 115.3, 261.299, 456.469, 912.857,1831.419,3676.336,7290.534]

charlie_size = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]
charlie_time = [0.079,0.663,3.29,13.246,35.901,86.824,195.558,396.304,744.545,1332.306,2285.819,3759.908,5992.9,9283.569,14107.611,20809.166,30217.893,43107.306,60589.996,83991.306]

delta_size = [2,4,8,16, 32,64,128,256,512,1024,2048,4096,8192]
delta_time = [0.013,0.019,0.034,0.104,0.382,1.553,8.421,40.934,223.845,1306.56,8461.372,61462.496,461133.86]

plt.plot(alpha_size, alpha_time, marker = "o")

plt.title("Alpha sorting Input Size over Time (ms)")
plt.xlabel("Log Base 2(Input Size)")
plt.ylabel("Time (ms)")

plt.show()

plt.plot(bravo_size, bravo_time, marker = "o")

plt.title("Bravo sorting Input Size over Time (ms)")
plt.xlabel("Input Size")
plt.ylabel("Time (ms)")

plt.show()

plt.plot(charlie_size, charlie_time, marker = "o")

plt.title("Charlie sorting Input Size over Time (ms)")
plt.xlabel("Input Size")
plt.ylabel("Time (ms)")

plt.show()

plt.plot(delta_size, delta_time, marker = "o")

plt.title("Delta sorting Input Size over Time (ms)")
plt.xlabel("Input Size")
plt.ylabel("Time (ms)")

plt.show()
