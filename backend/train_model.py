from model import NLPModel

from sklearn.model_selection import train_test_split
import pandas as pd


def train_model():
    path = 'lib/data/imdb_labelled.txt'
    data = pd.read_csv(path, sep='\t', header=None)
    data.columns = ['text', 'score']

    reviews_train, reviews_test, y_train, y_test = train_test_split(
        data['text'],
        data['score'],
        test_size=0.2,
    )

    model = NLPModel()
    model.fit_vectorizer(reviews_train)
    X_train = model.transform_vectorizer(reviews_train)
    X_test = model.transform_vectorizer(reviews_test)

    model.train(X_train, y_train)

    model.report_accuracy(X_test, y_test, 'lib/model/accuracy')

    model.pickle_vectorizer()
    model.pickle_clf()


if __name__ == '__main__':
    train_model()
