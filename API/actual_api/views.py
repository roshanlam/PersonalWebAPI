from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import urllib.request, json , codecs, glob, os


def index(request):
    return HttpResponse("Hello World, this is Roshan Lamichhane's API for his perspnal website")

def getProjectInfos(request):
    with urllib.request.urlopen("https://api.github.com/users/roshanlam/repos?page={page_num") as url:
        data = json.loads(url.read())
        # keywords = ['name', 'git_url', 'language']
        keywords = ['name']
        data = [i[k] for i in data for k in keywords]
        print(data)
        try:
            with open('projects' + '.json', 'w+') as dataNameFile:
                json.dump(data, dataNameFile)
        except FileNotFoundError:
            with open('projects' + '.json', 'w+') as dataNameFile:
                json.dump(data, dataNameFile)

        path = os.getcwd()
        json_files = glob.glob(os.path.join(path + "projects.json"))
        for info in json_files:
            data = info
    return HttpResponse(data, content_type='application/json')

def readFile(path, encoding='utf-8'):
    with codecs.open(path, 'r', encoding=encoding) as file:
        try:
            content = file.read()
        except UnicodeDecodeError as e:
            raise Exception("%s: %s" % (e, path))
    return content