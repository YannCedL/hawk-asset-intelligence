# API FastAPI pour le moteur Hawk Asset Intelligence
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .detector import detect_assets

app = FastAPI(
    title="Hawk Asset Intelligence API",
    description="Moteur de Détection & Inventaire d'Actifs Physiques",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil de detection d'actifs
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Hawk API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Hawk", "version": "1.0.0"}

@app.get("/api/v1/detect", response_model=ResultContract)
def get_detect(image_path: str = Query("vue_aerienne_site.jpg")):
    return detect_assets(image_path)
