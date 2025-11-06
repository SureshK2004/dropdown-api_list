class DepartmentListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

         
            departments = Departments.objects.filter(org_id=org_id, status=1).order_by('department')

            data = [
                {
                    "id": dept.id,
                    "department": dept.department
                }
                for dept in departments
            ]

            return Response({
                "status": "success",
                "count": len(data),
                "results": data
            })

        except Exception as e:
            return Response({
                "status": "error",
                "message": str(e)
            }, status=500)
            
            
            
#urls
path('api/dept_list/',views.DepartmentListAPI.as_view(),name='department-list')