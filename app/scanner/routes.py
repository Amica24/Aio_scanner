from app.scanner import views


def setup_routes(app):
    """
    set up url routes for scanner app
    """
    app.router.add_get('/scan/{ip}/{begin_port}/{end_port}/', views.handle)
