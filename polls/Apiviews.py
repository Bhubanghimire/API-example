from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll,Choice,Vote
from .serializers import PollSerializers,ChoiceSerializers,VoteSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics

class PollList(APIView):
    def get(self,request):
        polls = Poll.objects.all()
        data = PollSerializers(polls,many=True).data
        print("bhuban")
        print(data)
        return Response(data)


class PollDetaiil(APIView):
    def get(self,request,id):
        pol = get_object_or_404(Poll,id=id)
        data = PollSerializers(pol).data
        print("bhuban")
        print(data)
        return Response(data)


#using generic views

class PollListg(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers


class PollDetailg(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers


class ChoiceApiView(generics.ListCreateAPIView):
    queryset =  Choice.objects.all()
    serializer_class = ChoiceSerializers


class VoteApiView(generics.CreateAPIView):
    serializer_class = VoteSerializers
    

    # queryset =  Vote.objects.all()
    # serializer_class = VoteSerializers