import pandas as pd

#data as a dataframe
data = pd.read_csv('userReviews.csv', sep=';')

#the same as SELECT function in SQL
print(data.head())
print(data[:3])
print(data.movieName.iloc[1])

#creating a subset of the data regarding the movie "about-a-boy"
subset = data[data.movieName == 'about-a-boy']

#overview of the authors whom reviewed the movie
print(subset)

#Create final dataframe for the recommendations that also include the relative score
recommendations = pd.DataFrame(columns=data.columns.tolist()+['rel_inc'])

#loop over all Authors that watched the same favorit movie and then save each author who gave a ranking for the favorite movie
for idx, Author in subset.iterrows():

#save the author and ranking who reviewed this specific favourite movie
    author = Author[['Author']].iloc[0]
    ranking = Author[['Metascore_w']].iloc[0]
    
#create a new possible recommendations
    filter1 = (data.Author==author)
    filter2 = (data.Metascore_w>ranking)
    possible_recommendations = data[filter1 & filter2]
    
#calcuate the relative increase
    possible_recommendations.loc[:,'rel_inc'] = possible_recommendations.Metascore_w/ranking
    
#change recommendations to the new recommendations
    recommendations = recommendations.append(possible_recommendations)
    
#sort the recommendations where the highest values relative are on top of that
recommendations = recommendations.sort_values(['rel_inc'], ascending=False)

#drop the duplicates to decrease somehow the siez eo ffht efile
recommendations = recommendations.drop_duplicates(subset='movieName', keep="first")

#check the outcome first - if these recommendations make sense
print(recommendations.head(50))

#creating a file with the recommendations
recommendations.head(50).to_csv("PY_recommendationsBasedOnMetascore.csv", sep=";", index=False)

#show the recommendations reults
print(recommendations.head(50))
