LABELS = ['car', 'truck', 'aircraft', 'vessel']

def label_asset(l): return l if l in LABELS else 'unknown'
