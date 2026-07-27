# Cricket Score Tracker
def analyze_scores(runs):
    total_runs = sum(runs)
    highest_score = max(runs)
    half_centuries = sum(1 for r in runs if r >= 50)
    ducks = runs.count(0)
    print("===================================")
    print(f"Runs in 15 matches : {runs}")
    print(f"Total Runs         : {total_runs}")
    print(f"Highest Score      : {highest_score}")
    print(f"Half-Centuries     : {half_centuries}")
    print(f"Ducks (0 runs)     : {ducks}")
    print("===================================")
def main():
    runs = []
    for i in range(15):
        run = int(input(f"Enter runs for Match {i+1}: "))
        runs.append(run)
    analyze_scores(runs)
if __name__ == "__main__":
    main()
