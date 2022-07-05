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
    plasticplace_page = bs4_utility.scrape_website(
        Data.PLASTICPLACE_TRASH_BAGS_SMALL_8_GAL_1000)
    # title = functions.get_title(plasticplace_page)
    # whole_number = functions.get_price(plasticplace_page)
    # item_type = functions.get_item_type(plasticplace_page)
    # count_price = functions.get_count_price(plasticplace_page)


if __name__ == "__main__":
    main()
