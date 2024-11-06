from phone import Phone
from laptop import Laptop

class Store:
    def __init__(self,name):
        self.name=name
        self.objects={'phone':{},'laptop':{}}
    def add_data(self,obj):
        type_obj='phone' if isinstance(obj,Phone) else 'laptop'
        self.objects[type_obj][obj.id]=obj
        print(f'added:{obj.name}')
    @staticmethod
    def show_info(data,type_obj):
        print("\n"+"_"*18+type_obj.capitalize() + "_"*18)
        for item in data.values():
            print(item)
        if not data:
            print('empty')
    def display(self,type_obj=None):
        if type_obj:
            type_obj += type_obj.lower()
            try:
                data=self.objects[type_obj]
                self.show_info(data,type_obj)
            except KeyError:
                print('not found')
        else:
            for k,data in self.objects.items():
                self.show_info(data,k)
    def remove(self,obj_id):
        for group in self.objects.values():
            if obj_id in group:
                del group[obj_id]
                return f'{obj_id}'
        return 'not found'
    def search(self,**criteria):
        result=[]
        for group in self.objects.values():
            for obj in group.values():
                if all(getattr(obj,attr,None) == value for attr, value in criteria.items()):
                   result.append(obj)
        return result