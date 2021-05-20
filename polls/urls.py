from django.urls import path

from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView

from rest_framework.routers import DefaultRouter



router = DefaultRouter()

router.register('polls', PollViewSet, basename='polls')


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='polls_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='polls_list'),
]

urlpatterns += router.urls
