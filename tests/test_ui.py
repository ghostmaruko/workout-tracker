from playwright.sync_api import expect
# This test file is for testing the UI of a web application using Playwright. The test checks if the title of the page is "Workout Tracker" when navigating to the specified URL.
test_url = "http://127.0.0.1:5000"

def test_workout_tracker(page):
	page.goto(test_url)
	expect(page).to_have_title("Workout Tracker")

def test_corsa_mostra_allenamenti(page):
	page.request.post(test_url + "/api/workouts", data={"categoria": "corsa", "tipo_corsa": "tempo_run", "distanza_km": 12, "tempo_minuti": 59,})
	page.goto(test_url)
	page.click("#corsa-btn")
	expect(page.locator("#corsa-content")).to_be_visible()
	expect(page.locator("#palestra-content")).to_be_hidden()
	expect(page.locator("#profilo")).to_be_hidden()


def test_palestra_mostra_allenamenti(page):
    page.request.post(test_url + "/api/workouts", data={"categoria": "palestra", "esercizio": "push-up", "serie": 3,
			"ripetizioni": 15, "peso": 0})
    page.goto(test_url)
    page.click("#palestra-btn")
    expect(page.locator("#palestra-content")).to_be_visible()
    expect(page.locator("#corsa-content")).to_be_hidden()
    expect(page.locator("#profilo")).to_be_hidden()

def test_profilo_mostra_profilo(page):
	page.goto(test_url)
	page.click("#profilo-btn")
	expect(page.locator("#profilo")).to_be_visible()
	expect(page.locator("#corsa-content")).to_be_hidden()
	expect(page.locator("#palestra-content")).to_be_hidden()