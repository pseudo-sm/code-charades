from django.shortcuts import render
from django.http import JsonResponse
from .models import Questions,Submissions
# Create your views here.
from random import randint
import requests
def index(request):
    
    questions = list(Questions.objects.filter(type="1").values("type","question","description","props"))
    i = randint(0,len(questions)-1)
    request.session["next"] = "2"
    print(questions[i])
    return render(request,"index.html",{"question":questions[i]})

def fetch(request):

    questions = list(Questions.objects.filter(type=request.session["next"]).values("type","question","description","props"))
    request.session["next"] = "3"
    i = randint(0,len(questions)-1)
    print(questions[i])
    return JsonResponse({"question":questions[i]})

def code(request):

    return render(request,"code.html")

url = "https://api.hackerearth.com/v3/code/compile/"
run_url = "https://api.hackerearth.com/v3/code/run/"


def gfg_compile(lang, code, _input=None, save=False):
    data = {
      'lang': lang,
      'source': code,
      "client_secret" : "9e94c82bb37aad13733fa9815ab23bfe522b6520",
      "input" : _input
    }

    r = requests.post(url,data=data)
    r = requests.post(run_url,data=data)
    return r

def compile(request):

    lang = request.GET.get("lang")
    code = request.GET.get("code")
    input = request.GET.get("input")
    result = gfg_compile(lang,code,input)
    print(result.json())
    return JsonResponse({"output" : result.json()},safe=False)


def editor(request):

    return render(request,"editor.html")


def start(request):
    p1 = request.GET.get("p1")
    p2 = request.GET.get("p2")
    id = request.GET.get("id")
    problem = Problems.objects.get(sl=id)
    submission = Submissions(player1=p1,player2=p2,question=problem)
    submission.save()
    return JsonResponse({"uc":submission.pk},safe=False)

def start_exam(request):
    yn = request.GET.get("yn")
    pn = request.GET.get("pn")
    request.session["yn"] = yn
    request.session["pn"] = pn
    return JsonResponse(True,safe=False)

def submit(request):

    yn = request.session["yn"]
    pn = request.session["pn"]
    code = request.GET.get("code")
    submission = Submissions.objects.create(name=yn,partner_name=pn,code=code)
    return JsonResponse(submission.pk,safe=False)