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
    whole_number = get_price(plasticplace_page)
    print(whole_number)


if __name__ == "__main__":
    main()
