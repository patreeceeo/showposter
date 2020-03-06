from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('id', 'image')

class UploadedImageView(viewsets.ModelViewSet):
    serializer_class = UploadedImageSerializer
    queryset = UploadedImage.objects.all()

class UnusedUploadedImageView(viewsets.ReadOnlyModelViewSet):
    serializer_class = UploadedImageSerializer
    queryset = UploadedImage.objects.filter(post=None)

@api_view(http_method_names=['delete'])
def bulk_delete_uploaded_image(request):
    print(repr(request.data))
    UploadedImage.objects.filter(pk__in=request.data).delete()
    return Response(status=200)
