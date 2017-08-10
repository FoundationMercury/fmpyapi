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

# Basic Demographics by County
bd = client.get_basic_county("12", "097")
print(bd.__dict__)
# {'state_abbrev': 'FL', 'state_code': '12', 'state_name': 'Florida', 'county_code': '097', 'county_name': 'Osceola County', 'tract_code': '', 'block_code': '', 'zcta5': '', 'geo_name': 'Osceola County', 'square_miles': '1327.4527', 'housing_units': 128170,'total_population': 268685, 'population_density': '202.4065', 'white': 190641, 'white_pct': '70.95', 'black': 30369, 'black_pct': '11.30', 'native': 1452, 'native_pct': '0.54', 'asian': 7406, 'asian_pct': '2.76', 'hawaiian': 294, 'hawaiian_pct': '0.11', 'other': 27623, 'other_pct': '10.28', 'two_or_more': 10900, 'two_or_more_pct': '4.06', 'not_hisplatino': 146539, 'not_hisplatino_pct': '54.54', 'hisplatino': 122146, 'hisplatino_pct': '45.46', 'males': 131634, 'males_pct': '48.99', 'females': 137051, 'females_pct': '51.01', 'age_median': 36, 'age_median_male': 34, 'age_median_female': 37, 'house_1male': 7601, 'house_1male_pct': '8.39', 'house_1female': 8661, 'house_1female_pct': '9.56', 'house_family': 68547, 'house_family_pct': '75.66', 'house_husbwife': 47563, 'house_husbwife_pct': '52.50', 'households': 90603}

# Zip Code Tabulation Areas
zctas = client.get_zctas("12")
z = zctas[0]
print(z.__dict__)
# {'zcta': '32003', 'lat': '30.09607230', 'lon': '-81.71333030'}

# Basic Demographics by Tract
bd = client.get_basic_tract("12", "001", "000301")
print(bd.__dict__)
# {'state_abbrev': 'FL', 'state_code': '12', 'state_name': 'Florida', 'county_code': '001', 'county_name': 'Alachua County', 'tract_code': '000301', 'block_code': '', 'zcta5': '', 'geo_name': 'Census Tract 3.01', 'square_miles': '0.9541', 'housing_units': 1933, 'total_population': 3308, 'population_density': '3467.1833', 'white': 2301, 'white_pct': '69.56', 'black': 751, 'black_pct': '22.70', 'native': 20, 'native_pct': '0.60', 'asian': 70, 'asian_pct': '2.12', 'hawaiian': 0, 'hawaiian_pct': '0.00', 'other':61, 'other_pct': '1.84', 'two_or_more': 105, 'two_or_more_pct': '3.17', 'not_hisplatino': 2976, 'not_hisplatino_pct': '89.96', 'hisplatino': 332, 'hisplatino_pct': '10.04', 'males': 1671, 'males_pct': '50.51', 'females': 1637, 'females_pct': '49.49', 'age_median': 27, 'age_median_male': 27, 'age_median_female': 27, 'house_1male': 436, 'house_1male_pct': '24.80', 'house_1female': 391, 'house_1female_pct': '22.24', 'house_family': 493, 'house_family_pct': '28.04', 'house_husbwife': 212, 'house_husbwife_pct':'12.06', 'households': 1758}

# Basic Demographics by Block
bd = client.get_basic_block("12", "001", "000200", "1001")
print(bd.__dict__)
# {'state_abbrev': 'FL', 'state_code': '12', 'state_name': 'Florida', 'county_code': '001', 'county_name': 'Alachua County', 'tract_code': '000200', 'block_code': '1001', 'zcta5': '32601', 'geo_name': 'Block 1001', 'square_miles': '0.0054', 'housing_units':13, 'total_population': 23, 'population_density': '4225.4028', 'white': 5, 'white_pct': '21.74', 'black': 18, 'black_pct': '78.26', 'native': 0, 'native_pct': '0.00', 'asian': 0, 'asian_pct': '0.00', 'hawaiian': 0, 'hawaiian_pct': '0.00', 'other': 0, 'other_pct': '0.00', 'two_or_more': 0, 'two_or_more_pct': '0.00', 'not_hisplatino': 23, 'not_hisplatino_pct': '100.00', 'hisplatino': 0, 'hisplatino_pct': '0.00', 'males': 9, 'males_pct': '39.13', 'females': 14, 'females_pct': '60.87', 'age_median': 47, 'age_median_male': 57, 'age_median_female': 31, 'house_1male': 1, 'house_1male_pct': '10.00', 'house_1female': 3, 'house_1female_pct':'30.00', 'house_family': 5, 'house_family_pct': '50.00', 'house_husbwife': 1, 'house_husbwife_pct': '10.00', 'households': 10}

# Cities
cities = client.get_cities("FL")
print(cities[0].__dict__)
# {'name': 'Acacia Villas', 'lat': Decimal('26.64582820'), 'lon': Decimal('-80.11047080')}

# Geocode
latlon = client.geocode("1415 W Oak St, Kissimmee, FL 34741")
print(latlon.__dict__)
# {'lat': Decimal('28.30139130'), 'lon': Decimal('-81.41856570'), 'descr': 'Exact', 'block_code': '1001', 'tract_code': '041800','county_code': '097', 'county_name': 'Osceola County', 'state_code': '12', 'state_abbrev': 'FL', 'state_name': 'Florida'}

# Reverse Geocode 
addr = client.revgeocode("28.30139130", "-81.41856570")
print(addr.__dict__)
# {'address': '1415 W OAK ST, KISSIMMEE FL, 34741', 'distance': Decimal('0.0000')}

# SF1 Docs
docs = client.get_sf1_docs("03")
print(docs[0].__dict__)
# {'col_name': 'fileid', 'col_title': 'fileid', 'col_descr': 'File Identification'}

