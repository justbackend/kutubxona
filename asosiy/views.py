from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout

# User = get_user_model()


from django.http import HttpResponse
# Create your views here.

def muallif(request):
    if request.method == "POST":
        forma = MuallifModelForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("/muallif/")

    ism = request.GET.get('ism')
    if ism:
        natija = Muallif.objects.filter(ism__contains=ism)
    else:
        natija = Muallif.objects.all()
    content = {
        'mualliflar': natija,
        "forma": MuallifForm,
    }
    return render(request, "muallif.html", content)

def talaba(request):
    if request.method == "POST":
        forma = TalabaForm(request.POST)
        if forma.is_valid():
            Talaba.objects.create(
                ism = forma.cleaned_data.get("i"),
                kurs = forma.cleaned_data.get("k"),
                kitoblar_soni = forma.cleaned_data.get(("k_s"))
            )

            return redirect("/talaba/")
    content = {
        'talaba': Talaba.objects.all(),
        'kitobi_bor': Talaba.objects.filter(kitoblar_soni__gt=0),
        "forma": TalabaForm(),
    }
    return render(request, 'talaba.html', content)


def all_books(request):
    if request.method == "POST":
        forma = KitobForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("/all_books/")
    content = {
        "kitoblar": Kitob.objects.all(),
        "forma": KitobForm()
    }

    return render(request, "all_books.html", content)

def names_with_a(request):
    content = {
        "names": Talaba.objects.filter(ism__contains="a")
    }

    return render(request, "names_with_a.html", content)

def records(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            forma = RecordForm(request.POST)
            if forma.is_valid():
                forma.save()
            return redirect("/records/")
        ism = request.GET.get("ism")
        if ism:
            natija = Record.objects.filter(talaba__ism__contains=ism)
        else:
            natija = Record.objects.all()

        content = {
            "talabalar": Talaba.objects.all(),
            "kitoblar": Kitob.objects.all(),
            "adminlar": Admin.objects.all(),
            "records": natija,
            "forma": RecordForm()
        }

        return render(request, "records.html", content)
    else:
        return redirect("/login/")

def alive_writers(request):
    content = {
        "writers": Muallif.objects.filter(tirik=True)
    }

    return render(request, "alive_writers.html", content)

def show_number(request, id):
    content = {
        'talaba': Talaba.objects.get(id=id)
    }

    return render(request, "show_number.html", content)

def delete_student(request, talaba_id):
    Talaba.objects.get(id=talaba_id).delete()
    return redirect("/talaba/")

def qidirish(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism = request.POST.get("ism"),
            kurs = request.POST.get("kurs"),
            kitoblar_soni = request.POST.get("kitoblar_soni"),
        )
        return redirect("/talabalar/")

    qidiruv_sozi = request.GET.get('ism')
    if qidiruv_sozi:
        talaba = Talaba.objects.filter(ism__contains=qidiruv_sozi)
    else:
        talaba = Talaba.objects.all()

    content = {
        "talabalar": talaba
    }

    return render(request, 'talabalar.html', content)


def delete_muallif(request, muallifning_idisi):
    Muallif.objects.get(id=muallifning_idisi).delete()

    return redirect("/muallif/")

def delete_records(request, record_id):
    Record.objects.get(id=record_id).delete()

    return redirect("/records/")

def adminn(request):
    if request.method == "POST":
        forma = AdminForm(request.POST)
        if forma.is_valid():
            Admin.objects.create(
                ism = forma.cleaned_data.get("ism"),
                ish_vaqti=forma.cleaned_data.get("ish_vaqti")
            )
        return redirect("/adminka/")
    content = {
        "adminlar": Admin.objects.all(),
        "forma": AdminForm()
    }

    return render(request, "admin.html", content)

def talaba_update(request, pk):
    if request.method == "POST":
        Talaba.objects.filter(id=pk).update(
            kurs = request.POST.get("kurs"),
            kitoblar_soni = request.POST.get("kitoblar_soni")
        )
        return redirect("/talabalar/")
    content = {
        "talaba": Talaba.objects.get(id=pk)
    }

    return render(request, 'talaba_edit.html', content)

def kitob(request, pk):
    if request.method == "POST":
        Kitob.objects.filter(id=pk).update(sahifa=request.POST.get('sahifa'))
        return redirect("/all_books/")
    content = {
        "kitoblar": Kitob.objects.all()
    }

    return render(request, 'kitob.html', content)

def admin_edit(request, pk):
    if request.method == "POST":
        Admin.objects.filter(id=pk).update(ish_vaqti=request.POST.get("ish_vaqti"))
        return redirect("/adminka/")
    content = {
        "adminlar": Admin.objects.get(id=pk)
    }

    return render(request, "admin_edit.html", content)

def muallif_edit(request, pk):
    if request.method == "POST":
        Muallif.objects.filter(id=pk).update(
            kitob_soni = request.POST.get("kitob_soni"),
        )
        return redirect("/muallif/")
    content = {
        "mualliflar": Muallif.objects.get(id=pk)
    }

    return render(request, "muallif_edit.html", content)

def record_edit(request, pk):
    if request.method == "POST":
        Record.objects.filter(id=pk).update(qaytarish_sana=request.POST.get("qaytarish_sana"))
        return redirect("/records/")
    content = {
        "recordlar": Record.objects.get(id=pk)
    }

    return render(request, "record_edit.html", content)

def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['login'],
            password=request.POST['parol']
        )
        if user is None:
            return redirect("/login/")
        login(request, user)
        return redirect("/muallif/")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("/login/")



