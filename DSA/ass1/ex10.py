# Product Rating System
def analyze_ratings(ratings):
    average = sum(ratings) / len(ratings)
    five_star_count = ratings.count(5)
    sorted_ratings = sorted(ratings)
    print("===================================")
    print(f"Ratings List        : {ratings}")
    print(f"Average Rating      : {average:.2f}")
    print(f"5-Star Ratings      : {five_star_count}")
    print(f"Sorted Ratings      : {sorted_ratings}")
    print("===================================")
def main():
    ratings = []
    n = int(input("Enter number of ratings: "))
    for i in range(n):
        rating = int(input(f"Enter rating {i+1} (1-5): "))
        if 1 <= rating <= 5:
            ratings.append(rating)
        else:
            print("Invalid rating! Please enter between 1 and 5.")
            return 
    analyze_ratings(ratings)
if __name__ == "__main__":
    main()
