from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ClassForm
from .models import DjangoClasses


def admin_console(request):
    classes = DjangoClasses.objects.all()
    return render(request, 'classes/schedule.html', {'classes': classes})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(DjangoClasses, pk=pk)
    form = ClassForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'classes/show_classes.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(DjangoClasses, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item,}
    return render(request, "classes/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates a form instance and binds data to it
        form = ClassForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def createRecord(request):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ClassForm()
    context = {
        'form': form,
    }
    return render(request, 'classes/createClass.html', context)