class ProjectListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

            print(f"Received org_id: {org_id}")

           
            projects = CreateProject.objects.filter(org__id=org_id).order_by('project_name')

            print(f"Found {projects.count()} projects for org_id={org_id}")

            data = [
                {
                    "id": project.id,
                    "project_name": project.project_name
                }
                for project in projects
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
