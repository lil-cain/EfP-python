import os
import unittest
import json

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_excercise1(self):
        response = self.app.get('/greet/Cian')
        greeting = json.loads(response.data.decode())
        self.assertTrue(greeting['response'] == "Hello Cian, nice to meet you!", "Default works!")

        response = self.app.get('/greet/Gemma')
        greeting = json.loads(response.data.decode())['response']
        self.assertTrue(greeting == "Hello Gemma, you're looking good!", "Gemma works")

        response = self.app.get('/greet/')
        greeting = json.loads(response.data.decode())['response']
        self.assertTrue(greeting == "You need to tell me your name", "Blank string works")

    def test_excercise2(self):
        response = self.app.get('/count/omgwtf')
        count = json.loads(response.data.decode())['count']
        self.assertEqual(int(count), 6, "String count")

        response = self.app.get('/count/')
        response = json.loads(response.data.decode())['response']
        self.assertEqual(response, "No string provided", "blank string")

    def test_excercise3(self):
        response = self.app.get('/quote/', data=json.dumps(
            {'who': 'Obi Wan Kenobi',
             'quote': "These are not the droids you're looking for"}))
        response = json.loads(response.data.decode())['comment']
        self.assertEqual(response, 
            'Obi Wan Kenobi said "These are not the droids you\'re looking for"',
            'Quote turned to comment')

    def test_excercise4(self):
        response = self.app.get('/madlib/', data=json.dumps({
            'noun': 'dog',
            'verb': 'walk',
            'adjective': 'blue',
            'adverb': 'quickly'}))
        response = json.loads(response.data.decode())['madlib']
        self.assertEqual(response, 
            "Do you walk your blue dog quickly? That's a bit mad",
            "madlib")



if __name__ == '__main__':
    unittest.main()
