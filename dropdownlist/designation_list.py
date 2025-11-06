class DesignationListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

            
            designations = Designation.objects.filter(
                org_id=org_id,
                status=1
            ).order_by('designation')

            data = [
                {
                    "id": desg.id,
                    "designation": desg.designation
                }
                for desg in designations
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