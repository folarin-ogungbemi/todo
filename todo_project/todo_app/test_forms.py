from django.test import TestCase
from .forms import TodoForm

# Create your tests here.


class TestTodoForm(TestCase):
    def test_todo_name_is_required(self):
        form = TodoForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_todo_content_is_required(self):
        form = TodoForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = TodoForm({
            'name': 'name successful',
            'content': 'content succesful'})
        self.assertTrue(form.is_valid)

    def test_fields_are_explicit_in_form_metaclass(self):
        form = TodoForm()
        self.assertEqual(form.Meta.fields, ['name', 'content', 'done'])
        