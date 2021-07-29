from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll,Choice,Vote
from .serializers import PollSerializers,ChoiceSerializers,VoteSerializers,UserSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics,status
from rest_framework import viewsets
from django.contrib.auth import authenticate


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


#new refined
class Choicelist(generics.ListCreateAPIView):

    def get_queryset(self):
        print("run")
        queryset= Choice.objects.filter(poll_id=self.kwargs["pk"])
        return queryset

    serializer_class = ChoiceSerializers


class CreateVote(APIView):
    serializer_class = VoteSerializers

    def post(self,request,pk,choice_pk):
        print(pk)
        poll = Poll.objects.get(pk=pk)
        choice = Choice.objects.get(pk=choice_pk)
        voted_by = request.data.get("voted_by")
        
        
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}  
       
        serializer = VoteSerializers(data=data)

        if serializer.is_valid():

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializers



class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializers


class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)