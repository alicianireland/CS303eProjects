# File: movies.py
# Description: A program works with movie ratings and reviews.
# Based on the Nifty Assignment:
# http://nifty.stanford.edu/2016/manley-urness-movie-review-sentiment/
# Assignment Number: 12
#
# Name: Alicia Ireland
# EID:  ani324
# Email: alicianireland@gmail.com
# Grader: Noah
#
#Â On my honor, Alicia Ireland, this programming assignment is my own work
#Â and I have not provided this code to any other student.


# Read the main data file and run the menu loop.
def main():
    print('Welcome to the movie sentiment program.')
    print('Enter a word to see the average rating of movies with that word.')
    file_name = input('Enter file name with reviews: ')
    reviews = get_reviews(file_name)
    choice = get_choice()
    # List of our functions. They all take a single parameter, the reviews.
    functions = [print_word_sentiment, print_sentiments_from_file,
                 print_longest_review, print_shortest_review]
    VALUE_1 = ord('1')
    while '1' <= choice <= '4':
        # Get the index of the function to call.
        index = ord(choice) - VALUE_1
        function = functions[index](reviews)
        choice = get_choice()

    
# Display the menu and get the users choice.
# Returns the user's choice as a String.
def get_choice():
    print()
    print('OPTIONS:')
    print('1. See average rating for a word.')
    print('2. Show average reviews for all words in a file.')
    print('3. See the longest review.')
    print('4. See the shortest review.')
    result = input('Please enter your choice: ')
    print()
    return result


# Given the file name, create a list of lists with the movie reviews.
# We expect one review per line. The first element will be an int [0, 4].
# The rest of the line shall be the review.
# All letters in the reviews are converted to lower case.
def get_reviews(file_name):   
    file = open(file_name)
    list_review = convert_into_list(file, "make_lower")
    file.close()

    # change movie rating at begining of each list to an integer
    for i in range(len(list_review)):
        list_review[i][0] = int(list_review[i][0])
            
    return list_review

# Take a file and converts contents into a list of list with each line  
# from file  converted to its own list of the words in line. Removes all 
# white spaces after each line and splits each line by spaces between words.
def convert_into_list(file,condition):
    list_review = []
    for line in file:
        if condition == "make_lower":
            line = line.lower()
        line = line.split()
        list_review += [line]
    return list_review


# Get a word from the user and determine the average rating of
# reviews that contain that word. reviews is a list of lists that
# contain the reviews.
def print_word_sentiment(reviews):
    word = input("Enter the word to search for: ")

    word_appears, average_reviews = get_occurances(reviews, word)

    if word_appears == 0:
        print(word,"did not appear in any reviews")
    else:
        review = "review" if word_appears == 1 else "reviews"
        print(word,"appeared in", word_appears, review + ". " +
          "Average review score =", average_reviews)        


# Ask the user for the name of a file with words and phrases.
# We assume one word or phrase per line in the file.
# For each word or phrase in the file, determine and show
# the average rating of reviews that contain the given word.
def print_sentiments_from_file(reviews):
    file = input("Enter file name with words to check: ")
    file = open(file)
     
    list_review = convert_into_list(file, "dont_make_lower")
  
    for i in range(len(list_review)):
        word_phrase = list_review[i][0]
        word_appears, num_reviews = get_occurances(reviews, word_phrase)

       
        review = "review" if word_appears == 1 else "reviews"
            
        if num_reviews !=0:
            print("Word number", i+1,"is '" + word_phrase + "'. Results: \n" +
                  word_phrase, "appeared in", word_appears, review +
                  ". Average review", "score =", str(num_reviews) + "\n")
        else:
            print("Word number", i+1,"is '" + word_phrase + "'. Results: \n" +
                  word_phrase, "did not appear in any reviews\n")
              
    
# Get a word from the user and determine the average rating of
# reviews that contain that word. reviews is a list of lists that
# contain the reviews.
def get_occurances(reviews,word_phrase):
    word_appears = 0
    word_phrase = word_phrase.lower()

    # Loops through every row and counts if row (review)
    # contains word atleast once. Keeps track of the review num
    # given and adds to total if word is present in that review.
    review_given = 0
    for i in range(len(reviews)):
        if word_phrase in reviews[i]:
            word_appears += 1
            review_given += reviews[i][0]
            
    if word_appears != 0:
        average_review = review_given / word_appears
    else:
        average_review = 0

    return word_appears, average_review 
    

# Print information about the longest review. 
def print_longest_review(reviews):
    longest_review_len, longest_review = \
                        find_min_max_len(reviews, "longest") 
    print("Longest review has", longest_review_len, "words.")
    print("Review as list:",longest_review)

        
# Print information about the shortest review. 
def print_shortest_review(reviews):

    shortest_review_len, shortest_review = \
                         find_min_max_len(reviews, "shortest")    
    print("Shortest review has", shortest_review_len, "words.")
    print("Review as list:",shortest_review)


# Finds the shortest or longest review based on the condition passed.
# Length based on number of words, with every token counted as a word except
# the first number. If a tie for length occurs, the one that appears
# first is displayed. Returns the length of the shortest or longest review 
# and the review itself.
def find_min_max_len(reviews, condition):
    # make copy of list of reviews to pop off first int num.
    copy_reviews = [line[:] for line in reviews]
    current_len = len(copy_reviews[0])    

    # loops through every row comparing the length of row
    # to the previous row length.
    for i in range(len(reviews)):
        copy_reviews[i].pop(0)
        next_len = len(copy_reviews[i])
        if (current_len <  next_len if condition =="longest" else \
            current_len >  next_len): 
            current_len = next_len
            row_of_review = i
    review = copy_reviews[row_of_review]
    return current_len, review
    

main()
