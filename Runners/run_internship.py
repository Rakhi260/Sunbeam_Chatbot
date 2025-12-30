import json
from Core.driver_manager import get_driver
from Scrapers.internship_scraper import InternshipScraper

if __name__ == "__main__":
    driver = get_driver()

    try:
        scraper = InternshipScraper(driver)
        data = scraper.scrape()

        with open("sunbeam_internship.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print("Internship_Page scrapped successfully")

    finally:
        driver.quit()
