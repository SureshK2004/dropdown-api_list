class LocationListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

            branches = LocationList.objects.filter(
                org_id=org_id,
                status=1
            ).select_related('client', 'site').order_by('name')

           
            data = []
            for b in branches:
                client_name = b.client.client_name if b.client and hasattr(b.client, "client_name") else ""
                site_name = b.site.site_name if b.site and hasattr(b.site, "site_name") else ""
                base_name = b.name if b.name else ""

                
                if client_name and base_name:
                    display_name = f"{client_name} - {base_name}"
                elif site_name and base_name:
                    display_name = f"{site_name} - {base_name}"
                else:
                    display_name = base_name or client_name or site_name or "Unnamed"

                data.append({
                    "id": b.id,
                    "name": display_name
                })

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