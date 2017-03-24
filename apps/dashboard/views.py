from django.shortcuts import render, redirect, reverse
from .models import Quote, Favorite
from django.contrib import messages


def index(request):
    if 'user_id' in request.session:

        user=request.session['user_id']

        context={
            'quotes': Quote.objects.all(),
            'fav': Favorite.objects.filter(user_fav=user)
            }
    return render(request, 'dashboard/index.html', context)

def quote(request):
    title=request.POST['html_title']
    quote=request.POST['html_quote']
    auth = True

    if len(title)<1:
        auth=False
        messages.add_message(request,messages.ERROR,'Title is too short')
    elif len(quote)<1:
        auth  = False
        messages.add_message(request,messages.ERROR,'Quote is too short')
    elif auth == True:
        Quote.objects.create(quote_by=title, quote=quote, quote_creator_id=request.session['user_id'])

    return redirect('Board:Home')
def favorites(request, fav_id):
    
    Favsorite.objects.create(favorite_id=fav_id, user_fav_id=request.session['user_id'])
    
    return redirect('Board:Home')

# def remove(request, fav_id):
    # Favorite.objects.filter(favorite_id=fav_id, user_fav_id=request.session['user_id']).delete()
    # return redirect('Board:Home')




