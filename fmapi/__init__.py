"Foundation Mercury Python API Client"

import decimal

import requests


def samples():
    "Samples"
    gets = [
        "/api/census2010/states",
        "/api/census2010/counties/12",
        "/api/census2010/tracts/12/001",
        "/api/census2010/blocks/12/001/000200",
        "/api/census2010/dp/12/001/000301",
        "/api/census2010/sf1basic/state/12/county/097",
        "/api/census2010/zcta5/12",
        "/api/census2010/sf1basic/state/12/zcta5/34746",
        "/api/census2010/sf1basic/state/12/county/001/tract/000301",
        "/api/census2010/sf1basic/state/12/county/001/tract/000200/block/1001",
        "/api/cities/FL",
        "/api/census2010/sf1/01/12/001/000200/1000",
        "/api/census2010/sf1/03/12/001/000200/1000",
        "/api/census2010/sf1/05/12/001/000200/1000",
        "/api/census2010/sf1/06/12/001/000200/1000",
        "/api/census2010/sf1/07/12/001/000200/1000",
        "/api/census2010/sf1/03/docs",
        "/api/geocode/770%20Maple%20Ridge%20Rd,Palm%20Harbor%20FL%2034683",
        "/api/neighborhood/1/census2010/tract",
        "/api/neighborhoods/state/FL/city/Kissimmee",
        "/api/neighborhood/10",
        "/api/revgeocode/28.08893740/-82.75338220"
    ]


URL_BASE = "https://www.foundationmercury.com/api"
    

class CensusState():
    "A US State"
    def __init__(self, d=None):
        self.name = ""
        self.state_abbrev = ""
        self.state_code = ""
        if d:
            self.name = d["name"]
            self.state_abbrev = d["state_abbrev"]
            self.state_code = d["state_code"]


class CensusCounty():
    "A US County or County Equivalent"
    def __init__(self, d=None):
        self.name = ""
        self.county_code = ""
        self.lat = decimal.Decimal(0)
        self.lon = decimal.Decimal(0)
        if d is not None:
            self.name = d["name"]
            self.county_code = d["county_code"]
            self.lat = decimal.Decimal(d["lat"])
            self.lon = decimal.Decimal(d["lon"])


class CensusTract():
    "A census tract"
    def __init__(self, d=None):
        self.name = ""
        self.tract_code = ""
        self.lat = decimal.Decimal(0)
        self.lon = decimal.Decimal(0)
        if d is not None:
            self.name = d["name"]
            self.tract_code = d["tract_code"]
            self.lat = decimal.Decimal(d["lat"])
            self.lon = decimal.Decimal(d["lon"])


class CensusBlock():
    "A census block"
    def __init__(self, d=None):
        self.name = ""
        self.block_code = ""
        self.lat = decimal.Decimal(0)
        self.lon = decimal.Decimal(0)
        if d is not None:
            self.name = d["name"]
            self.block_code = d["block_code"]
            self.lat = decimal.Decimal(d["lat"])
            self.lon = decimal.Decimal(d["lon"])


