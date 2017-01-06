from flask import url_for

class TestApp: 
    '''Test App'''
    def test_app_is_running(self, app_client):
        response = app_client.get('/')
        assert response.status_code == 200
