from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pik/<int:pk>', views.pikDetail, name='detail'),
    path('pik/<int:pik>/update', views.updatePik, name='updatePik'),   
    path('pik/<int:pik>/k-0', views.tambahKNol, name='KNol'),
    path('pik/<int:pik>/anggota', views.listAnggota, name='anggota'),
    path('pik/<int:pik>/anggota/<int:pk>/update', views.updateAnggota, name='updateAnggota'),
    path('pik/<int:pik>/laporan/baru', views.tambahLaporan, name='tambahLaporan'),
    path('pik/<int:pik>/anggota/baru', views.tambahAnggota, name='tambahAnggota'),
    
    path('listPik/', views.listPik, name='listPik'),
    path('pik/<int:pik>/laporan/cetak', views.viewLaporanPik, name='laporanPik'),
    
    path('login/', views.loginView, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]