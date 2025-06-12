
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Card
from .forms import EditCardForm



def get_context(active_page):
    return {'active_page': active_page}

# this is a view for listing all the cards
def cards(request):
   # retrieving all the cards from the database
    cards = Card.objects.all()
    context = get_context('cards')
    # Добавляем карточки в контекст
    context['cards'] = cards
    return render(request, 'cards/cards.html', context)

# this is a view for listing a single card, it will take id as an argument
# this is a view for listing a single card
def card_detail(request, id):
    # querying a particular card by its id
    card = Card.objects.get(pk=id)
    context = {'card': card}
    return render(request, 'cards/card-detail.html', context)

# this is a list for adding a card
# this is a view for adding a card
def add_card(request):
    # checking if the method is POST
    if request.method == 'POST':
        # getting all the data from the POST request
        data = request.POST
        # getting the image
        image = request.FILES.get('image-file')
        # creating and saving the card
        card = Card.objects.create(
           title = data['title'],
           description = data['description'],
           associative_imagery = data['associative_imagery'],
           image = image
        )
        # going to the home page
        return redirect('home')
    return render(request, 'cards/add-card.html')

# this is a view for editing the card's info
# this is a view for editing the card's info
def edit_card(request, id):
    # getting the card to be updated
    card = Card.objects.get(pk=id)
    # populating the form with the card's information
    form = EditCardForm(instance=card)
    # checking if the request is POST
    if request.method == 'POST':
        # filling the form with all the request data 
        form = EditCardForm(request.POST, request.FILES, instance=card)
        # checking if the form's data is valid
        if form.is_valid():
            # saving the data to the database
            form.save()
            # redirecting to the home page
            return redirect('home')
    context = {'form': form}
    return render(request, 'cards/update-card.html', context)

# this is a view for deleting a card,it will take id as an argument
# this is a view for deleting a card
def delete_card(request, id):
    # getting the card to be deleted
    card = Card.objects.get(pk=id)
    # checking if the method is POST
    if request.method == 'POST':
        # delete the card
        card.delete()
        # return to home after a success delete
        return redirect('home')
    context = {'card': card}
    return render(request, 'cards/delete-card.html', context)

def home(request):
   # retrieving all the cards from the database

    return render(request, 'cards/home.html', {'active_page': 'home'})

def matirial(request):
   # retrieving all the cards from the database

    return render(request, 'cards/matirial.html', {'active_page': 'matirial'})

def projects(request):
    
    return render(request, 'cards/projects.html', {'active_page': 'projects'})

def your_view(request):
    card = Card.objects.first()  # Или логика для получения конкретной карточки
    return render(request, 'your_template.html', {'card': card})

