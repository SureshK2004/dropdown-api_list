class UserListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

         
            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

          
            users = UserMasterDetails.objects.filter(
                org_id=org_id,
                active_status=1,
                status=1
            ).order_by('full_name')

           
            data = [
                {
                    "id": user.id,
                    "name": f"{user.full_name} - {user.emp_Id}".strip(" -")  
                }
                for user in users
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