from utils import bs4_utility  # type: ignore
from utils import functions
from utils import Data


def main():
    first_search()
    # soup = bs4_utility.scrape_website(
    #     Data.PLASTICPLACE_TRASH_BAGS_SMALL_8_GAL_1000)
    # print(soup.find('span', id='productTitle'))
    # title = 'Plasticplace 8 Gallon Trash Bags │ 0.7 Mil │ White Drawstring Garbage Can Liners │ 22" x 22" (200 Case), Count       </span>'


def first_search():
    try:
        plasticplace_page = bs4_utility.scrape_website(
        Data.PLASTICPLACE_TRASH_BAGS_SMALL_8_GAL_1000)
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
    # try:
    #     title = functions.get_title(plasticplace_page)
    # except BaseException as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    # try:
    #     whole_number = functions.get_price(plasticplace_page)
    # except BaseException as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    # try:
    #     item_type = functions.get_item_type(plasticplace_page)
    # except BaseException as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    # try:
    #     count_price = functions.get_count_price(plasticplace_page)
    # except BaseException as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
    # try:
        t = functions.check_count(plasticplace_page)
    # except BaseException as err:
    #     print(f"Unexpected {err=}, {type(err)=}")
        
    print(t)


if __name__ == "__main__":
    main()
