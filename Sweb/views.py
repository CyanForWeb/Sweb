from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import datetime, date
import random
from random import randrange
from .models import *
from django.http import JsonResponse

def home(request):
    Test.objects.all().delete()
    return render(request, 'html/home.html',)

def add(request):
    if request.method == 'POST':
        if "save" in request.POST: #ボタンが押されたら...
            attribute = request.POST.get('attribute')
            content = request.POST.get('content')
            img = request.POST.get('image')
            correct = request.POST.get('correct')
            incorrect_1 = request.POST.get('incorrect_1')
            incorrect_2 = request.POST.get('incorrect_2')
            incorrect_3 = request.POST.get('incorrect_3')
            incorrect_4 = request.POST.get('incorrect_4')
            incorrect_5 = request.POST.get('incorrect_5')
            discription = request.POST.get('discription')
            Questions.objects.create(title=attribute,
                                    question=content,
                                    image=img,
                                    correct=correct,
                                    incorrect_1=incorrect_1,
                                    incorrect_2=incorrect_2,
                                    incorrect_3=incorrect_3,
                                    incorrect_4=incorrect_4,
                                    incorrect_5=incorrect_5,
                                    discription=discription
                                    )
            return render(request, 'html/add_end.html',)
    return render(request, 'html/add.html',)

def pdf(request):
    return render(request, 'html/pdf.html',)

def test_start(request):
    incorrect_id = Test.objects.all().delete()
    questions = list(Questions.objects.all())
    if request.method == 'POST':
        if "start" in request.POST:
            return redirect('next_question',0)
    return render(request,'html/test_start.html',{'length':len(questions)})

def next_question(request, question_index):
    incorrect_id = Test.objects.all()
    questions = list(Questions.objects.all())
    random_questions = random.sample(questions,k=len(questions))#シャッフル
    current_question = random_questions[question_index]#現在の問題内容
    if question_index < len(questions) - 1:
        return render(request, 'html/test.html',
        {'incorrect_id':incorrect_id,'length':len(questions), 'question_index': question_index + 1, 'show_finish_button': False, 'current_question': current_question})
    else:
        return render(request, 'html/test.html',
        {'incorrect_id':incorrect_id,'length':len(questions),'questions': questions, 'question_index': question_index + 1, 'show_finish_button': True, 'current_question': current_question})

def create_test_instance(request, question_index):
    # Testモデルの新しいインスタンスを作成
    test_instance = Test(question_id=question_index)
    test_instance.save()
    return JsonResponse({'status': 'success'})

def quiz_complete(request):
    incorrect_id = Test.objects.all()
    questions = list(Questions.objects.all())
    length_correct = len(questions) - len(incorrect_id)
    return render(request, 'html/quiz_complete.html',{'length_correct':length_correct,'incorrect_id':incorrect_id,'length':len(questions)})

def incorrect(request):
    incorrect_list = Test.objects.all()
    questions = Questions.objects.all()
    return render(request, 'html/incorrect.html',{'incorrect_list':incorrect_list,'questions':questions})

def video(request):
    return render(request, 'html/video.html',)
