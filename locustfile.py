from locust import HttpUser, task, between

class UserLoadTest(HttpUser):
    wait_time = between(1, 3)

    @task
    def search_test(self):
        self.client.get("/search?q=car")

    @task
    def product_test(self):
        self.client.get("/product/138528017")
