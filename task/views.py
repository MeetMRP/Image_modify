from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from PIL import Image
from django.contrib.sites.shortcuts import get_current_site

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
    
class ImageApi(generics.GenericAPIView):
    serializer_class = ImageSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        image1 = serializer.validated_data['image']

        im = Image.open(image1)
        Thumbnail  = im.resize((200, 300))
        Medium  = im.resize((500, 500))
        Large   = im.resize((1024, 768))
        Grayscale  = im.convert('L')

        Thumbnail.save('media/Thumbnail.jpg')
        Medium.save('media/Medium.jpg')
        Large.save('media/Large.jpg')
        Grayscale.save('media/Grayscale.jpg')

        current_site = get_current_site(request).domain
        Thumbnail = current_site+'/media/Thumbnail.jpg'
        Medium = current_site+'/media/Medium.jpg'
        Large = current_site+'/media/Large.jpg'
        Grayscale = current_site+'/media/Grayscale.jpg'

        return Response({
            'Thumbnail': Thumbnail,
            'Medium': Medium,
            'Large': Large,
            'Grayscale': Grayscale,
        })