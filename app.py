from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:
    # Lauch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new page
    page = browser.new_page()
    # Visit the website
    page.goto("https://navpro.dasa.com.br")

    # Locate a link element with "Entrar" text
    titulo_text = page.get_by_text('A plataforma para gestão de exames ')
    exames_button = page.get_by_role('link', name="Exames")
    exames_button.click()

    #Get the url
    print("Exames:", page.url)

    browser.close()