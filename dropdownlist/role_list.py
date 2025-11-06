from attendence.models import UserActiveInactiveMasterView         
class RoleListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

           
            roles = (
                UserActiveInactiveMasterView.objects
                .filter(org_id=org_id)
                .exclude(role_name__isnull=True)
                .exclude(role_name__exact="")
                .values('role_id', 'role_name')
                .distinct()
                .order_by('role_name')
            )

            
            data = [
                {
                    "id": r["role_id"],
                    "role_name": r["role_name"]
                }
                for r in roles
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