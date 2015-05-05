# DTU-02806
Final assignment in Social Data Analysis and visualization


## Quick intro
The web app is made using Django framework and mpld3 (d3.js + matplotlib) to visualize data. The data is mined, preprocessed (cleansed -> translated -> stemmed) and then analyzed using django cron-jobs.

## Database
MySQL 5.6, although the project started out using sqlite (sqlite db in repo).

## The plan
1. Mine data from Facebook API
2. Remove all stop words and convert emojis to words.
3. Stem danish words (grundled).
4. Translate to english using e.g. py-translate
5. Sentiment analysis
6. Visualize
7. 

## Visualizations
* Reply activity per party or page
* Like / comment ratio per party or page
* Negative/positve comments per party
* Negative/positive comments per party
* Time-series of negative comments
* Correlation between likes and positive/negative words
* Correlation between replies and negative words
* Word cloud on words per party
