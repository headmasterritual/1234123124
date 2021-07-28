from locust import HttpLocust
from locust import TaskSet
from locust import task

# For HTML reporting
from locust.web import app
from src import report
app.add_url_rule('/htmlreport', 'htmlreport', report.download_report)

class Test_1(TaskSet):
    @task(1)
    def users(self):
        response = self.client.post("/posts", data=
        {
        "name": "Silence of the Lambs",
        "phone": "Thriller Book",
        "email": 1,
        "form_name": "Гарантии результата",
        "from_page": "https://sukhoff.com/"
        }
        )
