import json

with open("earthquake.json", encoding="utf-8") as f:
    data = json.load(f)

print("顶层字段：", data.keys())
print("地震总数：", data["metadata"]["count"])
print("features 中的条目数：", len(data["features"]))

earthquake = data["features"][0]

print("地点：", earthquake["properties"]["place"])
print("震级：", earthquake["properties"]["mag"])
print("坐标：", earthquake["geometry"]["coordinates"])
print("时间：", earthquake["properties"]["time"])