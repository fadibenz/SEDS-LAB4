import SEDS_LAB4.SEDS_LAB4.modeling.sentiment as se
import pytest
import pandas as pd

testdata =["Borussia Dortmund’s loss was heartbreaking as they failed to gain momentums from their  two goals advance. Very disappointing results for our Algerian player Bensebaini."]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):
    neg_sentiment = se.extract_sentiment(sample)
    assert neg_sentiment <= 0

def test_extract_positive_sentiment():
    positive_text = "Barcelona played brilliantly last Wednesday. Rafinia’s hat-trick was pure magic. Visca Barça!"
    sentiment = se.extract_sentiment(positive_text)
    assert sentiment > 0


@pytest.mark.parametrize('sample', pd.read_csv('../../data/raw/soccer_sentiment_analysis.csv')['Text'].tolist())
def test_extract_sentiment_from_csv(sample):
    sentiment = se.extract_sentiment(sample)

    assert -1 <= sentiment <= 1