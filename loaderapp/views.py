from django.views.generic import ListView
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from .models import Loader, TechService, Claims
from .serializers import *
from .permissions import IsAdminOrReadOnly


class LoaderAPIList(generics.ListCreateAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication, )
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )


class LoaderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class LoaderAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class LoaderAPIDestroy(generics.RetrieveDestroyAPIView, ):
    queryset = Loader.objects.all()
    serializer_class = LoaderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class TechServiceAPIList(generics.ListCreateAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TechServiceAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TechServiceAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )


class TechServiceAPIDestroy(generics.RetrieveDestroyAPIView, ):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ClaimsAPIList(generics.ListCreateAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ClaimsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ClaimsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ClaimsAPIDestroy(generics.RetrieveDestroyAPIView, ):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ModelLoaderAPIList(generics.ListCreateAPIView):
    queryset = ModelLoader.objects.all()
    serializer_class = ModelLoaderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ModelLoaderAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ModelLoader.objects.all()
    serializer_class = ModelLoaderSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ModelLoaderAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Loader.objects.all()
    serializer_class = ModelLoaderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class ModelLoaderAPIDestroy(generics.RetrieveDestroyAPIView, ):
    queryset = ModelLoader.objects.all()
    serializer_class = ModelLoaderSerializer
    permission_classes = (IsAdminOrReadOnly, )


class HomePageView(ListView):
    model = Loader
    template_name = 'home_page.html'

