from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

import config
import text_list

# プロキシサーバーからアクセス
url = config.PROXY

driver = webdriver.Chrome()

driver.get(url)

# ログインページに飛ぶ
input_url = driver.find_element(By.ID,'url')
sleep(2)
input_url.send_keys(config.LOGIN_URL)
input_url.send_keys(Keys.ENTER)
sleep(5)

# ログイン情報入力
input_id = driver.find_element(By.ID,'email')
sleep(2)
input_id.send_keys(config.MAILADDRESS)
input_password = driver.find_element(By.ID,'password')
sleep(2)
input_password.send_keys(config.PASSWORD)

login_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/main/div/div[1]/div[5]/button')
login_button.click()

sleep(10)

# 投稿ボタン取得
posting_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/header/span/div/nav/div[3]/button')
posting_button.click()

sleep(10)

# 投稿のジャンル(今回の場合はテキスト)を取得
text_ul = driver.find_element(By.TAG_NAME,'ul')
text_li = text_ul.find_elements(By.TAG_NAME,'li')
text_link = text_li[0].find_element(By.TAG_NAME,'a')
get_text_link = text_link.get_attribute('href')

driver.get(get_text_link)

# ログイン情報入力
input_id = driver.find_element(By.ID,'email')
sleep(2)
input_id.send_keys(config.MAILADDRESS)
input_password = driver.find_element(By.ID,'password')
sleep(2)
input_password.send_keys(config.PASSWORD)

login_button = driver.find_element(By.XPATH,'//*[@id="__layout"]/div/div[1]/main/div/div[1]/div[5]/button')
login_button.click()

sleep(10)

############################################################
# 記事タイトルと内容を入力し、サムネイル画像はアップロードする。
############################################################

# 写真アイコンを取得
img_button = driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div[1]/div[2]/div[1]/main/div[1]/button/span/span')
img_button.click()

sleep(5)

# 画像アップロードを取得
img_upload = driver.find_element(By.XPATH,'//*[@id="__next"]/div[3]/div[1]/div[2]/div[1]/main/div[1]/div/div[1]/button')
img_upload.click()

path = config.PATH

# 画像をアップロードする
upload_input = driver.find_element(By.CSS_SELECTOR, 'input[type="file"]')
upload_input.send_keys(path)

sleep(5)

# 保存する
save_img = driver.find_element(By.XPATH,'//span[text()="保存"]/..')
save_img.click()

sleep(10)

# テキスト入力
input_text = driver.find_element(By.CSS_SELECTOR,'[contenteditable=true]')
input_text.send_keys(text_list.TEXT)

sleep(5)

# 記事タイトル入力
input_title = driver.find_element(By.TAG_NAME,'textarea')
input_title.send_keys(text_list.TITLE)

sleep(1)

# 公開する
public_posting = driver.find_element(By.XPATH, '//span[text()="公開に進む"]/..')
public_posting.click()

sleep(1)

# 投稿する
posting = driver.find_element(By.XPATH, '//span[text()="投稿する"]/..')
posting.click()

sleep(5)

driver.close()