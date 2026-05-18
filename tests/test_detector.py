# test du moteur de détection d'actifs Hawk
from hawk_asset_intelligence.detector import detect_assets

def test_detect_assets():
    contract = detect_assets("vue_aerienne_site.jpg")
    assert contract is not None
    assert len(contract.result["detections"]) >= 1
    assert contract.result["total_estimated_value_eur"] > 0
    assert len(contract.evidence) >= 1
