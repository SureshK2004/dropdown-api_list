class ZoneListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

          
            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

       
            zones= ZoneMaster.objects.filter(
                org_id=org_id,
                status=1
            ).order_by('zone_name')

            data = [
                {
                    "id": z.id,
                    "zone_name": z.zone_name
                }
                for z in zones
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
