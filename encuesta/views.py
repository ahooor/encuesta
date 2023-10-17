from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import loader
from encuesta.models import Answer, Question, Topic


def index(request):
    return render(request, 'index.html')

def login(request):

    if request.method == "POST":
        if('name' not in request.POST or request.POST["name"] == ''):
            context = {
                'errors': {
                    'name': True
                }
            }

            return render(request, 'login.html', context)

        request.session['user'] = request.POST["name"]
        request.session['correct_answers'] = 0
        request.session['incorrect_answers'] = 0
        request.session['times_up'] = 0
        request.session['fails'] = 0

        questions = Question.objects.values_list('id', flat=True).order_by('?')

        request.session['questions'] = list(questions)

        return  HttpResponseRedirect("/encuesta/quiz");

    return render(request, 'login.html')


def quiz(request):
    if 'user' not in request.session:
        return  HttpResponseRedirect("/encuesta/login");

    if request.method == 'POST':
        
        if 'answer' in request.POST:
            question_id = request.POST["question"]
            answer_id = request.POST["answer"]

            answer = Answer.objects.filter(id=answer_id, question_id=question_id).first()

            if answer.is_correct:
                request.session['correct_answers'] = request.session['correct_answers'] + 1
            else:
                request.session['incorrect_answers'] = request.session['incorrect_answers'] + 1
                request.session['fails'] = request.session['fails'] + 1
        
        else:
            request.session['times_up'] = request.session['times_up'] + 1
            request.session['fails'] = request.session['fails'] + 1

    if request.session['fails'] == 3:
        print("Game Over")
        return  HttpResponseRedirect("/encuesta/quiz/results")

    questions = request.session['questions'];
    question_id = questions.pop()
    request.session['questions'] = questions;

    question = Question.objects.filter(id=question_id).first()
    answers = Answer.objects.filter(question=question).all()

    context = {
        'question': question,
        'answers': answers,
        'correct_answers': request.session['correct_answers'],
        'incorrect_answers': request.session['incorrect_answers'],
        'times_up': request.session['times_up'],
        'fails': request.session['fails']
    }
    
    return render(request, 'quiz.html', context)


def results(request):
    template = loader.get_template('results.html')
    context = {
        'user': request.session['user'],
        'correct_answers': request.session['correct_answers'],
        'incorrect_answers': request.session['incorrect_answers'],
        'times_up': request.session['times_up'],
        'fails': request.session['fails']
    }
    return HttpResponse(template.render(context, request))


def categories(request):
    topics = Topic.objects.all()
    template = loader.get_template('categories.html')
    context = {
        'topics': topics,
    }
    return HttpResponse(template.render(context, request))


def category(request, id):
    topic = Topic.objects.filter(id=id).first()
    template = loader.get_template('category.html')
    context = {
        'topic': topic,
    }
    return HttpResponse(template.render(context, request))