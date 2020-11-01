Considering the interpretation of the recommendations that I've received, I can now analyze the results in general (Postgresql vs. Python).

Beginning with the Postgresql the 1st movie, "About a boy", I received 13 recommendations based on the Summary, 35 based on the Title and 10 based on Starring.
The 2nd movie, "Her", I gained 12 recommendations based on the Summary, 0 based on the Title and 50 based on Starring. 
The 3nd movie, "Before Sunset", got 50 recommendations based on the Summary, 4 based on the Title and 0 based on Starring. 
Taking into consideration these results, all of them were ranked with the treshold either > 0.5 or > 0.05.

Moving on to the Python made recommendations, they were based on the the author that reviewed the specific, in this case "About a boy" movie
and metascore that this movie has received. After creating the subset of the data regarding this movie, getting an overview of the authors who review it and creating a dataframe that recieved 
the relative score, I could filter the authors and create new recommendations. Thanks to that, I've got 50 rows of recommendations for the other movies that received the highest score. 

Following that, I can state that recommendations based on the Postgresql vs. Python differ. While Postgresql coding part provided me with more specific and in-detailed results, Python code,
enabled me to receive more broader recommendations list based on the authors review and metascore. 