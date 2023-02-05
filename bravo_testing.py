import time
import statistics
from data_generators import create_numbers
from sorting_routines import sort_bravo
import matplotlib.pyplot as plt

def callAmount(n):
    times = []
    
    for i in range(10):
        before = time.perf_counter()
        sort_bravo(create_numbers(n))
        after = time.perf_counter()
        total =  (after-before)*10**3
        times.append(total)
    print(f"{ n : <15}{i+1 : <10}{round(statistics.median(times),3) : <20}{round(statistics.mean(times),3) : <20}{round(statistics.stdev(times),3): <10}")
    return {"size": n, "count": i+1, "median": round(statistics.median(times),3), "mean": round(statistics.mean(times),3), "SD": round(statistics.stdev(times),3)}


def main():
    all_values = []
    print(f"{'Size' : <15}{'Count' : <10}{'Median': <20}{'Mean' : <20}{'StDev' : <10}")
    for i in range(4, 23):
        all_values.append(callAmount(2**i))
    
    all_sizes = []
    all_length = []
    for item in all_values:
        all_sizes.append(2**(4+len(all_sizes)))
        all_length.append(item['mean'])
    plt.plot(all_sizes,all_length)
    plt.show()



if __name__ == "__main__":
    main()