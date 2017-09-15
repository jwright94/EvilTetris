import json
import random
import HTMLParser
import urllib, json

questions = []

class Question:
	def __init__(self):
		self.question = ""
		self.options = []
		self.answer = 0
		
	def __str__(self):
		out = ""
		out += ("Q: " + self.question + '\r\n')
		for a in self.options:
			out += a + '\r\n';
		out += str(self.answer) + '\r\n'
		return out

def downloadQuestions():
	url = "https://opentdb.com/api.php?amount=20&category=18&difficulty=hard"
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	print(data)
	return data
	
def loadQuestions():
	loadQuestionsFromJson(downloadQuestions()['results'])
	with open('questions.json') as questionFile:    
		loadQuestionsFromJson(json.load(questionFile)['results'])
			
def loadQuestionsFromJson(data):
		
	for q in data:
		obj = Question()
		obj.question = processText(q['question']);
		obj.options = [];
		
		incorrectAnswers = q['incorrect_answers'];
		obj.answer = random.randint(0, len(incorrectAnswers))
		
		# could do this better with array alicing but im lazy
		for i in range(len(incorrectAnswers)):
			if i == obj.answer:
				obj.options.append(processText(q['correct_answer']))
			obj.options.append(processText(incorrectAnswers[i]))
		
		if obj.answer == len(incorrectAnswers):
			obj.options.append(processText(q['correct_answer']))
			
		questions.append(obj)
		
h = HTMLParser.HTMLParser()
	
def processText(txt):
	return h.unescape(txt).encode(encoding="utf-8")
	
def getQuestion():
	if len(questions) == 0:
		loadQuestions()
	q = random.choice(questions)
	questions.remove(q)
	print(q)
	return q

loadQuestions()

print(getQuestion())