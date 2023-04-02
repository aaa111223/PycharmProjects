from locust import HttpUser,HttpLocust,task,between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task
    def about(self):
        self.client.get("/about")

    @task(3)
    def contact(self):
        self.client.post("/contact", {"name": "John", "email": "john@example.com", "message": "Hello"})

    def on_start(self):
        self.client.post("/login", {"username": "testuser", "password": "testpass"})

