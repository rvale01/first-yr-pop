# Example of aggregation

class Address:
    def __init__(self, postcode):
        self.postcode = postcode


class Student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def info(self):
        print("%s lives at %s" %
              (self.name, self.address.postcode))

ad = Address("BS16 3FT")

st = Student("Nick", ad)

st.info()