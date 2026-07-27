def analyze_traffic(traffic):
    max_traffic = max(traffic)
    peak_hour = traffic.index(max_traffic) + 1
    min_traffic = min(traffic)
    min_hour = traffic.index(min_traffic) + 1
    total = sum(traffic)
    average = total / len(traffic)
    above_500 = [i+1 for i, v in enumerate(traffic) if v > 500]
    print("===================================")
    print(f"Traffic Data (24 hrs): {traffic}")
    print(f"Peak Traffic Hour    : Hour {peak_hour} ({max_traffic} vehicles)")
    print(f"Minimum Traffic Hour : Hour {min_hour} ({min_traffic} vehicles)")
    print(f"Total Daily Traffic  : {total}")
    print(f"Average per Hour     : {average:.2f}")
    print(f"Hours > 500 vehicles : {above_500}")
    print("===================================")

def main():
    traffic = []
    for i in range(24):
        val = int(input(f"Enter vehicles for Hour {i+1}: "))
        traffic.append(val)
    analyze_traffic(traffic)

if __name__ == "__main__":
    main()
