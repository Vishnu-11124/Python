class College:
    college_name = "ABC College"  # Class variable

    @classmethod
    def get_college_name(cls, name):
        cls.college_name = name
        return cls.college_name  # Accessing class variable using cls

tarun = College()
print(tarun.get_college_name("XYZ College"))  # Output: ABC College
