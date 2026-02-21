from django.shortcuts import render, redirect, get_object_or_404
from .models import Grocery


def index(request):
    items = Grocery.objects.all()
    edit_item = None

    if request.method == "POST":
        name = request.POST.get("name")
        item_id = request.POST.get("item_id")

        if item_id:
            item = Grocery.objects.get(id=item_id)
            item.name = name
            item.save()
        else:
            Grocery.objects.create(name=name)

        return redirect("/")

    edit_id = request.GET.get("edit")
    if edit_id:
        edit_item = Grocery.objects.get(id=edit_id)

    return render(request, "grocery/index.html", {
        "items": items,
        "edit_item": edit_item
    })


def delete_item(request, id):
    item = get_object_or_404(Grocery, id=id)
    item.delete()
    return redirect("/")


def toggle_complete(request, id):
    item = get_object_or_404(Grocery, id=id)
    item.completed = not item.completed
    item.save()
    return redirect("/")