from selenium import webdriver
import logging

# quick and dirty -
# set up some default logging
# use selenium browser automation to request page, parse and log interesting values


# set default logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# handler for logging to file
# create a handler to log on the filesystem
file_handler = logging.FileHandler('sneaker_release_finishline.log')
# file_handler.setFormatter()
file_handler.setLevel(logging.INFO)

# handler for logging to console
stream_handler = logging.StreamHandler()
# stream_handler.setFormatter()
stream_handler.setLevel(logging.INFO)

# add handlers to root logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# configure browser and options
    # driver
geckodriver = '/home/ou/applications/gecko_driver/geckodriver'
    # options
options = webdriver.FirefoxOptions()
options.add_argument('-headless')

browser = webdriver.Firefox(executable_path=geckodriver, options=options)

# request url
browser.get('https://finishline.com/store/sneaker-release-dates?mnid=release_calendar')

# log sneaker release dates
for ele in browser.find_elements_by_tag_name('h2'):

    for dateI in browser.find_elements_by_class_name('muted'):

        for dateD in browser.find_elements_by_tag_name('h3'):
            if "text-left mt-3" in dateD.get_attribute('class'):
                if ele.text:
                    logger.info(dateD.text + " " + ele.text + " " + dateI.text)

browser.quit()

