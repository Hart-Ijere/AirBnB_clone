import unittest
from datetime import datetime
from time import sleep
from base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case with a new instance of BaseModel.
        """
        self.model = BaseModel()

    def test_instance_creation(self):
        """
        Test that a new instance of BaseModel is created with correct attributes.
        """
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_str_method(self):
        """
        Test the __str__ method to ensure it returns the correct string format.
        """
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_method(self):
        """
        Test the save method to ensure it updates the updated_at attribute.
        """
        old_updated_at = self.model.updated_at
        sleep(0.01)  # Ensure time has passed
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method to ensure it returns the correct dictionary representation.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_to_dict_additional_keys(self):
        """
        Test to_dict method to ensure it includes additional keys in the instance.
        """
        self.model.name = "Test"
        model_dict = self.model.to_dict()
        self.assertIn('name', model_dict)
        self.assertEqual(model_dict['name'], 'Test')

    def test_to_dict_no_private_keys(self):
        """
        Test to_dict method to ensure private attributes are not included.
        """
        self.model._private_attr = "Should not be in dict"
        model_dict = self.model.to_dict()
        self.assertNotIn('_private_attr', model_dict)

    def test_unique_id(self):
        """
        Test that each instance of BaseModel has a unique id.
        """
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)


if __name__ == '__main__':
    unittest.main()

