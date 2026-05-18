from hawk_asset_intelligence import detect_assets

def test_detect_assets():
    c = detect_assets("satellite_image.jpg")
    assert c.result["count"] > 0
    assert c.confidence > 0.9
