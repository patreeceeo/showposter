from rest_framework import viewsets, serializers
from posts.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = UploadedImage
    fields = ('id', 'image')

class UploadedImageRESTView(viewsets.ModelViewSet):
  serializer_class = UploadedImageSerializer
  queryset = UploadedImage.objects.all()

