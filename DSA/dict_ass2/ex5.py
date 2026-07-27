def add_movie(movies, name):
    movies.append(name)
    print(f"'{name}' added successfully.")
def remove_movie(movies, name):
    if name in movies:
        movies.remove(name)
        print(f"'{name}' removed successfully.")
    else:
        print(f"'{name}' not found in the collection.")
def search_movie(movies, name):
    if name in movies:
        print(f"'{name}' is present in the collection.")
    else:
        print(f"'{name}' not found.")
def sort_movies(movies):
    movies.sort()
    print("Movies sorted alphabetically.")
def display_movies(movies):
    if not movies:
        print("No movies in the collection.")
    else:
        print("Movie Collection:")
        for movie in movies:
            print(f"- {movie}")
def main():
    movies = []
    while True:
        print("\n--- Movie Collection Manager ---")
        print("1. Add Movie")
        print("2. Remove Movie")
        print("3. Search Movie")
        print("4. Sort Movies")
        print("5. Display All Movies")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter movie name to add: ")
            add_movie(movies, name)
        elif choice == 2:
            name = input("Enter movie name to remove: ")
            remove_movie(movies, name)
        elif choice == 3:
            name = input("Enter movie name to search: ")
            search_movie(movies, name)
        elif choice == 4:
            sort_movies(movies)
        elif choice == 5:
            display_movies(movies)
        elif choice == 6:
            print("Exiting Movie Collection Manager...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
