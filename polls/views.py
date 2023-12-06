# views.py
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework import status
from .models import UploadedImage
from .serializers import UploadedImageSerializer
from detect import run
from models.common import DetectMultiBackend
from utils.torch_utils import select_device
import os
import gdown


def download_trained_weights():
    file_url = "https://drive.google.com/uc?export=download&id=1p_DrK0w5SYebJ21scnyNdjV1Fr8-sdUx"
    file_name = "best.pt"

    # Check if the file already exists in the directory
    if not os.path.exists(file_name):
        # If the file doesn't exist, download it using gdown
        gdown.download(file_url, file_name, quiet=False)
        print(f"{file_name} downloaded successfully.")
    else:
        print(f"{file_name} already exists in the directory. No need to download.")
    
download_trained_weights()

device = select_device('0')
global model
model = DetectMultiBackend(weights=r"best.pt", device=device, dnn=False, data='', fp16=False)
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_image(request):
    if request.method == 'POST':
        serializer = UploadedImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            predicted_result=run(source=serializer.data['image'],weights='yolov5x.pt',model=model)
            return Response({'name of the detected plant':predicted_result}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
