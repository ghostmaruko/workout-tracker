def test_get_workouts_restituisce_lista(client):
    response = client.get("/api/workouts")

    assert response.status_code == 200
    assert isinstance(response.get_json(), list)


def test_aggiungi_workout_corsa_valido(client):
    payload = {
        "categoria": "corsa",
        "tipo_corsa": "tempo_run",
        "distanza_km": 12,
        "tempo_minuti": 59,
        "frequenza_cardiaca_media": 145,
        "data": "2026-08-19"
    }

    response = client.post("/api/workouts", json=payload)
    body = response.get_json()

    assert response.status_code == 201
    assert body["categoria"] == "corsa"
    assert body["passo_min_per_km"] == 4.92


def test_aggiungi_workout_corsa_campo_mancante(client):
    payload = {
        "categoria": "corsa",
        "tipo_corsa": "recupero",
        "tempo_minuti": 30
    }

    response = client.post("/api/workouts", json=payload)

    assert response.status_code == 400
    assert "distanza_km" in response.get_json()["errore"]


def test_aggiungi_workout_categoria_non_valida(client):
    payload = {
        "categoria": "nuoto",
        "data": "2026-08-22"
    }

    response = client.post("/api/workouts", json=payload)

    assert response.status_code == 400