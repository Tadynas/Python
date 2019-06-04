class NewClass:
    name_attribute = "Ted"

    def name_method(self):
        return self.name_attribute

new_instance = NewClass()
print(new_instance.name_method())
#Ted