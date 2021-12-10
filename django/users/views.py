from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomUserCreate(APIView):    # register
    permission_classes = [AllowAny]
    
    def post(self, request):
        req_serializer = RegisterUserSerializer(data=request.data)
        
        if req_serializer.is_valid():
            new_user = req_serializer.save()
            
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
            
        return Response(
            req_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
        
        
class BlackListTokenView(APIView):  # logout
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, AllowAny]
    
    def post(self, request, *args, **kwargs):
        try: 
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            
            return Response(status=status.HTTP_205_RESET_CONTENT)
        
        except Exception as ex:
            return Response(status=status.HTTP_400_BAD_REQUEST)