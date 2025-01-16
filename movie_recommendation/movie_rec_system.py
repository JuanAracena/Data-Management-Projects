# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    ratings_data = {}
    for line in open(f):

        name, rating, mId = line.split('|')
        if name in ratings_data:
            ratings_data[name.strip()].append(float(rating.strip()))
        else:
            ratings_data[name.strip()] = [float(rating.strip())]
        
    
    return ratings_data
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    movie_data = {}
    for line in open(f):
        genre, number, name = line.split('|')
        movie_data[name.strip()] = genre.strip()

    return movie_data

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    #print(d)
    #genre_dict = {}
    #for keys, values in d.items():
       # genre_dict[values] = keys

    lst = [(value, key) for key, value in d.items()]
    genre_dict = defaultdict(list)
    for keys, values in lst:
        genre_dict[keys].append(values)


    return dict(genre_dict)
    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW

    lst = [x for x in d.values()]
    total_lst = []
    for rating_lst in lst:
        total = sum(rating_lst)
        total_lst.append(total/len(rating_lst))    
    
    
    key_lst = [key for key in d.keys()]
    rating_dict = dict(zip(key_lst, total_lst))
    
    return rating_dict
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW

    pop_movies = Counter(d)
    top_movies = pop_movies.most_common(n)

    return dict(top_movies)
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filter_lst = [(key, value) for key, value in d.items() if value >= thres_rating]

    return dict(filter_lst)
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    get_pop_genre = {}

    if genre in genre_to_movies:
        for movie_genre in genre_to_movies[genre]:
            if movie_genre in movie_to_average_rating:
                get_pop_genre[movie_genre] = movie_to_average_rating[movie_genre]
    final_lst = sorted(get_pop_genre.items(), key = lambda x : x[1], reverse=True)[:n]

    return dict(final_lst)
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    genre_avg = 0
    movie_lst = []
    if genre in genre_to_movies:
        for movie_genre in genre_to_movies[genre]:
            if movie_genre in movie_to_average_rating:
                movie_lst.append(movie_to_average_rating[movie_genre])
    
    return sum(movie_lst) / len(movie_lst)
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    genre_pop_dict = {}

    for key, value in genre_to_movies.items():
        genre_pop_dict[key] = get_genre_rating(key, genre_to_movies, movie_to_average_rating)
    
    genre_counter = Counter(genre_pop_dict)

    return dict(genre_counter.most_common(n))

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    ratings_data = {}

    for line in open(f):
        name, rating, mId = line.split('|')
        mId = mId.strip()
        name = name.strip()
        rating = rating.strip()
        if mId in ratings_data:
            ratings_data[mId].append((name, rating))
        else:
            ratings_data[mId] = [(name, rating)]
    
    
    return ratings_data
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    
    user_ratings =  user_to_movies.get(str(user_id), [])

    genre_ratings = {}
    genre_counts = {}

    for movie_id, rating in user_ratings:
        genre = movie_to_genre[movie_id]
        if genre:
            if genre in genre_ratings:
                genre_ratings[genre] += float(rating)
                genre_counts[genre] += 1
            else:
                genre_ratings[genre] = float(rating)
                genre_counts[genre] = 1
    
    genre_avg_ratings = {}
    for genre, total_rating in genre_ratings.items():
        genre_avg_ratings[genre] = total_rating/genre_counts[genre]
    
    top_genre = max(genre_avg_ratings, key = genre_avg_ratings.get)
    return top_genre

    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW

    
    fav_genre = get_user_genre(str(user_id), user_to_movies, movie_to_genre)
    genre_to_movies = create_genre_dict(movie_to_genre)
    top_genre_movies = get_popular_in_genre(fav_genre, genre_to_movies, movie_to_average_rating)
    
    user_ratings = user_to_movies.get(str(user_id), [])
    rated_movies = {movie_id for movie_id, _ in user_ratings}

    unrated_movies = [movie for movie in top_genre_movies if movie not in rated_movies]

    recommended_movies = {}
    for movie_id in unrated_movies:
        recommended_movies[movie_id] = movie_to_average_rating.get(movie_id)

    return recommended_movies


# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    ratingsf = {}
    ratingsf = read_ratings_data('ratings.txt')
    genresf = {}
    genresf = read_movie_genre('movies.txt')
    newGenres = create_genre_dict(genresf)
    newRatings = calculate_average_rating(ratingsf)
    popularity = get_popular_movies(newRatings)
    thresh_movies = filter_movies(newRatings)
    genre_pop = get_popular_in_genre('Comedy', newGenres, newRatings, 2)
    genre_rating = get_genre_rating('Comedy', newGenres, newRatings)
    pop_genre = genre_popularity(newGenres, newRatings)
    ratings = read_user_ratings('ratings.txt')
    final_func = get_user_genre(6, ratings, genresf)
    rec_movies = recommend_movies(1, ratings, genresf, newRatings)

    print(f'Task 1.1: {ratingsf}\n')
    print(f'Task 1.2: {genresf}\n')
    print(f'Task 2.1: {newGenres}\n')
    print(f'Task 2.2: {newRatings}\n')
    print(f'Task 3.1: {popularity}\n')
    print(f'Task 3.2: {thresh_movies}\n')
    print(f'Task 3.3: {genre_pop}\n')
    print(f'Task 3.4: {genre_rating}\n')
    print(f'Task 3.5: {pop_genre}\n')
    print(f'Task 4.1: {ratings}\n')
    print(f'Task 4.2: {final_func}\n')
    print(f'Task 4.3: {rec_movies}\n')
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    
