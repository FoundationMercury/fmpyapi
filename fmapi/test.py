"API Client Tests"

import unittest 
import fmapi

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_gets(self):
        "Test everything"
        client = fmapi.Client(url_base="http://127.0.0.1:5000/api")
        states = client.get_states()
        assert states
        for state in states:
            print(state.__dict__)
            counties = client.get_counties(state.state_code)
            assert counties
            print(counties[0].__dict__)


if __name__ == '__main__':
    unittest.main()
    
