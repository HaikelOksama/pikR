from django.shortcuts import redirect, render
from .models import PikR, Pengurus, LaporanKegiatan, Anggota, User
from .forms import LaporanPikForm, AnggotaPikForm, KNolForm, PikForm
from django.contrib import messages
# Create your views here

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        print(request.POST)
        usernameIn = request.POST['username']
        passwordIn = request.POST['password']
        
        user = authenticate(request, username = usernameIn, password=passwordIn)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password anda Salah!')
       
    return render(request, 'base/login.html')

def user_logOut(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
    
    return redirect('home')

@login_required(login_url='login/')
def index(request):
    try:
        modelsPik = PikR.objects.get(admin = request.user)
    except:
        modelsPik = PikR.objects.none()
    
    allPik = PikR.objects.all()
    if request.user.is_superuser:
        allKegiatan = LaporanKegiatan.objects.all()
    else:
        allKegiatan = LaporanKegiatan.objects.filter(pik = modelsPik)
    print(allPik)
    
    context= {
        'pik': modelsPik,
        'allPik': allPik,
        'kegiatan': allKegiatan
    }
    return render(request, 'base/index.html', context)

@login_required(login_url='login/')
def pikDetail(request, pk):
    modelsPik = PikR.objects.get(id=pk)
    
    print(modelsPik.admin)
    kegiatan = modelsPik.laporankegiatan_set.all()
    anggota = modelsPik.anggota_set.all()
    print(kegiatan)
    context = {
        'pik': modelsPik,
        'kegiatan' : kegiatan,
        'anggota' : anggota
    } 
    return render(request, 'base/detail.html', context)

@login_required(login_url='login/')
def updatePik(request, pik):
    modelsPik = PikR.objects.get(id=pik)
    if request.user != modelsPik.admin:
        return redirect('home')
    form = PikForm(instance = modelsPik)
    if request.method == 'POST':
        form = PikForm(request.POST, instance = modelsPik)
        if form.is_valid():
            form.save()
            messages.success(request, f'Pik {modelsPik.nama} Berhasil Diupdate')
            return redirect('detail', pik)
    context = {
        'pik': modelsPik,
        'form' : form
    }
    return render(request, 'base/updatePik.html', context)
    
            
@login_required(login_url='login/')
def tambahLaporan(request, pik):
    modelsPik = PikR.objects.get(id=pik)
    if request.user != modelsPik.admin:
        return redirect('home')
    form = LaporanPikForm()
    if request.method == 'POST':
        form = LaporanPikForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pik = modelsPik
            instance.save()
            messages.success(request, 'Laporan Berhasil Ditambahkan')
            return redirect('detail', pik)
    
    context = {
        'pik': modelsPik,
        'form' : form
    }
    return render(request, 'base/input_laporan.html', context)

@login_required(login_url='login/')
def tambahAnggota(request, pik):
    modelsPik = PikR.objects.get(id=pik)
    if request.user != modelsPik.admin:
        return redirect('home')
    form = AnggotaPikForm()
    if request.method == 'POST':
        form = AnggotaPikForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.pik = modelsPik
            instance.save()
            messages.success(request, 'Anggota Berhasil Ditambahkan')
            return redirect('detail', pik) 
    context = {
        'pik': modelsPik,
        'form' : form
    }
    return render(request, 'base/input_laporan.html', context)



@login_required(login_url='login/')
def tambahKNol(request, pik):
    modelsPik = PikR.objects.get(id=pik)
    if request.user != modelsPik.admin:
        return redirect('home')
    form = KNolForm(instance = modelsPik)
    if request.method == 'POST':
        form = KNolForm(request.POST, request.FILES, instance=modelsPik)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'K-0 Berhasil Ditambahkan')
            return redirect('detail', pik) 
        
    context = {
        'pik': modelsPik,
        'form' : form
    }
    return render(request, 'base/input_K0.html', context)

@login_required(login_url='login/')
def listAnggota(request, pik):
    modelsPik = PikR.objects.get(id=pik)
    anggota = modelsPik.anggota_set.all()
    if request.method == 'POST':
        try:
            instance = Anggota.objects.get(id =request.POST['delete'])
            instance.delete()
            messages.success(request, 'Anggota Berhasil Dihapus')
        except:
            return redirect('anggota', pik)
        
    context = {
        'pik': modelsPik,
        'anggota': anggota
    }
    return render(request, 'base/list_anggota.html', context)

@login_required(login_url='login/')
def updateAnggota(request, pik, pk):
    modelsPik = PikR.objects.get(id=pik)
    if request.user != modelsPik.admin:
        return redirect('home')
    
    anggota = modelsPik.anggota_set.get(id=pk)
    
    form = AnggotaPikForm(instance=anggota)
    if request.method == 'POST':
        form = AnggotaPikForm(request.POST, instance=anggota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Anggota Berhasil Diupdate')
            return redirect('anggota', pik) 
    context = {
        'anggota': anggota,
        'pik': modelsPik,
        'form' : form
    }
    return render(request, 'base/update_anggota.html', context)

@login_required(login_url='login/')
def listPik(request):
    modelsPik = PikR.objects.all()
    
    context = {
        'listPik': modelsPik
    }
    return render(request, 'base/list_pik.html', context)

@login_required(login_url='login/')
def viewLaporanPik(request, pik):
    modelsPik =PikR.objects.get(id=pik)
    laporanPik = modelsPik.laporankegiatan_set.all()
    context = {
        'pik': modelsPik,
        'kegiatan': laporanPik
    }
    
    return render(request, 'base/laporanPik.html', context)