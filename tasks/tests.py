from django.test import TestCase
from .models import Task
from datetime import date

class TaskListViewTests(TestCase):
    def setUp(self):
        Task.objects.create(title="Test Task 1", description="Description 1", due_date=date(2024, 1, 1), priority=1, status="To Do")
        Task.objects.create(title="Test Task 2", description="Description 2", due_date=date(2024, 2, 1), priority=2, status="Done")

    def test_filter_by_status(self):
        response = self.client.get('/tasks/?status=To Do')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task 1")
        self.assertNotContains(response, "Test Task 2")

    def test_sort_by_priority(self):
        response = self.client.get('/tasks/?sort_by=priority')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task 1")
        self.assertContains(response, "Test Task 2")

    def test_sort_by_due_date(self):
        response = self.client.get('/tasks/?sort_by=due_date')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task 1")
        self.assertContains(response, "Test Task 2")

