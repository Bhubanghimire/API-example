from django.urls import path
from .views import home
from .Apiviews import PollList,PollDetaiil,PollListg,PollDetailg,ChoiceApiView,VoteApiView

urlpatterns = [
    path('list/',PollList.as_view()),
    path('detail/<int:id>/',PollDetaiil.as_view()),
    
    #url for generic
    path('listg/',PollListg.as_view()),
    path('detailg/<int:pk>/',PollDetailg.as_view()),
    path('choice/',ChoiceApiView.as_view()),
    path('vote/',VoteApiView.as_view()),
]