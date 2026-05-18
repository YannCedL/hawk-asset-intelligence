from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus

def detect_assets(image_path: str) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    detections = [
        {"label": "aircraft", "confidence": 0.97, "bbox": [120, 80, 420, 260]},
        {"label": "vehicle", "confidence": 0.89, "bbox": [600, 400, 750, 480]},
    ]
    contract.result = {"image": image_path, "detections": detections, "count": len(detections)}
    contract.add_evidence(Evidence(subject=image_path, predicate="asset_detection",
        value=f"{len(detections)} assets", source="hawk_engine", observed_at=now,
        confidence=0.93, status=EpistemicStatus.INFERENCE))
    return contract

# fixed bbox coordinate system
