from django.test import TestCase
from .models import Todo


class TestTodoModels(TestCase):
    def test_done_default_is_false(self):
        todo = Todo.objects.create(name='test', content='testing test')
        self.assertFalse(todo.done)
    
    def test_todo_return_string_is_name(self):
        todo = Todo.objects.create(name='test', content='testing test')
        self.assertEqual(str(todo), todo.name)
