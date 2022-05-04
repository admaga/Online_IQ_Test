from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

db = SQL("sqlite:///iqtest.db")

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/history")
def history():
	return render_template("history.html")

@app.route("/pretest")
def pretest():
	return render_template("pretest.html")

@app.route("/results", methods = ['POST', 'GET'])
def results():
	if request.method == "GET":
		return render_template("/",)
	else:
		# List with all the answers from user
		user_answers = []
		for i in range(1, 20 + 1):
			n1 = request.form.get(str(i))
			user_answers.append([i, n1])

		# Dictionary with all the correct answers from database
		c_answers = db.execute("SELECT answer FROM answers WHERE correct = 'TRUE'")

		# Boolean list of correct answers
		check_answers = []
		# Count of correct answers
		c_count = 0
		# Verify user answer with correct answers
		for i in range(0, 20):
			if c_answers[i]['answer'] == user_answers[i][1]:
				check_answers.append('TRUE')
				c_count += 1
			else:
				check_answers.append('FALSE')

		# Count questions and correct answers for each answer type
		type_dict = {
			'Math': {'correct': 0, 'count': 0},
        		'Logic': {'correct': 0, 'count': 0},
        		'Verbal': {'correct': 0, 'count': 0},
        		'Technical': {'correct': 0, 'count': 0},
		}

		# Check correct answers per type of question and increment respective counter
		for TYPE, value in type_dict.items():
			# Select all the correct answers filtering by each type
			c_type_answers = db.execute("SELECT * FROM answers JOIN questions ON questions.id = answers.questionid WHERE questions.type= ? AND answers.correct = 'TRUE'", TYPE)
			# Upload count of total question per type
			type_dict[TYPE]['count'] = len(c_type_answers)
			# Verify this answers with the user answers
			for row in c_type_answers:
				for i in range(0, 20):
					if row['questionid'] == user_answers[i][0] and row['answer'] == user_answers[i][1]:
						# Counter for correct answers depending on the type of question
						type_dict[TYPE]['correct'] += 1
						break

		# IQ Result dictionary, type of questions are in 0-100 base
		iq_result = {
		  "Range": '',
		  "Comment": '',
		  "Math": 0,
		  "Logic": 0,
		  "Verbal": 0,
		  "Technical": 0,
		}

		# Resolve for general result
		if (c_count == 0):
			iq_result['Range'] = "0"
			iq_result['Comment'] = "No Answers Registered"
		elif (c_count < 3):
			iq_result['Range'] = "40-54"
			iq_result['Comment'] = "Moderately impaired"
		elif (c_count > 3 and c_count < 6):
			iq_result['Range'] = "55-69"
			iq_result['Comment'] = "Mildly impaired"
		elif (c_count > 5 and c_count < 9):
			iq_result['Range'] = "70-79"
			iq_result['Comment'] = "Borderline impaired"
		elif (c_count > 8 and c_count < 12):
			iq_result['Range'] = "80-89"
			iq_result['Comment'] = "Low average"
		elif (c_count > 11 and c_count < 15):
			iq_result['Range'] = "90-109"
			iq_result['Comment'] = "Average"
		elif (c_count > 14 and c_count < 17):
			iq_result['Range'] = "110-119"
			iq_result['Comment'] = "High average"
		elif (c_count > 16 and c_count < 19):
			iq_result['Range'] = "120-129"
			iq_result['Comment'] = "Superior"
		elif (c_count == 19):
			iq_result['Range'] = "130-144"
			iq_result['Comment'] = "Very advanced"
		elif (c_count == 20):
			iq_result['Range'] = "145-160"
			iq_result['Comment'] = "Highly advanced"

		# Verify grade per type of question
		for TYPE, value in type_dict.items():
			iq_result[TYPE] = int((type_dict[TYPE]['correct'] / type_dict[TYPE]['count']) * 100)

		return render_template("results.html", iq_result = iq_result)

@app.route("/test")
def test():
	questions = db.execute("SELECT * FROM questions")
	answers = db.execute("SELECT * FROM answers")
	return render_template("test.html", questions=questions, answers=answers)

