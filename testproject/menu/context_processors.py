def menu_context_processor(request):
    return {'current_path': request.path}
