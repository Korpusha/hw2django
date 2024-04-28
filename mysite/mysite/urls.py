from django.urls import path
from myapp.views import main, article, article_number, article_slug


urlpatterns = [
    path('', main, name='main_page'),
    path('article/', article),
    path('article/<int:article_id>', article_number),
    path('article/<int:article_id>/<slug:article_sl>', article_slug)

]
