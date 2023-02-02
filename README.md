# sentiment-classifier
This is a basic sentiment classifier using the [scikit-learn](https://scikit-learn.org/stable/) logistic regression classifier.

Both the back and frontend have now been taken down.

## Data
The data comes from the "Learning Word Vectors for Sentiment Analysis" paper by Mass et al. 2011. More information can be found [here](https://ai.stanford.edu/~amaas/data/sentiment/).

## Backend
The api was hosted on Heroku. Query the api by sending a GET request with data of the form ``query=<your review>``. The API will respond with either ``{"prediction": "Positive"}`` or ``{"prediction": "Negative"}``.

## Frontend
The frontend is built with [skeleton](http://getskeleton.com/) and was hosted on [netlify](https://www.netlify.com/).
