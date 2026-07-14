
class College:
    college_name = "ABC College"  # Class variable

    @staticmethod
    def get_college_name():
        return College.college_name  # Accessing class variable using class name

tarun = College()
print(tarun.get_college_name())  # Output: ABC College    