class TractDemographicProfile(): #pylint:disable=R0902
    "Demographic Profile data for a single census tract"
    def __init__(self, d=None): #pylint:disable=R0915
        self.sex_age_total = 0
        self.sex_age_under_5 = 0
        self.sex_age_5_9 = 0
        self.sex_age_10_14 = 0
        self.sex_age_15_19 = 0
        self.sex_age_20_24 = 0
        self.sex_age_25_29 = 0
        self.sex_age_30_34 = 0
        self.sex_age_35_39 = 0
        self.sex_age_40_44 = 0
        self.sex_age_45_49 = 0
        self.sex_age_50_54 = 0
        self.sex_age_55_59 = 0
        self.sex_age_60_64 = 0
        self.sex_age_65_69 = 0
        self.sex_age_70_74 = 0
        self.sex_age_75_79 = 0
        self.sex_age_80_84 = 0
        self.sex_age_85_plus = 0
        self.sex_age_total_m = 0
        self.sex_age_under_5_m = 0
        self.sex_age_5_9_m = 0
        self.sex_age_10_14_m = 0
        self.sex_age_15_19_m = 0
        self.sex_age_20_24_m = 0
        self.sex_age_25_29_m = 0
        self.sex_age_30_34_m = 0
        self.sex_age_35_39_m = 0
        self.sex_age_40_44_m = 0
        self.sex_age_45_49_m = 0
        self.sex_age_50_54_m = 0
        self.sex_age_55_59_m = 0
        self.sex_age_60_64_m = 0
        self.sex_age_65_69_m = 0
        self.sex_age_70_74_m = 0
        self.sex_age_75_79_m = 0
        self.sex_age_80_84_m = 0
        self.sex_age_85_plus_m = 0
        self.sex_age_total_f = 0
        self.sex_age_under_5_f = 0
        self.sex_age_5_9_f = 0
        self.sex_age_10_14_f = 0
        self.sex_age_15_19_f = 0
        self.sex_age_20_24_f = 0
        self.sex_age_25_29_f = 0
        self.sex_age_30_34_f = 0
        self.sex_age_35_39_f = 0
        self.sex_age_40_44_f = 0
        self.sex_age_45_49_f = 0
        self.sex_age_50_54_f = 0
        self.sex_age_55_59_f = 0
        self.sex_age_60_64_f = 0
        self.sex_age_65_69_f = 0
        self.sex_age_70_74_f = 0
        self.sex_age_75_79_f = 0
        self.sex_age_80_84_f = 0
        self.sex_age_85_plus_f = 0
        self.median_age_both = 0
        self.median_age_m = 0
        self.median_age_f = 0
        self.sex_16_over_both = 0
        self.sex_16_over_m = 0
        self.sex_16_over_f = 0
        self.sex_18_over_both = 0
        self.sex_18_over_m = 0
        self.sex_18_over_f = 0
        self.sex_21_over_both = 0
        self.sex_21_over_m = 0
        self.sex_21_over_f = 0
        self.sex_62_over_both = 0
        self.sex_62_over_m = 0
        self.sex_62_over_f = 0
        self.sex_65_over_both = 0
        self.sex_65_over_m = 0
        self.sex_65_over_f = 0
        self.race_total = 0
        self.race_one = 0
        self.race_white = 0
        self.race_black = 0
        self.race_native = 0
        self.race_asian = 0
        self.race_asian_indian = 0
        self.race_chinese = 0
        self.race_filipino = 0
        self.race_japanese = 0
        self.race_korean = 0
        self.race_vietnamese = 0
        self.race_other_asian = 0
        self.race_pacific = 0
        self.race_native_hawaiian = 0
        self.race_guam = 0
        self.race_samoam = 0
        self.race_other_pacific = 0
        self.race_other = 0
        self.race_two = 0
        self.race_white_native = 0
        self.race_white_asian = 0
        self.race_white_black = 0
        self.race_white_other = 0
        self.race_white_alone = 0
        self.race_black_alone = 0
        self.race_native_alone = 0
        self.race_asian_alone = 0
        self.race_hawaiian_alone = 0
        self.race_other_alone = 0
        self.hisp_not_total = 0
        self.hisp = 0
        self.mexican = 0
        self.puerto_rican = 0
        self.cuban = 0
        self.other_hisp = 0
        self.not_hisp = 0
        self.hisp_race_total = 0
        self.hisp_race_h = 0
        self.hisp_race_h_white = 0
        self.hisp_race_h_black = 0
        self.hisp_race_h_native = 0
        self.hisp_race_h_asian = 0
        self.hisp_race_h_hawaiian = 0
        self.hisp_race_h_other = 0
        self.hisp_race_h_two = 0
        self.hisp_race_noth = 0
        self.hisp_race_noth_white = 0
        self.hisp_race_noth_black = 0
        self.hisp_race_noth_native = 0
        self.hisp_race_noth_asian = 0
        self.hisp_race_noth_hawaiian = 0
        self.hisp_race_noth_other = 0
        self.hisp_race_noth_two = 0
        self.rel_total = 0
        self.rel_house = 0
        self.rel_house_holder = 0
        self.rel_house_spouse = 0
        self.rel_house_child = 0
        self.rel_house_child_18 = 0
        self.rel_house_other = 0
        self.rel_house_other_18 = 0
        self.rel_house_other_65 = 0
        self.rel_house_nonrel = 0
        self.rel_house_nonrel_18 = 0
        self.rel_house_nonrel_65 = 0
        self.rel_house_nonrel_unmp = 0
        self.rel_group = 0
        self.rel_group_inst = 0
        self.rel_group_inst_m = 0
        self.rel_group_inst_f = 0
        self.rel_group_noninst = 0
        self.rel_group_noninst_m = 0
        self.rel_group_noninst_f = 0
        self.house_total = 0
        self.house_family = 0
        self.house_family_18 = 0
        self.house_family_hw = 0
        self.house_family_hw_18 = 0
        self.house_family_m = 0
        self.house_family_m_18 = 0
        self.house_family_f = 0
        self.house_family_f_18 = 0
        self.house_nonfam = 0
        self.house_nonfam_alone = 0
        self.house_nonfam_m = 0
        self.house_nonfam_m_65 = 0
        self.house_nonfam_f = 0
        self.house_nonfam_f_65 = 0
        self.house_18 = 0
        self.house_65 = 0
        self.avg_house_size = decimal.Decimal(0)
        self.avg_fam_size = decimal.Decimal(0)
        self.occu_total = 0
        self.occu_occu = 0
        self.occu_vacant = 0
        self.occu_vacant_for_rent = 0
        self.occu_vacant_rented = 0
        self.occu_vacant_sale_only = 0
        self.occu_vacant_sold = 0
        self.occu_vacant_seasonal = 0
        self.occu_vacant_other = 0
        self.homeowner_vacany_rate = decimal.Decimal(0)
        self.rental_vacancy_rate = decimal.Decimal(0)
        self.tenure_total = 0
        self.tenure_owner = 0
        self.tenure_renter = 0
        self.pop_tenure_owner = 0
        self.pop_tenure_renter = 0
        self.avg_house_size_owner = decimal.Decimal(0)
        self.avg_house_size_renter = decimal.Decimal(0)
        if d is not None:
            self.sex_age_total = d["sex_age_total"]
            self.sex_age_under_5 = d["sex_age_under_5"]
            self.sex_age_5_9 = d["sex_age_5_9"]
            self.sex_age_10_14 = d["sex_age_10_14"]
            self.sex_age_15_19 = d["sex_age_15_19"]
            self.sex_age_20_24 = d["sex_age_20_24"]
            self.sex_age_25_29 = d["sex_age_25_29"]
            self.sex_age_30_34 = d["sex_age_30_34"]
            self.sex_age_35_39 = d["sex_age_35_39"]
            self.sex_age_40_44 = d["sex_age_40_44"]
            self.sex_age_45_49 = d["sex_age_45_49"]
            self.sex_age_50_54 = d["sex_age_50_54"]
            self.sex_age_55_59 = d["sex_age_55_59"]
            self.sex_age_60_64 = d["sex_age_60_64"]
            self.sex_age_65_69 = d["sex_age_65_69"]
            self.sex_age_70_74 = d["sex_age_70_74"]
            self.sex_age_75_79 = d["sex_age_75_79"]
            self.sex_age_80_84 = d["sex_age_80_84"]
            self.sex_age_85_plus = d["sex_age_85_plus"]
            self.sex_age_total_m = d["sex_age_total_m"]
            self.sex_age_under_5_m = d["sex_age_under_5_m"]
            self.sex_age_5_9_m = d["sex_age_5_9_m"]
            self.sex_age_10_14_m = d["sex_age_10_14_m"]
            self.sex_age_15_19_m = d["sex_age_15_19_m"]
            self.sex_age_20_24_m = d["sex_age_20_24_m"]
            self.sex_age_25_29_m = d["sex_age_25_29_m"]
            self.sex_age_30_34_m = d["sex_age_30_34_m"]
            self.sex_age_35_39_m = d["sex_age_35_39_m"]
            self.sex_age_40_44_m = d["sex_age_40_44_m"]
            self.sex_age_45_49_m = d["sex_age_45_49_m"]
            self.sex_age_50_54_m = d["sex_age_50_54_m"]
            self.sex_age_55_59_m = d["sex_age_55_59_m"]
            self.sex_age_60_64_m = d["sex_age_60_64_m"]
            self.sex_age_65_69_m = d["sex_age_65_69_m"]
            self.sex_age_70_74_m = d["sex_age_70_74_m"]
            self.sex_age_75_79_m = d["sex_age_75_79_m"]
            self.sex_age_80_84_m = d["sex_age_80_84_m"]
            self.sex_age_85_plus_m = d["sex_age_85_plus_m"]
            self.sex_age_total_f = d["sex_age_total_f"]
            self.sex_age_under_5_f = d["sex_age_under_5_f"]
            self.sex_age_5_9_f = d["sex_age_5_9_f"]
            self.sex_age_10_14_f = d["sex_age_10_14_f"]
            self.sex_age_15_19_f = d["sex_age_15_19_f"]
            self.sex_age_20_24_f = d["sex_age_20_24_f"]
            self.sex_age_25_29_f = d["sex_age_25_29_f"]
            self.sex_age_30_34_f = d["sex_age_30_34_f"]
            self.sex_age_35_39_f = d["sex_age_35_39_f"]
            self.sex_age_40_44_f = d["sex_age_40_44_f"]
            self.sex_age_45_49_f = d["sex_age_45_49_f"]
            self.sex_age_50_54_f = d["sex_age_50_54_f"]
            self.sex_age_55_59_f = d["sex_age_55_59_f"]
            self.sex_age_60_64_f = d["sex_age_60_64_f"]
            self.sex_age_65_69_f = d["sex_age_65_69_f"]
            self.sex_age_70_74_f = d["sex_age_70_74_f"]
            self.sex_age_75_79_f = d["sex_age_75_79_f"]
            self.sex_age_80_84_f = d["sex_age_80_84_f"]
            self.sex_age_85_plus_f = d["sex_age_85_plus_f"]
            self.median_age_both = d["median_age_both"]
            self.median_age_m = d["median_age_m"]
            self.median_age_f = d["median_age_f"]
            self.sex_16_over_both = d["sex_16_over_both"]
            self.sex_16_over_m = d["sex_16_over_m"]
            self.sex_16_over_f = d["sex_16_over_f"]
            self.sex_18_over_both = d["sex_18_over_both"]
            self.sex_18_over_m = d["sex_18_over_m"]
            self.sex_18_over_f = d["sex_18_over_f"]
            self.sex_21_over_both = d["sex_21_over_both"]
            self.sex_21_over_m = d["sex_21_over_m"]
            self.sex_21_over_f = d["sex_21_over_f"]
            self.sex_62_over_both = d["sex_62_over_both"]
            self.sex_62_over_m = d["sex_62_over_m"]
            self.sex_62_over_f = d["sex_62_over_f"]
            self.sex_65_over_both = d["sex_65_over_both"]
            self.sex_65_over_m = d["sex_65_over_m"]
            self.sex_65_over_f = d["sex_65_over_f"]
            self.race_total = d["race_total"]
            self.race_one = d["race_one"]
            self.race_white = d["race_white"]
            self.race_black = d["race_black"]
            self.race_native = d["race_native"]
            self.race_asian = d["race_asian"]
            self.race_asian_indian = d["race_asian_indian"]
            self.race_chinese = d["race_chinese"]
            self.race_filipino = d["race_filipino"]
            self.race_japanese = d["race_japanese"]
            self.race_korean = d["race_korean"]
            self.race_vietnamese = d["race_vietnamese"]
            self.race_other_asian = d["race_other_asian"]
            self.race_pacific = d["race_pacific"]
            self.race_native_hawaiian = d["race_native_hawaiian"]
            self.race_guam = d["race_guam"]
            self.race_samoam = d["race_samoam"]
            self.race_other_pacific = d["race_other_pacific"]
            self.race_other = d["race_other"]
            self.race_two = d["race_two"]
            self.race_white_native = d["race_white_native"]
            self.race_white_asian = d["race_white_asian"]
            self.race_white_black = d["race_white_black"]
            self.race_white_other = d["race_white_other"]
            self.race_white_alone = d["race_white_alone"]
            self.race_black_alone = d["race_black_alone"]
            self.race_native_alone = d["race_native_alone"]
            self.race_asian_alone = d["race_asian_alone"]
            self.race_hawaiian_alone = d["race_hawaiian_alone"]
            self.race_other_alone = d["race_other_alone"]
            self.hisp_not_total = d["hisp_not_total"]
            self.hisp = d["hisp"]
            self.mexican = d["mexican"]
            self.puerto_rican = d["puerto_rican"]
            self.cuban = d["cuban"]
            self.other_hisp = d["other_hisp"]
            self.not_hisp = d["not_hisp"]
            self.hisp_race_total = d["hisp_race_total"]
            self.hisp_race_h = d["hisp_race_h"]
            self.hisp_race_h_white = d["hisp_race_h_white"]
            self.hisp_race_h_black = d["hisp_race_h_black"]
            self.hisp_race_h_native = d["hisp_race_h_native"]
            self.hisp_race_h_asian = d["hisp_race_h_asian"]
            self.hisp_race_h_hawaiian = d["hisp_race_h_hawaiian"]
            self.hisp_race_h_other = d["hisp_race_h_other"]
            self.hisp_race_h_two = d["hisp_race_h_two"]
            self.hisp_race_noth = d["hisp_race_noth"]
            self.hisp_race_noth_white = d["hisp_race_noth_white"]
            self.hisp_race_noth_black = d["hisp_race_noth_black"]
            self.hisp_race_noth_native = d["hisp_race_noth_native"]
            self.hisp_race_noth_asian = d["hisp_race_noth_asian"]
            self.hisp_race_noth_hawaiian = d["hisp_race_noth_hawaiian"]
            self.hisp_race_noth_other = d["hisp_race_noth_other"]
            self.hisp_race_noth_two = d["hisp_race_noth_two"]
            self.rel_total = d["rel_total"]
            self.rel_house = d["rel_house"]
            self.rel_house_holder = d["rel_house_holder"]
            self.rel_house_spouse = d["rel_house_spouse"]
            self.rel_house_child = d["rel_house_child"]
            self.rel_house_child_18 = d["rel_house_child_18"]
            self.rel_house_other = d["rel_house_other"]
            self.rel_house_other_18 = d["rel_house_other_18"]
            self.rel_house_other_65 = d["rel_house_other_65"]
            self.rel_house_nonrel = d["rel_house_nonrel"]
            self.rel_house_nonrel_18 = d["rel_house_nonrel_18"]
            self.rel_house_nonrel_65 = d["rel_house_nonrel_65"]
            self.rel_house_nonrel_unmp = d["rel_house_nonrel_unmp"]
            self.rel_group = d["rel_group"]
            self.rel_group_inst = d["rel_group_inst"]
            self.rel_group_inst_m = d["rel_group_inst_m"]
            self.rel_group_inst_f = d["rel_group_inst_f"]
            self.rel_group_noninst = d["rel_group_noninst"]
            self.rel_group_noninst_m = d["rel_group_noninst_m"]
            self.rel_group_noninst_f = d["rel_group_noninst_f"]
            self.house_total = d["house_total"]
            self.house_family = d["house_family"]
            self.house_family_18 = d["house_family_18"]
            self.house_family_hw = d["house_family_hw"]
            self.house_family_hw_18 = d["house_family_hw_18"]
            self.house_family_m = d["house_family_m"]
            self.house_family_m_18 = d["house_family_m_18"]
            self.house_family_f = d["house_family_f"]
            self.house_family_f_18 = d["house_family_f_18"]
            self.house_nonfam = d["house_nonfam"]
            self.house_nonfam_alone = d["house_nonfam_alone"]
            self.house_nonfam_m = d["house_nonfam_m"]
            self.house_nonfam_m_65 = d["house_nonfam_m_65"]
            self.house_nonfam_f = d["house_nonfam_f"]
            self.house_nonfam_f_65 = d["house_nonfam_f_65"]
            self.house_18 = d["house_18"]
            self.house_65 = d["house_65"]
            self.avg_house_size = d["avg_house_size"]
            self.avg_fam_size = d["avg_fam_size"]
            self.occu_total = d["occu_total"]
            self.occu_occu = d["occu_occu"]
            self.occu_vacant = d["occu_vacant"]
            self.occu_vacant_for_rent = d["occu_vacant_for_rent"]
            self.occu_vacant_rented = d["occu_vacant_rented"]
            self.occu_vacant_sale_only = d["occu_vacant_sale_only"]
            self.occu_vacant_sold = d["occu_vacant_sold"]
            self.occu_vacant_seasonal = d["occu_vacant_seasonal"]
            self.occu_vacant_other = d["occu_vacant_other"]
            self.homeowner_vacany_rate = d["homeowner_vacany_rate"]
            self.rental_vacancy_rate = d["rental_vacancy_rate"]
            self.tenure_total = d["tenure_total"]
            self.tenure_owner = d["tenure_owner"]
            self.tenure_renter = d["tenure_renter"]
            self.pop_tenure_owner = d["pop_tenure_owner"]
            self.pop_tenure_renter = d["pop_tenure_renter"]
            self.avg_house_size_owner = d["avg_house_size_owner"]
            self.avg_house_size_renter = d["avg_house_size_renter"]




