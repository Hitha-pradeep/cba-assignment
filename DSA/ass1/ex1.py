# Daily Temperature Analyzer
def analyze_temperatures(temperatures):
    highest = max(temperatures)
    lowest = min(temperatures)
    average = sum(temperatures) / len(temperatures)
    above_avg_days = sum(1 for temp in temperatures if temp > average)
    print("===================================")
    print(f"Temperatures (7 days): {temperatures}")
    print(f"Highest Temperature  : {highest}")
    print(f"Lowest Temperature   : {lowest}")
    print(f"Average Temperature  : {average:.2f}")
    print(f"Days Above Average   : {above_avg_days}")
    print("===================================")
def main():
    temperatures = []
    for i in range(7):
        temp = float(input(f"Enter temperature for Day {i+1}: "))
        temperatures.append(temp)
    analyze_temperatures(temperatures)
if __name__ == "__main__":
    main()
