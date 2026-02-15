from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import login ,logout_view,verify_code_view,signup,profile_view,second_view,chats,hisobot,salary_menu_view,salary_calc_view1,salary_calc_view,salary_calc_manual_view



urlpatterns = [
    # Kirish va chiqish
    path('', login, name='Login'),
    path('logout/', logout_view, name='logout'),
    path('verify-code/', verify_code_view, name='verify_code'),

    # Ro'yxatdan o'tish
    path('signup/', signup, name='Sign Up'),

    # Foydalanuvchi qismlari
    path('profile/', profile_view, name='Profil'),
    path('second/', second_view, name='second_page'),
    path('chats/', chats, name='Chatlar'),
    path('hisobot/', hisobot, name='Hisobotlar'), # Name to'g'irlandi

    # Oylik kalkulyatorlari va menyusi
path('okladmenu/', salary_menu_view, name='salary_menu'),
path('Conculator/', salary_calc_view, name='salary_calc_high'),       # 20%
path('Kankulyator_Auto/', salary_calc_view1, name='salary_calc_low'),  # 40%
path('Kankulyator/', salary_calc_manual_view, name='salary_manual'),
]

# Media va Static fayllar uchun (Rasm va CSS chiqishi uchun)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)