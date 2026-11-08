"""Demo 02: print a hypothetical snippet for review; do not execute it."""


def main() -> None:
    # The Selenium-like code is printed as text, not executed. The placeholder
    # URL does not point to an application under test.
    print("[HYPOTHETICAL AI-GENERATED SELENIUM DRAFT — NOT EXECUTED]")
    print("""driver.get("https://example.invalid/cart")
driver.find_element("css selector", "#add-item").click()
driver.find_element("css selector", "#checkout").click()
# No assertion about delivery charge; no gift-card example.""")
    # Clicking through checkout alone cannot verify the delivery charge.
    # The draft has no assertion and does not cover the excluded gift card.
    print("[REVIEW] What delivery charge should the test assert for £40 goods + £10 gift card? £5.")
    # A browser test would need stable locators and explicit waits to observe
    # the result reliably; this script requires no browser or Selenium package.
    print("[REVIEW] What stable locators and explicit waits would the real app support?")
    print("[LIMIT] No browser, app, Selenium import, or AI call occurs in this demo.")


# Avoid printing the example when this module is imported.
if __name__ == "__main__":
    main()