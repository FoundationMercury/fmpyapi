# fmapi
Foundation Mercury Python API Client

This is a Python package that wraps Foundation Mercury's API.  Foundation Mercury provides API access to curated demographic data sets such as census data and public county records.

The client requires an API key, which can be created after registering at https://www.foundationmercury.com .

The API key is simply a username and password that is used as basic authentication.  You can either pass the username and password into the constructor for the client, or put it in your \~/.netrc file (\~\\_netrc on Windows).  (Note that the username and password you use to log in to the web site won't work here.  It has to be an API key that you create after logging in)

Sample .netrc file:

    machine www.foundationmercury.com
    login myapiusername
    password myapipassword

Installation:

    pip3 install fmapi

Sample usage:

```python
import fmapi

client = fmapi.Client()

# Get States
states = client.get_states()
state = states[0]
print(state.__dict__)
# {'name': 'Alabama', 'state_abbrev': 'AL', 'state_code': '01'}

# Get Counties
counties = client.get_counties(state.state_code)
county = counties[0]
print(county.__dict__)
# {'name': 'Autauga County', 'county_code': '001', 'lat': Decimal('32.53638180'), 'lon': Decimal('-86.64449010')}

# Get Tracts
tracts = client.get_tracts("12", "001")
tract = tracts[0]
print(tract.__dict__)
# {'name': 'Census Tract 2', 'tract_code': '000200', 'lat': Decimal('29.65111740'), 'lon': Decimal('-82.33339080')}

# Get Blocks
blocks = client.get_blocks("12", "001", "000200")
block = blocks[0]
print(block.__dict__)
# {'name': 'Block 1000', 'block_code': '1000', 'lat': Decimal('29.65859590'), 'lon': Decimal('-82.32728900')}

# Tract Demographic Profile
dp = client.get_tract_profile("12", "001", "000200")
print(dp.__dict__)
# {'sex_age_total': 7431, 'sex_age_under_5': 119, 'sex_age_5_9': 64, 'sex_age_10_14': 75, 'sex_age_15_19': 1255, 'sex_age_20_24':4244, 'sex_age_25_29': 598, 'sex_age_30_34': 254, 'sex_age_35_39': 139, 'sex_age_40_44': 116, 'sex_age_45_49': 116, 'sex_age_50_54': 102, 'sex_age_55_59': 105, 'sex_age_60_64': 81, 'sex_age_65_69': 53, 'sex_age_70_74': 26, 'sex_age_75_79': 38, 'sex_age_80_84': 25, 'sex_age_85_plus': 21, 'sex_age_total_m': 3233, 'sex_age_under_5_m': 72, 'sex_age_5_9_m': 32, 'sex_age_10_14_m': 30, 'sex_age_15_19_m': 391, 'sex_age_20_24_m': 1723, 'sex_age_25_29_m': 396, 'sex_age_30_34_m': 171, 'sex_age_35_39_m': 77, 'sex_age_40_44_m': 68, 'sex_age_45_49_m': 65, 'sex_age_50_54_m': 45, 'sex_age_55_59_m': 54, 'sex_age_60_64_m': 44, 'sex_age_65_69_m': 28,'sex_age_70_74_m': 11, 'sex_age_75_79_m': 12, 'sex_age_80_84_m': 11, 'sex_age_85_plus_m': 3, 'sex_age_total_f': 4198, 'sex_age_under_5_f': 47, 'sex_age_5_9_f': 32, 'sex_age_10_14_f': 45, 'sex_age_15_19_f': 864, 'sex_age_20_24_f': 2521, 'sex_age_25_29_f': 202, 'sex_age_30_34_f': 83, 'sex_age_35_39_f': 62, 'sex_age_40_44_f': 48, 'sex_age_45_49_f': 51, 'sex_age_50_54_f': 57, 'sex_age_55_59_f': 51, 'sex_age_60_64_f': 37, 'sex_age_65_69_f': 25, 'sex_age_70_74_f': 15, 'sex_age_75_79_f': 26, 'sex_age_80_84_f': 14, 'sex_age_85_plus_f': 18, 'median_age_both': 22, 'median_age_m': 22, 'median_age_f': 21, 'sex_16_over_both': 7157, 'sex_16_over_m': 3089, 'sex_16_over_f': 4068, 'sex_18_over_both': 7103, 'sex_18_over_m': 3071, 'sex_18_over_f': 4032, 'sex_21_over_both': 4593, 'sex_21_over_m': 2256, 'sex_21_over_f': 2337, 'sex_62_over_both': 212, 'sex_62_over_m': 88, 'sex_62_over_f': 124, 'sex_65_over_both': 163, 'sex_65_over_m': 65, 'sex_65_over_f': 98, 'race_total': 7431, 'race_one': 7245, 'race_white': 5575, 'race_black':1155, 'race_native': 20, 'race_asian': 340, 'race_asian_indian': 88, 'race_chinese': 92, 'race_filipino': 50, 'race_japanese': 5, 'race_korean': 28, 'race_vietnamese': 29, 'race_other_asian': 48, 'race_pacific': 7, 'race_native_hawaiian': 1, 'race_guam': 5, 'race_samoam': 1, 'race_other_pacific': 0, 'race_other': 148, 'race_two': 186, 'race_white_native': 15, 'race_white_asian': 72, 'race_white_black': 32, 'race_white_other': 20, 'race_white_alone': 5731, 'race_black_alone': 1218, 'race_native_alone': 51, 'race_asian_alone': 445, 'race_hawaiian_alone': 15, 'race_other_alone': 178, 'hisp_not_total': 7431, 'hisp': 838, 'mexican': 78,'puerto_rican': 120, 'cuban': 257, 'other_hisp': 383, 'not_hisp': 6593, 'hisp_race_total': 7431, 'hisp_race_h': 838, 'hisp_race_h_white': 640, 'hisp_race_h_black': 18, 'hisp_race_h_native': 4, 'hisp_race_h_asian': 7, 'hisp_race_h_hawaiian': 0, 'hisp_race_h_other': 126, 'hisp_race_h_two': 43, 'hisp_race_noth': 6593, 'hisp_race_noth_white': 4935, 'hisp_race_noth_black': 1137, 'hisp_race_noth_native': 16, 'hisp_race_noth_asian': 333, 'hisp_race_noth_hawaiian': 7, 'hisp_race_noth_other': 22, 'hisp_race_noth_two': 143, 'rel_total': 7431, 'rel_house': 6359, 'rel_house_holder': 2788, 'rel_house_spouse': 152, 'rel_house_child': 339, 'rel_house_child_18': 195, 'rel_house_other': 265, 'rel_house_other_18': 78, 'rel_house_other_65': 8, 'rel_house_nonrel': 2815, 'rel_house_nonrel_18': 16, 'rel_house_nonrel_65': 6, 'rel_house_nonrel_unmp': 141, 'rel_group': 1072, 'rel_group_inst': 11, 'rel_group_inst_m': 4, 'rel_group_inst_f': 7, 'rel_group_noninst': 1061, 'rel_group_noninst_m': 191, 'rel_group_noninst_f': 870, 'house_total': 2788, 'house_family': 432, 'house_family_18': 121, 'house_family_hw': 152, 'house_family_hw_18': 51, 'house_family_m': 81,'house_family_m_18': 18, 'house_family_f': 199, 'house_family_f_18': 52, 'house_nonfam': 2356, 'house_nonfam_alone': 965, 'house_nonfam_m': 552, 'house_nonfam_m_65': 27, 'house_nonfam_f': 413, 'house_nonfam_f_65': 33, 'house_18': 176, 'house_65': 139, 'avg_house_size': '2.2800', 'avg_fam_size': '2.7500', 'occu_total': 3123, 'occu_occu': 2788, 'occu_vacant': 335, 'occu_vacant_for_rent': 208, 'occu_vacant_rented': 11, 'occu_vacant_sale_only': 14, 'occu_vacant_sold': 0, 'occu_vacant_seasonal': 15, 'occu_vacant_other': 87, 'homeowner_vacany_rate': '3.6000', 'rental_vacancy_rate': '7.9000', 'tenure_total': 2788, 'tenure_owner': 373, 'tenure_renter': 2415, 'pop_tenure_owner': 883, 'pop_tenure_renter': 5476, 'avg_house_size_owner': '2.3700', 'avg_house_size_renter': '2.2700'}


```


