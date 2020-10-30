import sys
from selenium import webdriver


def test_scores_service(url):
    driver = webdriver.Firefox(executable_path=r'C:\Users\danieleh\PycharmProjects\daniele\venv\MyScripts\geckodriver.exe')
    driver.get(url)
    get_score = driver.find_element_by_id("score").text
    print("Score = {}".format(get_score))
    driver.close()
    if 0 < int(get_score) < 1000:
        return 0
    else:
        return 1


def main_function():
    score = test_scores_service("http://localhost:8777/")
    if score == 0:
        print("UNIT TEST passed success")
        sys.exit(0)
    else:
        print("UNIT TEST failed")
        sys.exit(1)


main_function()
