from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)
    @task
    def test_obtener_historial(self):
        path = "fallos/2"
        self.client.get(path)
        

    @task
    def test_obtener_inspeccion(self):
        path = "inspeccion/2"
        self.client.get(path)