from django.http import HttpResponse
from django.template import loader
from .models import Word

from datetime import datetime
currentYear = datetime.now().year

def words(request):
  allwords = Word.objects.all().values()
  template = loader.get_template('all_words.html')
  context = {
    'words': allwords,
    'year': currentYear
  }
  return HttpResponse(template.render(context, request))

def card(request):
  id = 1
  word = Word.objects.get(id=id)
  template = loader.get_template('card.html')
  context = {
    'word': word,
    'year': currentYear
  }
  return HttpResponse(template.render(context, request))
