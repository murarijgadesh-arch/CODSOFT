#codsoft task 4
print("recommendation system!!!")
#assigning dictionary for recommendation
movies={"Avengers":["Action","Superhero"],"Batman":["Action","Superhero"],"Ironman":["Action","Superhero"],"Titanic":["Romance","Drama"],"Notebook":["Romance","Drama"],"Interstellar":["Sci-fi","Adventure"],"Inception":["Sci-fi","Thriller"],"The Martian":["Sci-fi","Adventure"],"John Wick":["Acton","Thriller"],"Joker":["Drama","Thriller"]}
print("Available Genres")
print("Action")
print("Superhero")
print("Romance")
print("Drama")
print("Sci-fi")
print("Thriller")
print("Adventure")
genre=input("\n enter your favorite genre:")
recommendations=[]
for movie,genres in movies.items():
    if genre in genres:
        recommendations.append(movie)
print("\n Recommended movies!")
if recommendations:
    for movie in recommendations:
        print("-",movie)
else:
        print("No recommendations found!!")