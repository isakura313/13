import pytest
import random
from Survey import *

question = "На каком языке вы хотели заговорить?"
my_survey = Survey(question)

responses = ['English', 'Русский', "Spanish"]


def test_store_single_response():
    rand = random.choice(responses)
    my_survey.store_response(rand)
    assert rand in my_survey.responses

def test_store_some_responses():
    for response in responses:
        my_survey.store_response(response)
    for response in responses:
        assert response in my_survey.responses