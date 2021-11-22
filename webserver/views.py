from django.shortcuts import render

from .forms import SearchForm


def home(request):
    return render(request, './home.html')


def search(request, autoescape):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            if (autoescape):
                return render(request, './searchwithautoescape.html', {'form': form, 'search_value': request.POST['your_name']})
            else:
                return render(request, './searchwithoutautoescape.html', {'form': form, 'search_value': request.POST['your_name']})

    else:
        form = SearchForm()

    if (autoescape):
        return render(request, './searchwithautoescape.html', {'form': form, 'search_value': ""})
    else:
        return render(request, './searchwithoutautoescape.html', {'form': form, 'search_value': ""})
