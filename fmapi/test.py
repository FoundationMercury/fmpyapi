"API Client Tests"

import unittest 
import fmapi

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_gets(self):
        "Test everything"
        client = fmapi.Client(url_base="http://127.0.0.1:5000/api")

        # States
        states = client.get_states()
        assert states
        state = states[0]
        print(state.__dict__)

        # Counties
        counties = client.get_counties(state.state_code)
        assert counties
        county = counties[0]
        print(county.__dict__)

        # Tracts
        tracts = client.get_tracts("12", "001")
        assert tracts
        tract = tracts[0]
        print(tract.__dict__)

        # Blocks
        blocks = client.get_blocks("12", "001", "000200")
        assert blocks
        block = blocks[0]
        print(block.__dict__)

        # Tract Demographic Profile
        dp = client.get_tract_profile("12", "001", "000200")
        assert dp
        print(dp.__dict__)
        


if __name__ == '__main__':
    unittest.main()
    
