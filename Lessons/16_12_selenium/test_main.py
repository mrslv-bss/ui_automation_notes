from testdata.testdata import word
from pages.main_page import search_field_loc, search_button_loc
from pages.searched_result_page import top_tabs_images_loc, search_field_searched_loc, no_results_loc
from Libs.basic import sendkeys, start, click, check_inputted, get_result, check_word_title


if __name__ == '__main__':
    start()
    sendkeys(search_field_loc, word)
    click(search_button_loc, top_tabs_images_loc)
    assert check_inputted(search_field_searched_loc) == word
    assert get_result(no_results_loc) != 0
    assert check_word_title() == True
