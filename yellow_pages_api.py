import requests
from datetime import datetime
from bs4 import BeautifulSoup

class YpApi:
    def __init__(self):
        self.html_file = None
        self.search_terms = None
        self.extractor_path = None
        self.geo_location_terms = None
        self.rank_plier_path = "&page="
        self.extractor_path_multi = None
        self.route_path = "https://www.yellowpages.com/"
        self.now = str(datetime.now()).replace(" ", "--").split(".")[0].replace(":", "-")

    def __repr__(self):
        return f"Scraper object Initialized, with a route at {self.route_path} at {self.now.split('--')[1]}"

    # To generate the link for scraping
    def gen_extractor_link(self, search_term, geo_location_term, plier_rank=1):
        end_point = f"search?search_terms={search_term}&geo_location_terms={geo_location_term}"
        self.extractor_path = self.route_path + end_point + self.rank_plier_path + f"{plier_rank}"

        return self.extractor_path

    # Param parser for checking None objects
    def param_parser(self, param, href_parse=0):
        if href_parse:
            parse_element = param.a["href"] if param.a != None else None
        else:
            parse_element = param.text if param != None else None
        return parse_element

    # To generate the file name
    def name_gen(self, search_term, geo_location_term):
        self.now += f"_{search_term}_{geo_location_term}"
        return self.now

    # To scrape the webiste
    def scrape_extractor(self, search_term, geo_location_term, plier_rank=1, print_data=False):
        self.search_terms = search_term
        self.geo_location_terms = geo_location_term
        self.extractor_path = self.gen_extractor_link(self.search_terms, self.geo_location_terms, plier_rank)

        self.html_file = requests.get(self.extractor_path).text
        soup = BeautifulSoup(self.html_file, "lxml")

        categories = soup.find_all("div", class_="result")

        api_arr = []
        if print_data:
            print("")
        for category in categories:
            name = category.find("a", class_="business-name")
            status = self.param_parser(category.find("div", class_="open-status"))
            if (name != None):
                types = category.find("div", class_="categories").find_all("a")
                num = self.param_parser(category.find("h2", class_="n"))
                ph_num = self.param_parser(category.find("div", class_="phone"))
                info_website = name["href"]
                website = self.param_parser(category.find("div", class_="links"), href_parse=1)
                address = self.param_parser(category.find("div", class_="adr"))

                if print_data:
                    print(f"{num}")
                    print(f"Name: {name.text}")
                    print(f"Phone number: {ph_num}")
                    print(f"Categories: {[type_.text for type_ in types]}")
                    print(f"Status: {status}")
                    print(f"Address: {address}")
                    print(f"Website: {website}")
                    print(f"More info: https://www.yellowpages.com{info_website}")
                    print("-------------------------------------------------")
                    print("")

                dict_ = {"Name": name.text,
                         "Phone-number": ph_num,
                         "Categories": [type_.text for type_ in types],
                         "Status": status,
                         "Address": address,
                         "Website": website,
                         "More-info": f"https://www.yellowpages.com{info_website}"}

                api_arr.append(dict_)

        return api_arr

    # To write the scraped details in a file
    def scrape_extractor_in_file(self, search_term, geo_location_term, plier_rank=1):
        self.search_terms = search_term
        self.geo_location_terms = geo_location_term
        self.now = self.name_gen(self.search_terms, self.geo_location_terms)
        self.extractor_path = self.gen_extractor_link(self.search_terms, self.geo_location_terms, plier_rank)

        self.html_file = requests.get(self.extractor_path).text
        soup = BeautifulSoup(self.html_file, "lxml")

        categories = soup.find_all("div", class_="result")

        with open(f"Yellow-pages/{self.now}.txt", "w") as f:
            for category in categories:
                name = category.find("a", class_="business-name")
                status = self.param_parser(category.find("div", class_="open-status"))
                if (name != None):
                    types = category.find("div", class_="categories").find_all("a")
                    num = self.param_parser(category.find("h2", class_="n"))
                    ph_num = self.param_parser(category.find("div", class_="phone"))
                    info_website = name["href"]
                    website = self.param_parser(category.find("div", class_="links"), href_parse=1)
                    address = self.param_parser(category.find("div", class_="adr"))

                    f.write(f"{num}\n")
                    f.write(f"Name: {name.text}\n")
                    f.write(f"Phone number: {ph_num}\n")
                    f.write(f"Categories: {[type_.text for type_ in types]}\n")
                    f.write(f"Status: {status}\n")
                    f.write(f"Address: {address}\n")
                    f.write(f"Website: {website}\n")
                    f.write(f"More info: https://www.yellowpages.com{info_website}\n")
                    f.write("-------------------------------------------------\n")
                    f.write("\n")

    # To scrape multiple pages and generate more details for api
    def scrape_extractor_multi(self, search_term, geo_location_term, plier=10, print_data=False):
        self.search_terms = search_term
        self.geo_location_terms = geo_location_term

        api_arr = []
        for plier_rank in range(1, plier+1):
            self.extractor_path_multi = self.gen_extractor_link(self.search_terms,
                                                                self.geo_location_terms,
                                                                plier_rank)

            self.html_file = requests.get(self.extractor_path_multi).text
            soup = BeautifulSoup(self.html_file, "lxml")

            categories = soup.find_all("div", class_="result")

            if print_data:
                print("")
            for category in categories:
                name = category.find("a", class_="business-name")
                status = self.param_parser(category.find("div", class_="open-status"))
                if (name != None):
                    types = category.find("div", class_="categories").find_all("a")
                    num = self.param_parser(category.find("h2", class_="n"))
                    ph_num = self.param_parser(category.find("div", class_="phone"))
                    info_website = name["href"]
                    website = self.param_parser(category.find("div", class_="links"), href_parse=1)
                    address = self.param_parser(category.find("div", class_="adr"))

                    if print_data:
                        print(f"{num}")
                        print(f"Name: {name.text}")
                        print(f"Phone number: {ph_num}")
                        print(f"Categories: {[type_.text for type_ in types]}")
                        print(f"Status: {status}")
                        print(f"Address: {address}")
                        print(f"Website: {website}")
                        print(f"More info: https://www.yellowpages.com{info_website}")
                        print("-------------------------------------------------")
                        print("")

                    dict_ = {"Name": name.text,
                             "Phone-number": ph_num,
                             "Categories": [type_.text for type_ in types],
                             "Status": status,
                             "Address": address,
                             "Website": website,
                             "More-info": f"https://www.yellowpages.com{info_website}"}

                    api_arr.append(dict_)

        return api_arr

    # To write the details of multiple pages in a single file
    def scrape_extractor_multi_in_file(self, search_term, geo_location_term, plier=10):
        self.search_terms = search_term
        self.geo_location_terms = geo_location_term
        self.now = self.name_gen(self.search_terms, self.geo_location_terms) + f"_{plier}"

        with open(f"Yellow-pages/{self.now}.json", "w") as f:
            for plier_rank in range(1, plier + 1):
                self.extractor_path_multi = self.gen_extractor_link(self.search_terms,
                                                                    self.geo_location_terms,
                                                                    plier_rank)

                self.html_file = requests.get(self.extractor_path_multi).text
                soup = BeautifulSoup(self.html_file, "lxml")

                categories = soup.find_all("div", class_="result")

                for category in categories:
                    name = category.find("a", class_="business-name")
                    status = self.param_parser(category.find("div", class_="open-status"))
                    if (name != None):
                        types = category.find("div", class_="categories").find_all("a")
                        num = self.param_parser(category.find("h2", class_="n"))
                        ph_num = self.param_parser(category.find("div", class_="phone"))
                        info_website = name["href"]
                        website = self.param_parser(category.find("div", class_="links"), href_parse=1)
                        address = self.param_parser(category.find("div", class_="adr"))

                        f.write(f"{num}\n")
                        f.write(f"Name: {name.text}\n")
                        f.write(f"Phone number: {ph_num}\n")
                        f.write(f"Categories: {[type_.text for type_ in types]}\n")
                        f.write(f"Status: {status}\n")
                        f.write(f"Address: {address}\n")
                        f.write(f"Website: {website}\n")
                        f.write(f"More info: https://www.yellowpages.com{info_website}\n")
                        f.write("-------------------------------------------------\n")
                        f.write("\n")

    # To return tha array of api into a dictionary
    def get_api(self, json_arr):
        res_dict = {int(i + 1): elem for i, elem in enumerate(json_arr)}
        return res_dict


if __name__ == "__main__":
    api = YpApi()
    api.scrape_extractor_multi_in_file("auto-repair", "detroit", plier=2)
    # print(api)
