from random import randint
import uuid

class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]
    def _generateId(self):
        return str(uuid.uuid4())

    def add_member(self, member):
        member['id'] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        self._members = [m for m in self._members if m['id'] != id]

    def update_member(self, id, member):
        for i, m in enumerate(self._members):
            if m['id'] == id:
                self._members[i].update(member)
                return self._members[i]
        return None
    
    def get_member(self, id):
        for m in self._members:
            if m['id'] == id:
                return m
        return None

    def get_all_members(self):
        return self._members