# SF1 File 01 (Total Population)
sf = client.get_sf101("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '01', 'logrecno': 26, 'total_population': 23}

# SF1 File 03
sf = client.get_sf103("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '03', 'logrecno': 26, 'racepop_total': 23, 'racepop_white_alone': 5, 'racepop_black_alone': 18, 'racepop_native_alone': 0, 'racepop_asian_alone': 0, 'racepop_hawaiian_alone': 0, 'racepop_other_alone': 0, 'racepop_two_or_more': 0, 'hspor_total': 23, 'hspor_not': 23, 'hspor_latino': 0, 'hspra_total': 23, 'hspra_not': 23, 'hspra_not_white': 5, 'hspra_not_black': 18, 'hspra_not_native': 0, 'hspra_not_asian': 0, 'hspra_not_hawaiian': 0, 'hspra_not_other': 0, 'hspra_not_two': 0, 'hspra_hsp': 0, 'hspra_white': 0, 'hspra_black': 0, 'hspra_native': 0, 'hspra_asian': 0, 'hspra_hawaiian': 0, 'hspra_other': 0, 'hspra_two': 0, 'racepop_tally_total': 23, 'racepop_tally_white': 5, 'racepop_tally_black': 18, 'racepop_tally_native': 0, 'racepop_tally_asian': 0, 'racepop_tally_hawaiian': 0, 'racepop_tally_other': 0, 'hsp_tally_total': 23, 'hsp_tally_not': 23, 'hsp_tally_notw': 5, 'hsp_tally_notb': 18, 'hsp_tally_notn': 0, 'hsp_tally_nota': 0, 'hsp_tally_noth': 0,'hsp_tally_noto': 0, 'hsp_tally': 0, 'hsp_tally_w': 0, 'hsp_tally_b': 0, 'hsp_tally_n': 0, 'hsp_tally_a': 0, 'hsp_tally_h': 0, 'hsp_tally_o': 0, 'racepop_totaln': 23, 'racepop_1': 23, 'racepop_1w': 5, 'racepop_1b': 18, 'racepop_1n': 0, 'racepop_1a': 0, 'racepop_1h': 0, 'racepop_1o': 0, 'racepop_2m': 0, 'racepop_2': 0, 'racepop_2wb': 0, 'racepop_2wn': 0, 'racepop_2wa': 0, 'racepop_2wh': 0, 'racepop_2wo': 0, 'racepop_2bn': 0, 'racepop_2ba': 0, 'racepop_2bh': 0, 'racepop_2bo': 0, 'racepop_2na': 0, 'racepop_2nh': 0, 'racepop_2no': 0, 'racepop_2ah': 0, 'racepop_2ao': 0, 'racepop_2ho': 0, 'racepop_3': 0, 'racepop_3wbn': 0, 'racepop_3wba': 0, 'racepop_3wbh': 0, 'racepop_3wbo': 0, 'racepop_3wna': 0, 'racepop_3wnh': 0, 'racepop_3wno': 0, 'racepop_3wah': 0, 'racepop_3wao': 0, 'racepop_3who': 0, 'racepop_3bna': 0, 'racepop_3bnh': 0, 'racepop_3bno': 0, 'racepop_3bah': 0, 'racepop_3bao': 0, 'racepop_3bho': 0, 'racepop_3nah': 0, 'racepop_3nao': 0, 'racepop_3nho': 0, 'racepop_3aho': 0, 'racepop_4': 0, 'racepop_4wbna': 0, 'racepop_4wbnh': 0, 'racepop_4wbno': 0, 'racepop_4wbah': 0, 'racepop_4wbao': 0, 'racepop_4wbho': 0, 'racepop_4wnah': 0, 'racepop_4wnao': 0, 'racepop_4wnho': 0, 'racepop_4waho': 0, 'racepop_4bnah': 0, 'racepop_4bnao': 0, 'racepop_4bnho': 0, 'racepop_4baho': 0, 'racepop_4naho': 0, 'racepop_5': 0, 'racepop_5wbnah': 0, 'racepop_5wbnao': 0, 'racepop_5wbnho': 0, 'racepop_5wbaho': 0, 'racepop_5wnaho': 0, 'racepop_5bnaho': 0, 'racepop_6': 0, 'racepop_6wbnaho': 0, 'hspnot_total': 23, 'hspnot_h_total': 0, 'hspnot_n': 23, 'hspnot_n1': 23, 'hspnot_n1w': 5, 'hspnot_n1b': 18, 'hspnot_n1n': 0, 'hspnot_n1a': 0, 'hspnot_n1h': 0, 'hspnot_n1o': 0, 'hspnot_n2m': 0, 'hspnot_n2': 0, 'hspnot_n2wb': 0, 'hspnot_n2wn': 0, 'hspnot_n2wa': 0, 'hspnot_n2wh': 0, 'hspnot_n2wo': 0, 'hspnot_n2bn': 0, 'hspnot_n2ba': 0, 'hspnot_n2bh': 0, 'hspnot_n2bo': 0, 'hspnot_n2na': 0, 'hspnot_n2nh': 0, 'hspnot_n2no': 0, 'hspnot_n2ah': 0, 'hspnot_n2ao': 0, 'hspnot_n2ho': 0, 'hspnot_n3': 0, 'hspnot_n3wbn': 0, 'hspnot_n3wba': 0, 'hspnot_n3wbh': 0, 'hspnot_n3wbo': 0, 'hspnot_n3wna': 0, 'hspnot_n3wnh': 0, 'hspnot_n3wno': 0, 'hspnot_n3wah': 0, 'hspnot_n3wao': 0, 'hspnot_n3who': 0, 'hspnot_n3bna': 0, 'hspnot_n3bnh': 0, 'hspnot_n3bno': 0, 'hspnot_n3bah': 0, 'hspnot_n3bao': 0, 'hspnot_n3bho': 0, 'hspnot_n3nah': 0, 'hspnot_n3nao': 0, 'hspnot_n3nho': 0, 'hspnot_n3aho': 0, 'hspnot_n4': 0, 'hspnot_n4wbna': 0, 'hspnot_n4wbnh': 0, 'hspnot_n4wbno': 0, 'hspnot_n4wbah': 0, 'hspnot_n4wbao': 0, 'hspnot_n4wbho': 0, 'hspnot_n4wnah': 0, 'hspnot_n4wnao': 0, 'hspnot_n4wnho': 0, 'hspnot_n4waho': 0, 'hspnot_n4bnah': 0, 'hspnot_n4bnao': 0, 'hspnot_n4bnho': 0, 'hspnot_n4baho': 0, 'hspnot_n4naho': 0, 'hspnot_n5': 0, 'hspnot_n5wbnah': 0, 'hspnot_n5wbnao': 0, 'hspnot_n5wbnho': 0, 'hspnot_n5wbaho': 0, 'hspnot_n5wnaho': 0, 'hspnot_n5bnaho': 0,'hspnot_n6': 0, 'hspnot_n6wbnaho': 0}

# SF1 File 04
sf = client.get_sf104("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '04', 'logrecno': 26, 'racepop_total_18p': 21, 'racepop_1_18p': 21, 'racepop_white_alone_18p': 5, 'racepop_black_alone_18p': 16, 'racepop_native_alone_18p': 0, 'racepop_asian_alone_18p': 0, 'racepop_hawaiian_alone_18p': 0, 'racepop_other_alone_18p': 0, 'racepop_2m_18p': 0, 'racepop_2_18p': 0, 'racepop_2wb_18p': 0, 'racepop_2wn_18p': 0, 'racepop_2wa_18p': 0, 'racepop_2wh_18p': 0, 'racepop_2wo_18p': 0, 'racepop_2bn_18p': 0, 'racepop_2ba_18p': 0, 'racepop_2bh_18p': 0, 'racepop_2bo_18p': 0, 'racepop_2na_18p': 0, 'racepop_2nh_18p': 0, 'racepop_2no_18p': 0, 'racepop_2ah_18p': 0, 'racepop_2ao_18p': 0, 'racepop_2ho_18p': 0, 'racepop_3_18p': 0, 'racepop_3wbn_18p': 0, 'racepop_3wba_18p': 0, 'racepop_3wbh_18p': 0, 'racepop_3wbo_18p': 0, 'racepop_3wna_18p': 0, 'racepop_3wnh_18p': 0, 'racepop_3wno_18p': 0, 'racepop_3wah_18p': 0, 'racepop_3wao_18p': 0, 'racepop_3who_18p': 0, 'racepop_3bna_18p': 0, 'racepop_3bnh_18p': 0, 'racepop_3bno_18p': 0, 'racepop_3bah_18p': 0, 'racepop_3bao_18p': 0, 'racepop_3bho_18p': 0, 'racepop_3nah_18p': 0, 'racepop_3nao_18p': 0, 'racepop_3nho_18p': 0, 'racepop_3aho_18p': 0, 'racepop_4_18p': 0, 'racepop_4wbna_18p': 0, 'racepop_4wbnh_18p': 0, 'racepop_4wbno_18p': 0, 'racepop_4wbah_18p': 0, 'racepop_4wbao_18p': 0, 'racepop_4wbho_18p': 0, 'racepop_4wnah_18p': 0, 'racepop_4wnao_18p': 0, 'racepop_4wnho_18p': 0, 'racepop_4waho_18p': 0, 'racepop_4bnah_18p': 0, 'racepop_4bnao_18p': 0, 'racepop_4bnho_18p': 0, 'racepop_4baho_18p': 0, 'racepop_4naho_18p': 0, 'racepop_5_18p': 0, 'racepop_5wbnah_18p': 0, 'racepop_5wbnao_18p': 0, 'racepop_5wbnho_18p': 0, 'racepop_5wbaho_18p': 0, 'racepop_5wnaho_18p': 0, 'racepop_5bnaho_18p': 0, 'racepop_6_18p': 0, 'racepop_6wbnaho_18p': 0, 'hspnot_total_18p': 21, 'hspnot_h_total_18p': 0, 'hspnot_n_18p': 21, 'hspnot_n1_18p': 21, 'hspnot_n1w_18p': 5, 'hspnot_n1b_18p': 16, 'hspnot_n1n_18p': 0, 'hspnot_n1a_18p': 0, 'hspnot_n1h_18p': 0, 'hspnot_n1o_18p': 0, 'hspnot_n2m_18p': 0, 'hspnot_n2_18p': 0, 'hspnot_n2wb_18p': 0, 'hspnot_n2wn_18p': 0, 'hspnot_n2wa_18p': 0, 'hspnot_n2wh_18p': 0, 'hspnot_n2wo_18p': 0, 'hspnot_n2bn_18p': 0, 'hspnot_n2ba_18p': 0, 'hspnot_n2bh_18p': 0, 'hspnot_n2bo_18p': 0, 'hspnot_n2na_18p': 0, 'hspnot_n2nh_18p': 0, 'hspnot_n2no_18p': 0, 'hspnot_n2ah_18p': 0, 'hspnot_n2ao_18p': 0, 'hspnot_n2ho_18p': 0, 'hspnot_n3_18p': 0, 'hspnot_n3wbn_18p': 0, 'hspnot_n3wba_18p': 0, 'hspnot_n3wbh_18p': 0, 'hspnot_n3wbo_18p': 0, 'hspnot_n3wna_18p': 0, 'hspnot_n3wnh_18p': 0, 'hspnot_n3wno_18p': 0, 'hspnot_n3wah_18p': 0, 'hspnot_n3wao_18p': 0, 'hspnot_n3who_18p': 0, 'hspnot_n3bna_18p': 0, 'hspnot_n3bnh_18p': 0, 'hspnot_n3bno_18p': 0, 'hspnot_n3bah_18p': 0, 'hspnot_n3bao_18p': 0, 'hspnot_n3bho_18p': 0, 'hspnot_n3nah_18p': 0, 'hspnot_n3nao_18p': 0, 'hspnot_n3nho_18p': 0, 'hspnot_n3aho_18p': 0, 'hspnot_n4_18p': 0, 'hspnot_n4wbna_18p': 0, 'hspnot_n4wbnh_18p': 0, 'hspnot_n4wbno_18p': 0, 'hspnot_n4wbah_18p': 0, 'hspnot_n4wbao_18p': 0, 'hspnot_n4wbho_18p': 0, 'hspnot_n4wnah_18p': 0, 'hspnot_n4wnao_18p': 0, 'hspnot_n4wnho_18p': 0, 'hspnot_n4waho_18p': 0, 'hspnot_n4bnah_18p': 0, 'hspnot_n4bnao_18p': 0, 'hspnot_n4bnho_18p': 0, 'hspnot_n4baho_18p': 0, 'hspnot_n4naho_18p': 0, 'hspnot_n5_18p': 0, 'hspnot_n5wbnah_18p': 0, 'hspnot_n5wbnao_18p': 0, 'hspnot_n5wbnho_18p': 0, 'hspnot_n5wbaho_18p': 0, 'hspnot_n5wnaho_18p': 0, 'hspnot_n5bnaho_18p': 0, 'hspnot_n6_18p': 0, 'hspnot_n6wbnaho_18p': 0, 'sex_age_total': 23, 'sex_age_m': 9, 'sex_age_m_u5': 0, 'sex_age_m_5_9': 0, 'sex_age_m_10_14': 0, 'sex_age_m_15_17': 0, 'sex_age_m_18_19': 0, 'sex_age_m_20': 0, 'sex_age_m_21': 1, 'sex_age_m_22_24': 0, 'sex_age_m_25_29': 0, 'sex_age_m_30_34': 1, 'sex_age_m_35_39': 0, 'sex_age_m_40_44': 0, 'sex_age_m_45_49': 0, 'sex_age_m_50_54': 1, 'sex_age_m_55_59': 3, 'sex_age_m_60_61': 0, 'sex_age_m_62_64': 1, 'sex_age_m_65_66': 1, 'sex_age_m_67_69': 0, 'sex_age_m_70_74': 0, 'sex_age_m_75_79': 1, 'sex_age_m_80_84': 0, 'sex_age_m_85o': 0, 'sex_age_f': 14, 'sex_age_f_u5': 0, 'sex_age_f_5_9': 1, 'sex_age_f_10_14': 0, 'sex_age_f_15_17': 1, 'sex_age_f_18_19': 0, 'sex_age_f_20': 3, 'sex_age_f_21': 0, 'sex_age_f_22_24': 1, 'sex_age_f_25_29': 1, 'sex_age_f_30_34': 1, 'sex_age_f_35_39': 1, 'sex_age_f_40_44': 0, 'sex_age_f_45_49': 1, 'sex_age_f_50_54': 0, 'sex_age_f_55_59': 2, 'sex_age_f_60_61': 0, 'sex_age_f_62_64': 0, 'sex_age_f_65_66': 1, 'sex_age_f_67_69': 0, 'sex_age_f_70_74': 0, 'sex_age_f_75_79': 1, 'sex_age_f_80_84': 0, 'sex_age_f_85o': 0, 'sex_age_median_both': 47, 'sex_age_median_m': 57, 'sex_age_median_f': 31, 'sex_age_total_u20': 2, 'sex_age_m_u20': 0, 'sex_age_m_u1': 0, 'sex_age_m_1': 0, 'sex_age_m_2': 0, 'sex_age_m_3': 0, 'sex_age_m_4': 0, 'sex_age_m_5': 0, 'sex_age_m_6': 0, 'sex_age_m_7': 0, 'sex_age_m_8': 0, 'sex_age_m_9': 0, 'sex_age_m_10': 0, 'sex_age_m_11': 0, 'sex_age_m_12': 0, 'sex_age_m_13': 0, 'sex_age_m_14': 0, 'sex_age_m_15': 0, 'sex_age_m_16': 0, 'sex_age_m_17': 0, 'sex_age_m_18': 0, 'sex_age_m_19': 0, 'sex_age_f_u20': 2, 'sex_age_f_u1': 0, 'sex_age_f_1': 0, 'sex_age_f_2': 0, 'sex_age_f_3': 0, 'sex_age_f_4': 0, 'sex_age_f_5': 1, 'sex_age_f_6': 0, 'sex_age_f_7': 0, 'sex_age_f_8': 0, 'sex_age_f_9': 0, 'sex_age_f_10': 0, 'sex_age_f_11': 0, 'sex_age_f_12': 0, 'sex_age_f_13': 0, 'sex_age_f_14': 0, 'sex_age_f_15': 0, 'sex_age_f_16': 1, 'sex_age_f_17': 0, 'sex_age_f_18': 0, 'sex_age_f_19': 0}

# SF1 File 05
sf = client.get_sf105("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '05', 'logrecno': 26, 'hsphse_total': 10, 'hsphse_not': 10, 'hsphse_notwhtal': 4, 'hspse_notblkal': 6, 'hsphse_notaianal': 0, 'hsphse_notasial': 0, 'hsphse_notnhopial': 0, 'hsphse_notothal': 0, 'hsphse_nottwoplus': 0, 'hsphse_is': 0, 'hsphse_whtal': 0, 'hsphse_blkal': 0, 'hsphse_aianal': 0, 'hsphse_asial': 0, 'hsphse_nhopial': 0, 'hsphse_othal': 0, 'hsphse_twoplus': 0, 'popage_total': 23, 'popage_und18': 2, 'popage_18plus': 21, 'avghse_total': '2.3000', 'avghse_und18': '0.2000', 'avghse_18plus': '2.1000', 'hsetyp_total': 10, 'hsetyp_fam': 5, 'hsetyp_hwf': 1, 'hsetyp_of': 4, 'hsetyp_mh': 1, 'hsetyp_fh': 3, 'hsetyp_nfh': 5, 'hsetyp_nfhal': 4, 'hsetyp_nfhnotal': 1, 'hseownchd_total': 10, 'hseownchd_1h': 4, 'hseownchd_1mh': 1, 'hseownchd_1fh': 3, 'hseownchd_2ph': 6, 'hseownchd_famh': 5, 'hseownchd_hwh': 1, 'hseownchd_hwchd': 1, 'hseownchd_hwnochd': 0, 'hseownchd_of': 4, 'hseownchd_ofm': 1, 'hseownchd_ofmchd': 0, 'hseownchd_ofmnochd': 1, 'hseownchd_off': 3, 'hseownchd_offchd': 0, 'hseownchd_offnochd': 3, 'hseownchd_nf': 1, 'hseownchd_nfmh': 0, 'hseownchd_nffh': 1, 'hse18_total': 10, 'hse18_with': 2, 'hse18_fam': 2, 'hse18_hwfam': 1, 'hse18_hwund6': 0, 'hse18_hwund6to17': 0, 'hse18_hw6to17': 1, 'hse18_ofam': 1, 'hse18_ofmh': 1, 'hse18_omhund6': 1, 'hse18_omhund6to17': 0, 'hse18_omh6to17': 0, 'hse18_offh': 0, 'hse18_ofwund6': 0, 'hse18_ofwund6to17': 0, 'hse18_ofw6to17': 0, 'hse18_nfam': 0, 'hse18_nm': 0, 'hse18_nmund6': 0, 'hse18_nmund6to17': 0, 'hse18_nm6to17': 0, 'hse18_nf': 0, 'hse18_nfund6': 0, 'hse18_nfund6to17': 0, 'hse18_nf6to17': 0, 'hse18_not': 8, 'hse18_notfam': 3, 'hse18_nothwf': 0, 'hse18_notof': 3, 'hse18_notmh': 0, 'hse18_notfh': 3, 'hse18_notn': 5, 'hse18_notnm': 1, 'hse18_notnf': 4, 'hsechd_total': 10, 'hsechd_15to64': 8, 'hsechd_15to64f': 4, 'hsechd_15to64hwf': 1, 'hsechd_15to64hwfchd': 1, 'hsechd_15to64hwfno': 0, 'hsechd_15to64of': 3, 'hsechd_15to64mh': 1, 'hsechd_15to64mhchd': 1, 'hsechd_15to64mhno': 0, 'hsechd_15to64fh': 2, 'hsechd_15to64fhchd': 0, 'hsechd_15to64fhno': 2, 'hsechd_15to64nf': 4, 'hsechd_15to64nfal': 3, 'hsechd_15to64nfnal': 1, 'hsechd_65pl': 2, 'hsechd_65plf': 1, 'hsechd_65plhwf': 0, 'hsechd_65plhwfchd': 0, 'hsechd_65plhwfno': 0, 'hsechd_65plof': 1, 'hsechd_65plmh': 0, 'hsechd_65plmhchd': 0, 'hsechd_65plmhno': 0, 'hsechd_65plfh': 1, 'hsechd_65plfhchd': 0, 'hsechd_65plfhno': 1, 'hsechd_65plnf': 1, 'hsechd_65plnfal': 1, 'hsechd_65plnfnal': 0, 'hsehld_total': 10, 'hsehld_fam': 5, 'hsehld_fam15to24': 0, 'hsehld_fam25to34': 0, 'hsehld_fam35to44': 1, 'hsehld_fam45to54': 1, 'hsehld_fam55to59': 2, 'hsehld_fam60to64': 0, 'hsehld_fam65to74': 1, 'hsehld_fam75to84': 0, 'hsehld_fam85': 0, 'hsehld_nonfam': 5, 'hsehld_nonfam15to24': 3, 'hsehld_nonfam25to34': 0, 'hsehld_nonfam35to44': 0, 'hsehld_nonfam45to54': 0, 'hsehld_nonfam55to59': 1, 'hsehld_nonfam60to64': 0, 'hsehld_nonfam65to74': 0, 'hsehld_nonfam75to84': 1, 'hsehld_nonfam85': 0, 'hse60_total': 10, 'hse60_w': 4, 'hse60_wf': 3, 'hse60_whw': 0, 'hse60_wof': 3, 'hse60_wofm': 1, 'hse60_woff': 2, 'hse60_wnf': 1, 'hse60_n': 6, 'hse60_nf': 2, 'hse60_nhw': 1, 'hse60_nof': 1, 'hse60_nofm': 0, 'hse60_noff': 1, 'hse60_nnf': 4, 'hse60sze_total': 10, 'hse60sze_w': 4, 'hse60sze_w1': 1, 'hse60sze_w2pls': 3, 'hse60sze_w2plsf': 3, 'hse60sze_w2plsnf': 0, 'hse60sze_n': 6, 'hse60sze_n1': 3, 'hse60sze_n2pls': 3, 'hse60sze_n2plsf': 2, 'hse60sze_n2plsnf': 1, 'hse65sze_total': 10, 'hse65sze_w': 4, 'hse65sze_w1': 1, 'hse65sze_w2pls': 3, 'hse65sze_w2plsf': 3, 'hse65sze_w2plsnf': 0, 'hse65sze_n': 6, 'hse65sze_n1': 3, 'hse65sze_n2pls': 3, 'hse65sze_n2plsf': 2, 'hse65sze_n2plsnf': 1, 'hse75sze_total': 10, 'hse75sze_w': 2, 'hse75sze_w1': 1, 'hse75sze_w2pls': 1, 'hse75sze_w2plsf': 1, 'hse75sze_w2plsnf': 0, 'hse75sze_n': 8, 'hse75sze_n1': 3, 'hse75sze_n2pls': 5, 'hse75sze_n2plsf': 4, 'hse75sze_n2plsnf': 1, 'nonrel_total': 10, 'nonrel_1m': 2, 'nonrel_no': 8, 'hsesze_total': 10, 'hsesze_f': 5, 'hsesze_f2': 1, 'hsesze_f3': 1, 'hsesze_f4': 3, 'hsesze_f5': 0, 'hsesze_f6': 0, 'hsesze_f7pl': 0, 'hsesze_n': 5, 'hsesze_n1': 4, 'hsesze_n2': 1, 'hsesze_n3': 0, 'hsesze_n4': 0, 'hsesze_n5': 0, 'hsesze_n6': 0, 'hsesze_n7pl': 0, 'hserel_total': 23, 'hserel_h': 23, 'hserel_f': 17, 'hserel_fh': 5, 'hserel_fmh': 2, 'hserel_ffh': 3, 'hserel_fs': 1, 'hserel_fbc': 5, 'hserel_fac': 0, 'hserel_fsc': 0, 'hserel_fgc': 0, 'hserel_fbs': 1, 'hserel_fp': 1, 'hserel_fpl': 0, 'hserel_fsdl': 0, 'hserel_for': 3, 'hserel_fnr': 1, 'hserel_n': 6, 'hserel_nmh': 1, 'hserel_nmhla': 1, 'hserel_nmhnla': 0, 'hserel_nfh': 4, 'hserel_nfhla': 3, 'hserel_nfhnla': 1, 'hserel_nnr': 1, 'hserel_igq': 0, 'hserel_ip': 0, 'hserel_np': 0, 'hsepop_total': 23, 'hsepop_f': 17, 'hsepop_fhw': 4, 'hsepop_fof': 13, 'hsepop_fmh': 4, 'hsepop_ffh': 9, 'hsepop_n': 6, 'hsepop_nm': 1, 'hsepop_nm1': 1, 'hsepop_nm2': 0, 'hsepop_nf': 5, 'hsepop_nf1': 3, 'hsepop_nf2': 2}

# SF1 File 06
sf = client.get_sf106("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '06', 'logrecno': 26, 'p31_total': 2, 'p31_in_households': 2, 'p31_householder_or_spouse': 0, 'p31_rel_child': 2, 'p31_own_child': 1, 'p31_hw_fam': 1, 'p31_other_fam': 0, 'p31_no_w_fam': 0, 'p31_no_h_fam': 0, 'p31_other_relatives': 1, 'p31_grandchildren': 0, 'p31_nongrandchildren': 1, 'p31_nonrelatives': 0, 'p31_in_group': 0, 'p31_inst': 0, 'p31_noninst': 0, 'p32_total': 2, 'p32_householder_or_spouse': 2, 'p32_in_households': 0, 'p32_rel_child': 2, 'p32_own_child': 1, 'p32_own_u3': 0, 'p32_own_3to4': 0, 'p32_own_5': 0, 'p32_own_6to11': 0, 'p32_own_12to13': 0, 'p32_own_14': 0, 'p32_own_15to17': 1, 'p32_other_relatives': 1, 'p32_other_u3': 0, 'p32_other_3to4': 0, 'p32_other_5': 1, 'p32_other_6to11': 0, 'p32_other_12to13': 0, 'p32_other_14': 0, 'p32_other_15to17': 0, 'p32_nonrelatives': 0, 'p32_non_u3': 0, 'p32_non_3to4': 0, 'p32_non_5': 0, 'p32_non_6to11': 0, 'p32_non_12to13': 0, 'p32_non_14': 0, 'p32_non_15to17': 0, 'p32_in_group': 0, 'p32_inst_population': 0, 'p32_inst_u3': 0, 'p32_inst_3to4': 0, 'p32_inst_5': 0, 'p32_inst_6to11': 0, 'p32_inst_12to13': 0, 'p32_inst_14': 0, 'p32_inst_15to17': 0, 'p32_noninst_population': 0, 'p32_noninst_u3': 0, 'p32_noninst_3to4': 0, 'p32_noninst_5': 0, 'p32_noninst_6to11': 0, 'p32_noninst_12to13': 0, 'p32_noninst_14': 0, 'p32_noninst_15to17': 0, 'p33_total': 2, 'p33_fam': 2, 'p33_hw_fam': 1, 'p33_other_fam': 1, 'p33_no_w_fam': 1, 'p33_no_h_fam': 0, 'p33_no_fam': 0, 'p34_total': 4, 'p34_households': 4, 'p34_fam_households': 3, 'p34_fam_holder': 1, 'p34_fam_m_holder': 0, 'p34_fam_f_holder': 1, 'p34_fam_spouse': 0, 'p34_fam_parent': 1, 'p34_fam_inlaw': 0, 'p34_fam_other': 1, 'p34_fam_nonrelatives': 0, 'p34_nonfamily_households': 1, 'p34_nonfamily_m_holder': 0, 'p34_nonfamily_m_alone': 0, 'p34_nonfamily_m_not_alone': 0, 'p34_nonfamily_f_holder': 1, 'p34_nonfamily_f_alone': 1, 'p34_nonfamily_f_not_alone': 0, 'p34_nonfamily_nonrelatives': 0, 'p34_in_group': 0, 'p34_inst': 0, 'p34_noninst': 0, 'p35_total': 5, 'p36_total': 16, 'p36_u18': 2, 'p36_18o': 14, 'p37_total': '3.2000', 'p37_u18': '0.4000', 'p38_no_w_fam': 3, 'p37_18o': '5.0000', 'p38_total': 1, 'p38_hw_fam': 1, 'p38_hw_fam_own_u18': 0, 'p38_hw_fam_own_u6': 0, 'p38_hw_fam_own_u6_and_6to17': 1, 'p38_hw_fam_own_6to17': 0, 'p38_hw_fam_own_none_u18': 4, 'p38_other_fam': 1, 'p38_no_w_fam_own_u18': 0, 'p38_no_w_fam_own_u6': 0, 'p38_no_w_fam_own_u6_and_6to17': 0, 'p38_no_w_fam_own_6to17': 0, 'p38_no_w_fam_own_none_u18': 1, 'p38_no_h_fam': 3, 'p38_no_h_fam_own_u18': 0, 'p38_no_h_fam_own_u6': 0, 'p38_no_h_fam_own_u6_and_6to17': 0, 'p38_no_h_fam_own_6to17': 0, 'p38_no_h_fam_own_none_u18': 3, 'p39_total': 5, 'p39_hw_fam': 1, 'p39_hw_fam_rel_u18': 1, 'p39_hw_fam_rel_u6': 0, 'p39_hw_fam_rel_u6_and_6to17': 0, 'p39_hw_fam_rel_6to17': 1, 'p39_hw_fam_rel_none_u18': 0, 'p39_other_fam': 4, 'p39_no_h_fam_rel_6to17': 1, 'p39_no_w_fam': 1, 'p39_no_h_fam_rel_none_u18': 0, 'p39_no_w_fam_rel_u18': 1, 'p39_no_w_fam_rel_u6': 0, 'p39_no_w_fam_rel_u6_and_6to17': 0, 'p39_no_w_fam_rel_6to17': 3, 'p39_no_w_fam_rel_none_u18': 0, 'p39_no_h_fam': 0, 'p39_no_h_fam_rel_u18': 0, 'p39_no_h_fam_rel_u6': 0, 'p39_no_h_fam_rel_u6_and_6to17': 3, 'p40_total': 1, 'p40_hw_fam': 1, 'p40_hw_fam_u3': 0, 'p40_hw_fam_3to4': 0, 'p40_hw_fam_5': 0, 'p40_hw_fam_6toll': 0, 'p40_hw_fam_12to17': 1, 'p40_other_fam': 0, 'p40_no_w_fam': 0, 'p40_no_w_fam_u3': 0, 'p40_no_w_fam_3to4': 0, 'p40_no_w_fam_5': 0, 'p40_no_w_fam_6to11': 0, 'p40_no_w_fam_12to17': 0, 'p40_no_h_fam': 0, 'p40_no_h_fam_under3': 0, 'p40_no_h_fam_3to4': 0, 'p40_no_h_fam_5': 0, 'p40_no_h_fam_6to11': 0, 'p40_no_h_fam_12to17': 0, 'p41_total': 0, 'p41_grandchildren_u3': 0, 'p41_grandchildren_3to4': 0, 'p41_grandchildren_5years': 0, 'p41_grandchildren_6to11': 0, 'p41_grandchildren_12to17': 0, 'p42_total': 0, 'p42_inst_population': 0, 'p42_adult_cor_fac': 0, 'p42_juvinile_fac': 0, 'p42_nursing_fac': 0, 'p42_other_inst_fac': 0, 'p42_noninst_population': 0, 'p42_student_housing': 0, 'p42_military_quarters': 0, 'p42_other_noninst_fac': 0, 'p43_total': 0, 'p43_m_group_quarters': 0, 'p43_m_u18_group_quarters': 0, 'p43_m_u18_inst_population': 0, 'p43_m_u18_adult_cor_fac': 0, 'p43_m_u18_juvinile_fac': 0, 'p43_m_u18_nursing_fac': 0, 'p43_m_u18_other_inst_fac': 0, 'p43_m_u18_noninst_population': 0, 'p43_m_u18_student_housing': 0, 'p43_m_u18_military_quarters': 0, 'p43_m_u18_other_noninst_fac': 0, 'p43_m_18to64_group_quarters': 0, 'p43_m_18to64_inst_population': 0, 'p43_m_18to64_adult_cor_fac': 0, 'p43_m_18to64_juvinile_fac': 0, 'p43_m_18to64_nursing_fac': 0, 'p43_m_18to64_other_inst_fac': 0, 'p43_m_18to64_noninst_population': 0, 'p43_m_18to64_student_housing': 0, 'p43_m_18to64_military_quarters': 0, 'p43_m_18to64_other_noninst_fac': 0, 'p43_m_65o_group_quarters': 0, 'p43_m_65over_in_inst_population': 0, 'p43_m_65o_adult_cor_fac': 0, 'p43_m_65o_juvinile_fac': 0, 'p43_m_65o_nursing_fac': 0, 'p43_m_65o_other_inst_fac': 0, 'p43_m_65o_noninst_population': 0, 'p43_m_65o_student_housing': 0, 'p43_m_65o_military_quarters': 0, 'p43_m_65o_other_noninst_fac': 0, 'p43_f_group_quarters': 0, 'p43_f_u18_group_quarters': 0, 'p43_f_u18_inst_population': 0, 'p43_f_u18_adult_cor_fac': 0, 'p43_f_u18_juvinile_fac': 0, 'p43_f_u18_nursing_fac': 0, 'p43_f_u18_other_inst_fac': 0, 'p43_f_u18_noninst_population': 0, 'p43_f_u18_student_housing': 0, 'p43_f_u18_military_quarters': 0, 'p43_f_u18_other_noninst_fac': 0, 'p43_f_18to64_group_quarters': 0, 'p43_f_18to64_inst_population': 0, 'p43_f_18to64_adult_cor_fac': 0, 'p43_f_18to64_juvinile_fac': 0, 'p43_f_18to64_nursing_fac': 0, 'p43_f_18to64_other_inst_fac': 0, 'p43_f_18to64_noninst_population': 0, 'p43_f_18to64_student_housing': 0, 'p43_f_18to64_military_quarters': 0, 'p43_f_18to64_other_noninst_fac': 0, 'p43_f_65o_group_quarters': 0, 'p43_f_65o_inst_population': 0, 'p43_f_65o_adult_cor_fac': 0, 'p43_f_65o_juvinile_fac': 0, 'p43_f_65o_nursing_fac': 0, 'p43_f_65o_other_inst_fac': 0, 'p43_f_65o_noninst_population': 0, 'p43_f_65o_student_housing': 0, 'p43_f_65o_military_quarters': 0, 'p43_f_65o_other_noninst_fac': 0, 'p44_total': 23, 'p44_none_allocated': 23, 'p44_allocated': 0, 'p45_total': 23, 'p45_none_allocated': 15, 'p45_allocated': 8, 'p46_total': 23, 'p46_none_allocated': 1, 'p46_allocated': 22, 'p47_total': 23, 'p47_none_allocated': 4, 'p47_allocated': 19, 'p48_total': 23, 'p48_none_allocated': 0, 'p48_allocated': 23, 'p49_total': 23, 'p49_none_allocated': 4, 'p49_allocated': 19}

# SF1 File 07
sf = client.get_sf107("12", "001", "000200", "1001")
print(sf.__dict__)
# {'fileid': 'SF1ST', 'stusab': 'FL', 'chariter': '000', 'cifsn': '07', 'logrecno': 26, 'relationship_total': 23, 'relationship_allocated': 1, 'relationship_not_allocated': 22, 'alloc_pop_group_qters_total': 0, 'alloc_pop_group_qters_not': 0, 'alloc_pop_group_qters_1m': 0, 'sex_age_white_total': 5, 'sex_age_white_m': 0, 'sex_age_white_m_u5': 0, 'sex_age_white_m_5_9': 0, 'sex_age_white_m_10_14': 0, 'sex_age_white_m_15_17': 0, 'sex_age_white_m_18_19': 0, 'sex_age_white_m_20': 0, 'sex_age_white_m_21': 0, 'sex_age_white_m_22_24': 0, 'sex_age_white_m_25_29': 0, 'sex_age_white_m_30_34': 0, 'sex_age_white_m_35_39': 0, 'sex_age_white_m_40_44': 0, 'sex_age_white_m_45_49': 0, 'sex_age_white_m_50_54': 0, 'sex_age_white_m_55_59': 0, 'sex_age_white_m_60_61': 0, 'sex_age_white_m_62_64': 0, 'sex_age_white_m_65_66': 0, 'sex_age_white_m_67_69': 0, 'sex_age_white_m_70_74': 0, 'sex_age_white_m_75_79': 0, 'sex_age_white_m_80_84': 0, 'sex_age_white_m_85p': 0, 'sex_age_white_f': 5, 'sex_age_white_f_u5': 0, 'sex_age_white_f_5_9': 0, 'sex_age_white_f_10_14': 0, 'sex_age_white_f_15_17': 0, 'sex_age_white_f_18_19': 0, 'sex_age_white_f_20': 3, 'sex_age_white_f_21': 0, 'sex_age_white_f_22_24': 1, 'sex_age_white_f_25_29': 0, 'sex_age_white_f_30_34': 0, 'sex_age_white_f_35_39': 1, 'sex_age_white_f_40_44': 0, 'sex_age_white_f_45_49': 0, 'sex_age_white_f_50_54': 0, 'sex_age_white_f_55_59': 0, 'sex_age_white_f_60_61': 0, 'sex_age_white_f_62_64': 0, 'sex_age_white_f_65_66': 0, 'sex_age_white_f_67_69': 0, 'sex_age_white_f_70_74': 0, 'sex_age_white_f_75_79': 0, 'sex_age_white_f_80_84': 0, 'sex_age_white_f_85p': 0, 'sex_age_black_total': 18, 'sex_age_black_m': 9, 'sex_age_black_m_u5': 0, 'sex_age_black_m_5_9': 0, 'sex_age_black_m_10_14': 0, 'sex_age_black_m_15_17': 0, 'sex_age_black_m_18_19': 0, 'sex_age_black_m_20': 0, 'sex_age_black_m_21': 1, 'sex_age_black_m_22_24': 0, 'sex_age_black_m_25_29': 0, 'sex_age_black_m_30_34': 1, 'sex_age_black_m_35_39': 0, 'sex_age_black_m_40_44': 0, 'sex_age_black_m_45_49': 0, 'sex_age_black_m_50_54': 1, 'sex_age_black_m_55_59': 3, 'sex_age_black_m_60_61': 0, 'sex_age_black_m_62_64': 1, 'sex_age_black_m_65_66': 1, 'sex_age_black_m_67_69': 0, 'sex_age_black_m_70_74': 0, 'sex_age_black_m_75_79': 1, 'sex_age_black_m_80_84': 0, 'sex_age_black_m_85p': 0, 'sex_age_black_f': 9, 'sex_age_black_f_u5': 0, 'sex_age_black_f_5_9': 1, 'sex_age_black_f_10_14': 0, 'sex_age_black_f_15_17': 1, 'sex_age_black_f_18_19': 0, 'sex_age_black_f_20': 0, 'sex_age_black_f_21': 0, 'sex_age_black_f_22_24': 0, 'sex_age_black_f_25_29': 1, 'sex_age_black_f_30_34': 1, 'sex_age_black_f_35_39': 0, 'sex_age_black_f_40_44': 0, 'sex_age_black_f_45_49': 1, 'sex_age_black_f_50_54': 0, 'sex_age_black_f_55_59': 2, 'sex_age_black_f_60_61': 0, 'sex_age_black_f_62_64': 0, 'sex_age_black_f_65_66': 1, 'sex_age_black_f_67_69': 0, 'sex_age_black_f_70_74': 0, 'sex_age_black_f_75_79': 1, 'sex_age_black_f_80_84': 0, 'sex_age_black_f_85p': 0, 'sex_age_natam_total': 0, 'sex_age_natam_m': 0, 'sex_age_natam_m_u5': 0, 'sex_age_natam_m_5_9': 0, 'sex_age_natam_m_10_14': 0, 'sex_age_natam_m_15_17': 0, 'sex_age_natam_m_18_19': 0, 'sex_age_natam_m_20': 0, 'sex_age_natam_m_21': 0, 'sex_age_natam_m_22_24': 0, 'sex_age_natam_m_25_29': 0, 'sex_age_natam_m_30_34': 0, 'sex_age_natam_m_35_39': 0, 'sex_age_natam_m_40_44': 0, 'sex_age_natam_m_45_49': 0, 'sex_age_natam_m_50_54': 0, 'sex_age_natam_m_55_59': 0, 'sex_age_natam_m_60_61': 0, 'sex_age_natam_m_62_64': 0, 'sex_age_natam_m_65_66': 0, 'sex_age_natam_m_67_69': 0, 'sex_age_natam_m_70_74': 0, 'sex_age_natam_m_75_79': 0, 'sex_age_natam_m_80_84': 0, 'sex_age_natam_m_85p': 0, 'sex_age_natam_f': 0, 'sex_age_natam_f_u5': 0, 'sex_age_natam_f_5_9': 0, 'sex_age_natam_f_10_14': 0, 'sex_age_natam_f_15_17': 0, 'sex_age_natam_f_18_19': 0, 'sex_age_natam_f_20': 0, 'sex_age_natam_f_21': 0, 'sex_age_natam_f_22_24': 0, 'sex_age_natam_f_25_29': 0, 'sex_age_natam_f_30_34': 0, 'sex_age_natam_f_35_39': 0, 'sex_age_natam_f_40_44': 0, 'sex_age_natam_f_45_49': 0, 'sex_age_natam_f_50_54': 0, 'sex_age_natam_f_55_59': 0, 'sex_age_natam_f_60_61': 0, 'sex_age_natam_f_62_64': 0, 'sex_age_natam_f_65_66': 0, 'sex_age_natam_f_67_69': 0, 'sex_age_natam_f_70_74': 0, 'sex_age_natam_f_75_79': 0, 'sex_age_natam_f_80_84': 0, 'sex_age_natam_f_85p': 0, 'sex_age_asian_total': 0, 'sex_age_asian_m': 0, 'sex_age_asian_m_u5': 0, 'sex_age_asian_m_5_9': 0, 'sex_age_asian_m_10_14': 0, 'sex_age_asian_m_15_17': 0, 'sex_age_asian_m_18_19': 0, 'sex_age_asian_m_20': 0, 'sex_age_asian_m_21': 0, 'sex_age_asian_m_22_24': 0, 'sex_age_asian_m_25_29': 0, 'sex_age_asian_m_30_34': 0, 'sex_age_asian_m_35_39': 0, 'sex_age_asian_m_40_44': 0, 'sex_age_asian_m_45_49': 0, 'sex_age_asian_m_50_54': 0, 'sex_age_asian_m_55_59': 0, 'sex_age_asian_m_60_61': 0, 'sex_age_asian_m_62_64': 0, 'sex_age_asian_m_65_66': 0, 'sex_age_asian_m_67_69': 0, 'sex_age_asian_m_70_74': 0, 'sex_age_asian_m_75_79': 0, 'sex_age_asian_m_80_84': 0, 'sex_age_asian_m_85p': 0, 'sex_age_asian_f': 0, 'sex_age_asian_f_u5': 0, 'sex_age_asian_f_5_9': 0, 'sex_age_asian_f_10_14': 0, 'sex_age_asian_f_15_17': 0, 'sex_age_asian_f_18_19': 0, 'sex_age_asian_f_20': 0, 'sex_age_asian_f_21': 0, 'sex_age_asian_f_22_24': 0, 'sex_age_asian_f_25_29': 0, 'sex_age_asian_f_30_34': 0, 'sex_age_asian_f_35_39': 0, 'sex_age_asian_f_40_44': 0, 'sex_age_asian_f_45_49': 0, 'sex_age_asian_f_50_54': 0, 'sex_age_asian_f_55_59': 0, 'sex_age_asian_f_60_61': 0, 'sex_age_asian_f_62_64': 0, 'sex_age_asian_f_65_66': 0, 'sex_age_asian_f_67_69': 0, 'sex_age_asian_f_70_74': 0, 'sex_age_asian_f_75_79': 0, 'sex_age_asian_f_80_84': 0, 'sex_age_asian_f_85p': 0, 'sex_age_isl_total': 0, 'sex_age_isl_m': 0, 'sex_age_isl_m_u5': 0, 'sex_age_hawaii_isl_m_5_9': 0, 'sex_age_hawaii_isl_m_10_14': 0, 'sex_age_hawaii_isl_m_15_17': 0, 'sex_age_hawaii_isl_m_18_19': 0, 'sex_age_hawaii_isl_m_20': 0, 'sex_age_hawaii_isl_m_21': 0, 'sex_age_hawaii_isl_m_22_24': 0, 'sex_age_hawaii_isl_m_25_29': 0, 'sex_age_hawaii_isl_m_30_34': 0, 'sex_age_hawaii_isl_m_35_39': 0, 'sex_age_hawaii_isl_m_40_44': 0, 'sex_age_hawaii_isl_m_45_49': 0, 'sex_age_hawaii_isl_m_50_54': 0, 'sex_age_hawaii_isl_m_55_59': 0, 'sex_age_hawaii_isl_m_60_61': 0, 'sex_age_hawaii_isl_m_62_64': 0, 'sex_age_hawaii_isl_m_65_66': 0, 'sex_age_hawaii_isl_m_67_69': 0, 'sex_age_hawaii_isl_m_70_74': 0, 'sex_age_hawaii_isl_m_75_79': 0, 'sex_age_hawaii_isl_m_80_84': 0, 'sex_age_hawaii_isl_m_85p': 0, 'sex_age_hawaii_isl_f': 0, 'sex_age_hawaii_isl_f_u5': 0, 'sex_age_hawaii_isl_f_5_9': 0, 'sex_age_hawaii_isl_f_10_14': 0, 'sex_age_hawaii_isl_f_15_17': 0, 'sex_age_hawaii_isl_f_18_19': 0, 'sex_age_hawaii_isl_f_20': 0, 'sex_age_hawaii_isl_f_21': 0, 'sex_age_hawaii_isl_f_22_24': 0, 'sex_age_hawaii_isl_f_25_29': 0, 'sex_age_hawaii_isl_f_30_34': 0, 'sex_age_hawaii_isl_f_35_39': 0, 'sex_age_hawaii_isl_f_40_44': 0, 'sex_age_hawaii_isl_f_45_49': 0, 'sex_age_hawaii_isl_f_50_54': 0, 'sex_age_hawaii_isl_f_55_59': 0, 'sex_age_hawaii_isl_f_60_61': 0, 'sex_age_hawaii_isl_f_62_64': 0, 'sex_age_hawaii_isl_f_65_66': 0, 'sex_age_hawaii_isl_f_67_69': 0, 'sex_age_hawaii_isl_f_70_74': 0, 'sex_age_hawaii_isl_f_75_79': 0, 'sex_age_hawaii_isl_f_80_84': 0, 'sex_age_hawaii_isl_f_85p': 0}



```


