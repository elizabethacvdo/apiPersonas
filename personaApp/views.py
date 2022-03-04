
from django.shortcuts import render


import rest_framework.request as request
import rest_framework.status as status
from rest_framework.views import APIView
from rest_framework.response import Response

from personaApp.models import persona
from personaApp.serializers import PersonaSerializer




# Create your views here.


class personaView(APIView):

    def post(self,request):
        dui2 = request.data.get('dui', None)
        print(dui2)
        serializer = PersonaSerializer(data=request.data)
        if dui2 is not None:
            per = persona.objects.filter(dui=dui2).first()
            if per is None:
                if serializer.is_valid():
                    serializer.save()
                    return Response({"mensaje":"se agrego una persona"},status = status.HTTP_201_CREATED)
                else:
                    return Response({"mensaje":"no fue posible agregar"},status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"mensaje":"el dui ya existe"},status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"mensaje":"debe ingresar un dui"},status = status.HTTP_400_BAD_REQUEST)
    #-------------------------------------------------------------------------------------------------------------------        
    def get(self,request,dui=None):
        if dui:
            per = persona.objects.get(dui=dui)
            serializer = PersonaSerializer(per)
          
            return Response({"mensaje":"persona encontrada","persona":serializer.data},status = status.HTTP_200_OK)
        else:
            per = persona.objects.all()
            serializer = PersonaSerializer(per,many=True)
            return Response({"mensaje":"lista personas","personas":serializer.data},status = status.HTTP_200_OK)
            
    #-------------------------------------------------------------------------------------------------------------------

    def put(self,request,dui):
        dui2 = request.data.get('dui', None)
        
        if(dui==dui2):
            per = persona.objects.filter(dui=dui2).first()
            if per is not None:
                serializer = PersonaSerializer(per,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"mensaje":"modificacion exitosa"},status = status.HTTP_200_OK)
                else:
                    return Response({"mensaje":"ERROR"},status = status.HTTP_400_BAD_REQUEST)
                
            else:    
                return Response({"mensaje":"persona no encontrada"},status = status.HTTP_404_NOT_FOUND)
        else:
            return Response({"mensaje":"no se puede modificar el dui"},status = status.HTTP_400_BAD_REQUEST)

        
    #-------------------------------------------------------------------------------------------------------------------

    def delete(self,request,dui):
        per = list(persona.objects.filter(dui=dui).values())
        if len(per)>0:
            persona.objects.filter(dui=dui).delete()
            return Response({"mensaje":"eliminacion exitosa"},status = status.HTTP_200_OK)
        else:
            
            return Response({"mensaje":"persona no encontrada"},status = status.HTTP_404_NOT_FOUND)
