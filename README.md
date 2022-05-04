# _Online IQ Test_
#### CS50 Final Project
Present a sample of an IQ Test online and review your results. 

The project wants to encourage people to enhance their cognitive performance in life, this is based in the idea that the recurrent practice of our mental abilities like logical, verbal, mathematical and technical skills improves our overall development in our daily activities.

## Tech
- [Flask](https://flask.palletsprojects.com/en/2.1.x/#) - Python Web Framework
- [Web Development](https://www.w3schools.com/whatis/)- CSS, HTML, Javascript
- [Bootstrap](https://getbootstrap.com/) - CSS Framwork
- [Database](https://www.sqlite.org/index.html) - SQL Lite

## Project Explanation

The test consist in 20 questions that vary from different verbal, mathematical, logic and technical fields. They are selected from a database constructed in SQL Lite. There is a limit of 20 minute timeframe to finish it, after submitting the answers the results are displayed as a range of the IQ obtained, a comment of the achieved range and a grade per each major field.

### Database
The database consists of two tables:
1) **Questions**

With the following structure:
| *id* | *type* | *question* | *content* |
| ------ | ------ | ------ | ------ |
| 1 | Math | What numbers should replace the question marks? | 100, 95, ?, 79, 68, ?, 40, 23|
| 2 | Verbal | Clever is to ingenious as wise is to  | NULL |
| ..| .. |.. |.. |

A question can have or not data in the *content* column, this field contains supporting information to the question as the example shown above. The type of question will vary from the fields: verbal, math, logic or technical.

2) **Answers**

With the following structure:

| *id* | *questionid* | *answer* | *correct* |
| ------ | ------ | ------ | ------ |
| 1 | 1 | 90 and 41 | FALSE |
| 2 | 1 | 81 and 53  | FALSE |
| 3 | 1 | 88 and 55  | TRUE |
| 4 | 1 | 94 and 46  | FALSE |
| ..| .. |.. |.. |

The primary key for an answer is its *id*. There is one record per each answer and the *questionid* will relate the answer text with a particular question. The boolean field in the *correct* column represents a way to show the corrrect answer from an answer's set. As the example above, the answers correspond with the question wiht *id*=1 and the correct answer to the question is the third record.

## Usage
To run the application have to run the flask server:
```sh
flask run
```
Then the server will respond with a URL.
![Image text](https://github.com/admaga/CS50-Final-Project/blob/main/img/flask_run.jpg)

Where we can use our web page.
![Image text](https://github.com/admaga/CS50-Final-Project/blob/main/img/main_screen.jpg)

## Demonstration
There is a live demonstration of this project in the following Youtube [link](https://youtu.be/sq2JY4tL0XM)
