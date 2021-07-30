from django.urls import path
from .views import home
from .Apiviews import PollList,PollDetaiil,PollListg,PollDetailg,ChoiceApiView,VoteApiView,Choicelist,CreateVote,PollViewSet,UserCreate,LoginView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, 'polls')

urlpatterns = [
    path('list/',PollList.as_view(),name="polls_list"),
    path('detail/<int:id>/',PollDetaiil.as_view(),name="polls_detail"),
    
    #url for generic
    path('listg/',PollListg.as_view()),
    path('detailg/<int:pk>/',PollDetailg.as_view()),
    path('choice/',ChoiceApiView.as_view(),name="choice_list"),
    path('vote/',VoteApiView.as_view(),name="create_vote"),

    #new url
    path('polls/<int:pk>/choice/',Choicelist.as_view(),name="choice_lists"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',CreateVote.as_view()),

    path('user/',UserCreate.as_view(),name="user_create"),
    path('login/',LoginView.as_view(),name="login"),

] + router.urls