from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person,Question
from .serializers import PersonSerializer,QuestionSerializer,AnswerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status,generics
from permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator


class HomeView(APIView):
    # permission_classes = [IsAuthenticated,]

    def get(self,request):
        queryset = Person.objects.all()
        page_num = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('limit', 2)
        paginator = Paginator(queryset,page_size)
        serializer = PersonSerializer(instance=paginator.page(page_num),many=True)
        return Response(serializer.data)


class Paginatorr(PageNumberPagination):
    page_size = 2


class HomePagination(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    pagination_class = Paginator



class QuestionsListView(APIView):
    def get(self,request):
        questions = Question.objects.all()
        srz_data = QuestionSerializer(instance=questions,many=True).data
        return Response(srz_data,status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    """
        Create a new question
    """
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self,request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly,]

    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question,data=request.data , partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly,]

    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        question.delete()
        return Response({'message':'The question was deleted'})


