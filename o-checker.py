from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
import os
import argparse
from telegram import ParseMode
from telegram.ext import Updater, CommandHandler
import time
import json
import sys


EMAIL = os.getenv('UNIPR_EMAIL')
PASSWORD = os.getenv('UNIPR_PASSWORD')
TOKEN = os.getenv('TELEGRAM_TOKEN')


class VideoChecker:
    def __init__(self):
        self.setup_args()
        if TOKEN is not None:
            self.updater = Updater(token=TOKEN, use_context=True)
            dispatcher = self.updater.dispatcher
            dispatcher.add_handler(CommandHandler("start", start))
            self.updater.start_polling()
        if not self.args.test:
            self.check_vids()
        else:
            print("Bot idling!")
            self.updater.idle()

    def setup_args(self):
        '''Parse the given arguments'''
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '--url',
                            dest='url', type=str)
        parser.add_argument('-c', '--chat', dest='chat', type=str)
        parser.add_argument('-t', '--test', help='Print more data',
                            action='store_true')
        self.args = parser.parse_args()

    def check_vids(self):
        # Create the webdriver
        self.driver = webdriver.Firefox()
        self.driver.get(self.args.url)
        assert "Accesso" in self.driver.title
        email_input = None
        while email_input == None:
            email_input = self.driver.find_element_by_xpath(
                "//*[contains(@placeholder, 'posta')]")
        email_input.click()
        email_input.send_keys(EMAIL)
        email_input.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        password_input = None
        while password_input is None:
            password_input = self.driver.find_element_by_id("passwordInput")
        password_input.click()
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.RETURN)
        no_btn = None
        while no_btn == None:
            no_btn = self.driver.find_element_by_id("idBtn_Back")
        no_btn.click()
        self.driver.get(self.args.url)
        self.scroll_down()
        self.videos = self.driver.find_elements_by_class_name(
            "video-list-item-title")
        self.check_if_new()
        self.driver.close()
        self.updater.stop()

    def check_if_new(self):
        file_name = self.args.url.split('/')[-1]+".json"
        if len(file_name) == 0:
            file_name = self.args.url.split('/')[-2]
        new_vids = []
        if not os.path.exists(file_name):
            with open(file_name, 'w') as vids_file:
                json.dump([], vids_file)
        with open(file_name, 'r') as vids_file:
            old_vids = json.load(vids_file)
        if len(old_vids) != len(self.videos):
            for video in self.videos:
                if video.get_attribute('href') not in old_vids:
                    new_vids.append((video.get_attribute(
                        'href'), video.get_attribute('aria-label')))
                    old_vids.append(video.get_attribute('href'))
        with open(file_name, 'w') as vids_file:
            json.dump(old_vids, vids_file)
        if len(new_vids) > 0:
            self.notify_new_vids(new_vids)

    def notify_new_vids(self, new_vids):
        self.prof_name = self.driver.find_element_by_class_name(
            'name-line').text
        if TOKEN is not None:
            for video in new_vids:
                text = "Hai un nuovo video del prof. " + \
                    self.prof_name+"\n["+video[1]+"]("+video[0]+")"
                self.updater.bot.send_message(
                    chat_id=self.args.chat, text=text, parse_mode=ParseMode.MARKDOWN)

    def scroll_down(self):
        """A method for scrolling the page."""

        # Get scroll height.
        last_height = self.driver.execute_script(
            "return document.body.scrollHeight")

        while True:

            # Scroll down to the bottom.
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load the page.
            time.sleep(4)
            try:
                scroll_btn = self.driver.find_element_by_class_name(
                    "show-more")
                scroll_btn.click()
            except:
                pass
            # Calculate new scroll height and compare with last scroll height.
            new_height = self.driver.execute_script(
                "return document.body.scrollHeight")

            if new_height == last_height:

                break

            last_height = new_height


def start(update, context):
    '''reply to /start cmd'''
    print(update.message.chat_id)
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Correctly printed your chat ID\n")


def main():
    video_checker = VideoChecker()


if __name__ == '__main__':
    main()
