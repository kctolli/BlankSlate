from django.http import HttpResponse
from django.template import loader

from .models import Word

from lib.date import Date
year = Date().getCurrentYear()

def all(request):
    """
    Retrieves all the words from the Word model and renders them in a template.
    
    Parameters:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered template containing all the words and the current year.
    """
    template = loader.get_template('all_words.html')
    return HttpResponse(
        template.render(
            {
                'allwords': Word.getAllWords(Word).values(),
                'count': Word.getMaxId(Word),
                'year': year
            }, 
            request
        )
    )

def word(request):
    """
    Retrieves a specific word from the database and renders it on the 'card.html' template.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered template with the word and the current year.
    """
    template = loader.get_template('word.html')
    return HttpResponse(
        template.render(
            {
                'word': Word.getRandomWord(Word),
                'year': year
            }, 
            request
        )
    )

def main(request):
    """
    Renders the 'main.html' template.
    
    Args:
        request (HttpRequest): The HTTP request object.
    
    Returns:
        HttpResponse: The rendered template.
    """
    template = loader.get_template('main.html')
    return HttpResponse(
        template.render({'year': year}, request)
    )
