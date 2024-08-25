#!/usr/bin/python3
"""
Module FileStorage
Defines the FileStorage class for serializing and deserializing instances to and from JSON files.
"""
import json
import models


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes instances from a JSON file.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Returns the dictionary of all objects, or only objects of a specific class if provided.

        Args:
            cls (type, optional): The class type to filter objects by. Defaults to None.

        Returns:
            dict: A dictionary of all objects, or filtered objects if cls is provided.
        """
        if cls is None:
            return self.__objects
        
        cls_name = cls.__name__ if isinstance(cls, type) else cls
        return {k: v for k, v in self.__objects.items() if k.startswith(cls_name + ".")}

    def new(self, obj):
        """
        Adds an object to the storage dictionary.

        Args:
            obj: The object to add.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists).
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                objects = json.load(f)
            for key, val in objects.items():
                class_name = models.classes[val["__class__"]]
                self.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects if it exists.

        Args:
            obj: The object to delete.
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)
            self.save()

    def close(self):
        """
        Calls the reload method to deserialize the JSON file to objects.
        """
        self.reload()

    def get(self, cls, id):
        """
        Retrieves an object by its class and ID.

        Args:
            cls (type): The class of the object.
            id (str): The ID of the object.

        Returns:
            object: The object if found, None otherwise.
        """
        key = f"{cls.__name__}.{id}"
        return self.__objects.get(key)

    def count(self, cls=None):
        """
        Counts the number of objects in storage or the number of objects of a specific class.

        Args:
            cls (type, optional): The class type to filter objects by. Defaults to None.

        Returns:
            int: The number of objects in storage, or filtered objects if cls is provided.
        """
        if cls is None:
            return len(self.__objects)
        
        cls_name = cls.__name__ if isinstance(cls, type) else cls
        return sum(1 for k in self.__objects if k.startswith(cls_name + "."))





# #!/usr/bin/python3
# '''
#     Define class FileStorage
# '''
# import json
# import models


# class FileStorage:
#     '''
#         Serializes instances to JSON file and deserializes to JSON file.
#     '''
#     __file_path = "file.json"
#     __objects = {}

#     def all(self, cls=None):
#         '''
#             Return the dictionary
#         '''
#         new_dict = {}
#         if cls is None:
#             return self.__objects

#         if cls != "":
#             for k, v in self.__objects.items():
#                 if cls == k.split(".")[0]:
#                     new_dict[k] = v
#             return new_dict
#         else:
#             return self.__objects

#     def new(self, obj):
#         '''
#             Set in __objects the obj with key <obj class name>.id
#             Aguments:
#                 obj : An instance object.
#         '''
#         key = str(obj.__class__.__name__) + "." + str(obj.id)
#         value_dict = obj
#         FileStorage.__objects[key] = value_dict

#     def save(self):
#         '''
#             Serializes __objects attribute to JSON file.
#         '''
#         objects_dict = {}
#         for key, val in FileStorage.__objects.items():
#             objects_dict[key] = val.to_dict()

#         with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
#             json.dump(objects_dict, fd)

#     def reload(self):
#         '''
#             Deserializes the JSON file to __objects.
#         '''
#         try:
#             with open(FileStorage.__file_path, encoding="UTF8") as fd:
#                 FileStorage.__objects = json.load(fd)
#             for key, val in FileStorage.__objects.items():
#                 class_name = val["__class__"]
#                 class_name = models.classes[class_name]
#                 FileStorage.__objects[key] = class_name(**val)
#         except FileNotFoundError:
#             pass

#     def delete(self, obj=None):
#         '''
#         Deletes an obj
#         '''
#         if obj is not None:
#             key = str(obj.__class__.__name__) + "." + str(obj.id)
#             FileStorage.__objects.pop(key, None)
#             self.save()

#     def close(self):
#         '''
#         Deserialize JSON file to objects
#         '''
#         self.reload()

#     def get(self, cls, id):
#         '''
#             Retrieve an obj w/class name and id
#         '''
#         result = None

#         try:
#             for v in self.__objects.values():
#                 if v.id == id:
#                     result = v
#         except BaseException:
#             pass

#         return result

#     def count(self, cls=None):
#         '''
#             Count num objects in FileStorage
#         '''
#         cls_counter = 0

#         if cls is not None:
#             for k in self.__objects.keys():
#                 if cls in k:
#                     cls_counter += 1
#         else:
#             cls_counter = len(self.__objects)
#         return cls_counter
