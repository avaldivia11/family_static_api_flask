
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
import json

class FamilyStructure:
    def __init__(self,last_name):
        self.last_name = last_name
        


        # example list of members
        self._members = [
            {
            "id":3443,
            "first_name": "Tommy",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers": [7, 13, 22]
            },
            {
            "id":self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]
            },
            {
            "id":self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        member["id"]=self._generateId()
        member["last_name"]=self.last_name
        return self._members.append(member)
        

    def delete_member(self, id):
        # fill this method and update the return
        new_family= list(filter(lambda member:member["id"]!= id, self._members))
        self._members = new_family
        return self._members
        

    def get_member(self, id):
        member = list(filter(lambda one : one["id"] == id, self._members))
        return member[0]
        # fill this method and update the return
        

    def update_member(self, id,member):
        member = self.delete_member(id)
        members["id"] = id 
        members.append(member)
        return members 
        # fill this method and update the return
    

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
