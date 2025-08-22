from playwright.sync_api import sync_playwright
# Run python3 06_playwright_scraping.py in console to execute this script

url = "https://midu.dev"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False , slow_mo=1500)
    page = browser.new_page()
    page.goto(url)

    # Wait for the page to load completely
    page.wait_for_load_state("networkidle")

    # Get the title of the page
    title = page.title()
    print(f"Page title: {title}")

    # Get the first article anchor element and click it
    first_article_anchor = page.locator("article a").first
    print(f"First article anchor text: {first_article_anchor.text_content()}")
    first_article_anchor.click()

    # Wait for the page to load completely
    page.wait_for_load_state("networkidle")

    # Get the first image in the header and print its source
    first_image_locator = page.locator("header img")
    if first_image_locator.count() == 0:
        print("No image found")
        image_src = None
    else:
        first_image = first_image_locator.first
        image_src = first_image.get_attribute("src")
        print(f"First image source: {image_src}")

    # Add the complete URL to the image source if it's relative using urljoin

    # Scripting with xpath from a specific element containing "Contenido del curso"
    curso_content_container = page.locator('text="Contenido del curso"')
    curso_content_sibling = curso_content_container.locator('xpath=./div/')

    # Close the browser
    browser.close()