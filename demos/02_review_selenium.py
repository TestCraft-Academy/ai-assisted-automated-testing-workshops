"""Demo 02: print a hypothetical snippet for review; do not execute it."""


def main() -> None:
    print("[HYPOTHETICAL AI-GENERATED SELENIUM DRAFT — NOT EXECUTED]")
    print("""driver.get("https://example.invalid/cart")
driver.find_element("css selector", "#add-item").click()
driver.find_element("css selector", "#checkout").click()
# No assertion about delivery charge; no gift-card example.""")
    print("[REVIEW] What delivery charge should the test assert for £40 goods + £10 gift card? £5.")
    print("[REVIEW] What stable locators and explicit waits would the real app support?")
    print("[LIMIT] No browser, app, Selenium import, or AI call occurs in this demo.")


if __name__ == "__main__":
    main()