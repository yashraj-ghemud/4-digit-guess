from playwright.sync_api import sync_playwright

URL = "https://yashraj-ghemud.github.io/4-digit-guess/"


def main():
    with sync_playwright() as p:
        # headless=False = you can SEE browser cracking live 😈
        # slow_mo = adds delay (0 is fastest)
        browser = p.chromium.launch(headless=False, slow_mo=0)
        page = browser.new_page()

        print("[*] Opening website...")
        page.goto(URL, wait_until="domcontentloaded")

        # ====== Elements (from your website) ======
        code_input = page.locator("#codeInput")
        submit_btn = page.locator("#submitBtn")
        modal = page.locator("#modal")
        modal_code = page.locator("#modalCode")

        # Make sure input exists
        code_input.wait_for(timeout=10000)

        print("[*] Website opened ✅")
        print("[*] Starting brute force 0000 → 9999...")

        for i in range(10000):
            guess = f"{i:04d}"

            # ====== Terminal animation (same line) ======
            print(f"\rTrying: {guess}", end="", flush=True)

            # Fill guess and submit
            code_input.fill(guess)
            submit_btn.click()

            # If modal is visible => success
            if modal.is_visible():
                found_code = modal_code.inner_text().strip()

                print("\n\n✅ DONE! ACCESS GRANTED!")
                print(f"🎯 Correct Code Found: {found_code}")
                print(f"🧠 Attempts Taken: {i + 1}")
                browser.close()
                return

        print("\n\n❌ Finished all combos (0000-9999), but no success detected.")
        print("⚠️ Maybe UI changed or detection selector needs update.")
        browser.close()


if __name__ == "__main__":
    main()
