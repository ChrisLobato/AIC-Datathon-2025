import os, time, json, re
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Set up headless Chrome WebDriver
options = Options()
options.add_argument("--headless")  # run in headless mode (no GUI)
options.add_argument("--incognito")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_professor_links(url):
    driver.get(url)
    time.sleep(2)

    # Close cookie popup if present
    try:
        driver.find_element(By.CLASS_NAME, 'Button__ButtonWrapper-sc-1xyxj6h-0').click()
    except:
        pass

    #Switch to Computer Science Department
    try:
        print("Trying to get department")
        searchDepartment = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/header/div/div/div[2]/div/div[2]/div/div[1]/div[2]/input') #//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div
        searchDepartment.click()
        time.sleep(2)
        searchDepartment.send_keys("Computer")
        time.sleep(2)
        searchDepartment.send_keys(Keys.DOWN)
        time.sleep(0.5)
        searchDepartment.send_keys(Keys.DOWN)
        time.sleep(0.5)
        searchDepartment.send_keys(Keys.DOWN)
        time.sleep(0.5)
        searchDepartment.send_keys(Keys.RETURN)
    except:
        print("couldnt search class")
        pass



    # Click "Show More" until all professors are loaded
    while True:
        try:
            # print("Trying to click")
            # break #uncomment if you want to do less professors
            show_more = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/main/div[2]/div[2]/button')
            # show_more = WebDriverWait(driver, 2).until(
            #     EC.element_to_be_clickable((By.CLASS_NAME, "Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 joxzkC"))
            # )
            show_more.click()
            # print("Successful click")
            time.sleep(0.5)
        except:
            break

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    professors = []
    cards = soup.find_all('a', {'class': 'TeacherCard__StyledTeacherCard-syjs0d-0'})

    for card in cards:
        name = card.find('div', {'class': 'CardName__StyledCardName-sc-1gyrgim-0'}).text.strip()
        link = "https://www.ratemyprofessors.com" + card['href']
        professors.append({'name': name, 'rmp_link': link})

    return professors

def fetch_ratings(full_link,name):
    driver.get(full_link)
    time.sleep(2)
    page_source = driver.page_source

    match = re.search(r"window\.__RELAY_STORE__\s*=\s*({.*?});", page_source)
    # print(match)
    if not match:
        return {"r1": 0, "r2": 0, "r3": 0, "r4": 0, "r5": 0}

    data = json.loads(match.group(1))

    ratings_list = []
    for value in data.values():
        if isinstance(value, dict) and value.get("__typename") == "Rating":
            rating_info = {
                "Professor": name,
                "class": value.get("class", ""),
                "difficulty rating": value.get("difficultyRating", ""),
                "quality": value.get("helpfulRating", ""),
                "would take again": value.get("wouldTakeAgain", ""),
                "grade": value.get("grade", ""),
                "attendance mandatory": value.get("attendanceMandatory", "")
            }
            ratings_list.append(rating_info)

    return ratings_list

def main():
    url = "https://www.ratemyprofessors.com/search/professors/971?q=*"
    prof_links = scrape_professor_links(url)
    # print(prof_links)
    all_data = []

    for prof in prof_links:
        print(f"Fetching {prof['name']}...")
        ratings = fetch_ratings(prof["rmp_link"],prof["name"])
        all_data.extend(ratings)

    # Create DataFrame and save as CSV
    df = pd.DataFrame(all_data)
    df.to_csv("professors.csv", index=False)
    print("✅ Saved to professors.csv")

if __name__ == "__main__":
    main()
    driver.quit()