class Client():
    "API Client"

    def __init__(self, username=None, password=None, url_base=None):
        # If these are None, requests will look in .netrc for auth
        self.username = username
        self.password = password
        self.url_base = url_base
        if self.url_base is None:
            self.url_base = URL_BASE


    def get(self, url):
        "Call an API GET endpoint"
        full_url = self.url_base + url
        r = None
        if self.username:
            r = requests.get(full_url, auth=(self.username, self.password))
        else:
            r = requests.get(full_url) # Uses .netrc
        return r.json()
    

    def get_states(self):
        "Get a list of US states"
        j = self.get("/census2010/states")
        states = []
        for d in j:
            states.append(CensusState(d))
        return states


    def get_counties(self, state_code):
        "Get the counties in one state"
        j = self.get("/census2010/counties/" + state_code)
        counties = []
        for d in j:
            counties.append(CensusCounty(d))
        return counties


    def get_tracts(self, state_code, county_code):
        "Get the census tracts in one county"
        j = self.get(
            "/census2010/tracts/{}/{}".format(state_code, county_code))
        tracts = []
        for d in j:
            tracts.append(CensusTract(d))
        return tracts


    def get_blocks(self, state_code, county_code, tract_code):
        "Get the census blocks in one tract"
        j = self.get(
            "/census2010/blocks/{}/{}/{}".format(
                state_code, county_code, tract_code))
        blocks = []
        for d in j:
            blocks.append(CensusBlock(d))
        return blocks


    def get_tract_profile(self, state_code, county_code, tract_code):
        "Get the demographic profile for the census tract"
        j = self.get(
            "/census2010/dp/{}/{}/{}".format(
                state_code, county_code, tract_code))
        dp = TractDemographicProfile(j[0])
        return dp
    

