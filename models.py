from flask_sqlalchemy import SQLAlchemy

db2 = SQLAlchemy()

class User(db2.Model):
    #__tablename__ = user
    id = db2.Column(db2.Integer, primary_key = True)
    name = db2.Column(db2.String(25))
    quizes = db2.relationship('Quiz', backref = 'user')

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

class Quiz(db2.Model):
    id = db2.Column(db2.Integer, primary_key = True)
    name = db2.Column(db2.String(100))
    user_id = db2.Column(db2.Integer, db2.ForeignKey('user.id'))

    def __init__(self, name, user:User) -> None:
        super().__init__()
        self.name = name
        self.user = user

quiz_question = db2.Table('quiz_question',
            db2.Column('quiz_id', db2.Integer, db2.ForeignKey('quiz.id')),
            db2.Column('question_id', db2.Integer, db2.ForeignKey('question.id'))
            )

class Question(db2.Model):
    id = db2.Column(db2.Integer, primary_key = True)
    question_text = db2.Column(db2.String(250), nullable = False)
    answer = db2.Column(db2.String(250), nullable = False)
    wrong1 = db2.Column(db2.String(100), nullable = False)
    wrong2 = db2.Column(db2.String(100), nullable = False)
    wrong3 = db2.Column(db2.String(100), nullable = False)
    quiz = db2.relationship('Quiz', secondary=quiz_question, backref = 'question')

    def __init__(self, question_text: str, answer:str, wrong1:str, wrong2:str, wrong3:str) -> None:
        super().__init__()
        self.question_text = question_text
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def db_add_new_data():
    db2.drop_all()
    db2.create_all()

    user1 = User('user1')
    user2 = User('user2')

    quizes = [
        Quiz('quiz1', user1),
        Quiz('quiz2', user2),
    ]

    questions = [
        Question('2+2*2', '6', '0', '8', '5')
    ]

    #quizes[0].a


    db2.session.add_all([user1, user2])
    db2.session.add_all(quizes)

    db2.session.commit()