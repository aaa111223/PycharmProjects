from locust import FastHttpUser,Events,TaskSet


class Taskuser(TaskSet):
    def on_start(self):
        result = {}
        list = []
        user = []

