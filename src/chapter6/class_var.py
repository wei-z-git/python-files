# class Address:
#     detail = '广州'
#     post_code = '50000'
#     def info(self):
#         # print(detail)
#         print(Address.detail)
#         print(Address.post_code)


# print(Address.detail)
# addr = Address()
# addr.info()
# class Record:
#     item = "鼠标"
#     data = "2016-06-16"
#     def info(self):
#         print("info方法中：", self.item)
#         print("info方法中：", self.data)
#         print(self)


# rc=Record()
# print(rc.item)
# print(rc.data)
# rc.info()

class Inventory:
    item = '鼠标'
    quantity = 2000
    def change(self,item, quantity):
        self.item = item
        self.quantity = quantity
    

iv = Inventory()
iv.change('haha',1000)
print(iv.item)
print(iv.quantity)

print(Inventory.item)
print(Inventory.quantity)