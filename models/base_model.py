import uuid
from datetime import datetime


class BaseModel:
    """
    A base class for all models, providing common attributes and methods.

    Attributes:
        id (str): A unique identifier for each instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        Sets the id to a unique UUID, and initializes created_at and updated_at
        with the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the instance.
        
        Returns:
            str: A string in the format [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance.
        
        Returns:
            dict: A dictionary containing all keys/values of the instance's __dict__,
                  with created_at and updated_at as ISO format strings, and an
                  additional '__class__' key with the class name of the instance.
        """
        # Create a dictionary with all the instance attributes
        instance_dict = self.__dict__.copy()
        # Add the class name to the dictionary
        instance_dict['__class__'] = self.__class__.__name__
        # Convert created_at and updated_at to ISO format strings
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict
