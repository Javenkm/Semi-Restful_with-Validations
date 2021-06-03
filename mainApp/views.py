from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show


def index(request):
    return redirect('/shows')


def all_shows(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request, "all_shows.html", context)


def create_show(request):
    errors = Show.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f"/shows/{new_show.id}")
    else:
        new_show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            releaseDate = request.POST['releaseDate'],
            desc = request.POST['desc']
        )
        return redirect(f"/shows/{new_show.id}")


def new_show(request):
    return render(request, "new_show.html")


def display_show(request, show_id):
    context = {
        "show": Show.objects.get(id = show_id)
    }

    return render(request, "show.html", context)


def edit_show(request, show_id):
    context = {
        "show": Show.objects.get(id = show_id)
    }
    return render(request, 'edit_show.html', context)


def update_show(request, show_id):
    update = Show.objects.get(id = show_id)
    update.title = request.POST['title']
    update.network = request.POST['network']
    update.releaseDate = request.POST['releaseDate']
    update.desc = request.POST['desc']
    update.save()
    return redirect(f'/shows/{show_id}')


def delete_show(request, show_id):
    show = Show.objects.get(id = show_id)
    show.delete()

    return redirect('/shows')