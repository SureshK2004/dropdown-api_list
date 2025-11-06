class TaskListAPI(APIView):
    def get(self, request):
        try:
            org_id = request.query_params.get('org_id')

            if not org_id:
                return Response({"error": "org_id is required"}, status=400)

            tasks = TaskMaster.objects.filter(org_id=org_id).order_by('task_name')

            data = [
                {
                    "id": task.id,
                    "task_name": task.task_name
                }
                for task in tasks
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