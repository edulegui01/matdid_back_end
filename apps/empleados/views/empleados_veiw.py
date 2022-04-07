from rest_framework import viewsets, status
from rest_framework.response import Response
from apps.empleados.serializers.empleados_serializer import EmpleadosSerializer
from apps.empleados.models import Empleado
from apps.empleados.serializers.empleados_all_serializer import EmpleadoAllSerializer



class EmpleadoViewSet(viewsets.ModelViewSet):
    serializer_class = EmpleadosSerializer
    queryset = Empleado.objects.filter(state = True).order_by('-id')


    def create(self,request):
        empleado_serializer = EmpleadosSerializer(data=request.data)
        if empleado_serializer.is_valid():
            empleado_serializer.save()
            return Response({'message':'El empleado se creo con éxito.'},status = status.HTTP_200_OK)
        return Response(empleado_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk):
        query_all = Empleado.objects.filter(state = True, id = pk).first()
        empleado_retrive_serializer = EmpleadoAllSerializer(query_all)

        return Response(empleado_retrive_serializer.data,status = status.HTTP_200_OK)


    def update(self, request, pk):
        query_edit_product = Empleado.objects.filter(state = True, id=pk).first()
        product_serializer_edit = EmpleadosSerializer(query_edit_product,data=request.data)
        if product_serializer_edit.is_valid():
            product_serializer_edit.save()
            return Response({'message':'El empleado se ha editado correctamente'},status = status.HTTP_200_OK)
        return Response({'message':'No se pudo editar el empleado'})

    def destroy(self,request, pk=None):
        query_empleado_delete = Empleado.objects.filter(id=pk).first()
        print(query_empleado_delete.state)
        
        if query_empleado_delete:
            query_empleado_delete.state = False
            query_empleado_delete.save()
            return Response({'mensaje':'empleado eliminado'},status = status.HTTP_200_OK)
        return Response({'mensaje':'No existe ese empleado'},status = status.HTTP_400_BAD_REQUEST)