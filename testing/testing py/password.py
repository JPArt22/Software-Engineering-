import unittest

def isValidPassword(password:str):
    if len(password) < 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if any(c.isspace() for c in password):
        return False
    return True

print(isValidPassword("Password123")) 

class TestPassword(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(isValidPassword("Valid123"))
    
    def test_short_password(self):
        self.assertFalse(isValidPassword("Short1"))
    
    def test_no_uppercase(self):
        self.assertFalse(isValidPassword("lowercase1"))
    
    def test_no_lowercase(self):
        self.assertFalse(isValidPassword("UPPERCASE1"))
    
    def test_no_digit(self):
        self.assertFalse(isValidPassword("NoDigitHere!"))
    
    def test_with_space(self):
        self.assertFalse(isValidPassword("Invalid Password1"))  
    

unittest.main()