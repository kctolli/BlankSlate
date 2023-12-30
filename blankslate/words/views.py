from django.http import HttpResponse
from django.template import loader

from .models import Word

from lib.date import Date
from lib.randomint import randomint

def all(request):
  """
  Retrieves all the words from the Word model and renders them in a template.
  
  Parameters:
    request (HttpRequest): The HTTP request object.
    
  Returns:
    HttpResponse: The rendered template containing all the words and the current year.
  """
  allwords = Word.objects.all().values()
  template = loader.get_template('all_words.html')
  context = {
    'allwords': allwords,
    'year': Date().getCurrentYear()
  }
  return HttpResponse(template.render(context, request))

def word(request):
  """
  Retrieves a specific word from the database and renders it on the 'card.html' template.
  
  Args:
    request (HttpRequest): The HTTP request object.
  
  Returns:
    HttpResponse: The rendered template with the word and the current year.
  """
  id = randomint(Word.getMaxId(Word))
  word = Word.objects.get(id=id)
  template = loader.get_template('word.html')
  context = {
    'word': word,
    'year': Date().getCurrentYear()
  }
  return HttpResponse(template.render(context, request))

def main(request):
  """
  Renders the 'main.html' template.
  
  Args:
    request (HttpRequest): The HTTP request object.
  
  Returns:
    HttpResponse: The rendered template.
  """
  template = loader.get_template('main.html')
  context = {
    'year': Date().getCurrentYear()
  }
  return HttpResponse(template.render(context, request))
