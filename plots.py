
import json
from datetime import datetime, timezone

import matplotlib.pyplot as plt

# 1. 读取 JSON 数据
with open("earthquakes.json", "r") as f:
    data = json.load(f)

# 2. 按年份统计地震数量、震级总和
counts = {}
magnitude_sums = {}
magnitude_counts = {}

for earthquake in data["features"]:
    # USGS 时间戳单位为毫秒
    timestamp = earthquake["properties"]["time"]
    year = datetime.fromtimestamp(
        timestamp / 1000, tz=timezone.utc
    ).year

    magnitude = earthquake["properties"]["mag"]

    # 统计每年的地震次数
    counts[year] = counts.get(year, 0) + 1

    # 统计每年有效震级的总和与数量
    if magnitude is not None:
        magnitude_sums[year] = magnitude_sums.get(year, 0) + magnitude
        magnitude_counts[year] = magnitude_counts.get(year, 0) + 1

# 3. 准备绘图数据
years = sorted(counts)
numbers = [counts[year] for year in years]

avg_years = sorted(magnitude_counts)
averages = [
    magnitude_sums[year] / magnitude_counts[year]
    for year in avg_years
]

# 4. 第一张图：每年地震数量
plt.figure(figsize=(10, 5))
plt.bar(years, numbers)

plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.title("Number of Earthquakes per Year")
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.savefig("earthquake_counts.png", dpi=300)
plt.show()

# 5. 第二张图：每年平均震级
plt.figure(figsize=(10, 5))
plt.plot(avg_years, averages, marker="o")

plt.xlabel("Year")
plt.ylabel("Average Magnitude")
plt.title("Average Earthquake Magnitude per Year")
plt.xticks(avg_years, rotation=45)
plt.tight_layout()

plt.savefig("earthquake_magnitude.png", dpi=300)
plt.show()
