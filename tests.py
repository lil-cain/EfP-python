import os, json, unittest
import hypothesis
import hypothesis.strategies as st
from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    @hypothesis.given(st.text(min_size=1, alphabet=st.characters(
        blacklist_characters=["\n",',',':','/','?','#','[',']',
                              '@','!','$','&','(',')','*','+',';','='])))
    def test_excercise1(self, s):
        response = self.app.get("/greet/%s" % s)
        greeting = json.loads(response.data.decode())
        self.assertEqual(greeting['response'],  "Hello %s, nice to meet you!" % s, "Default works!")

    def test_excercise1_special_case(self):
        response = self.app.get('/greet/Gemma')
        greeting = json.loads(response.data.decode())['response']
        self.assertEqual(greeting, "Hello Gemma, you're looking good!", "Gemma works")

        response = self.app.get('/greet/')
        greeting = json.loads(response.data.decode())['response']
        self.assertEqual(greeting, "You need to tell me your name", "Blank string works")

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

    def test_excercise5(self):
        response = self.app.get('/math/', data=json.dumps([4, 10, 15]))
        response = json.loads(response.data.decode())
        self.assertEqual(response['addition'], '4 + 10 + 15 = 29', 'addition')
        self.assertEqual(response['subtraction'], '4 - 10 - 15 = -21', 'subtraction')
        self.assertEqual(response['multiplication'], '4 * 10 * 15 = 600', 'multiplication')
        self.assertEqual(response['division'], '4 / 10 / 15 = 0.026667', 'divison')

    def test_excercise6(self):
        response = self.app.get('/retirement/',
            data=json.dumps({'age': 28, 'retirementAge': 70}))
        response = json.loads(response.data.decode())
        self.assertEqual(response['yearsTillRetirement'], 42, 'years till retirement')
        self.assertEqual(response['retirementYear'], 2058, 'retirement year')

if __name__ == '__main__':
    unittest.main()
