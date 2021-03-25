# reference : https://medium.com/free-code-camp/learning-python-from-zero-to-hero-120ea540b567
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    # private function "_" prefix
    def _get_age(self):
        return self._age


tk = Person('TK', 25)
print(tk.show_age())  # => 25
try:
    # can call private functions directly. but private functions doesn't expose directly like class reference
    print(tk._get_age())
except Exception as e:
    print(e)
