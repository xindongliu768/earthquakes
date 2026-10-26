import json
import matplotlib.pyplot as plt

# 1. 读取已经下载的数据
with open("earthquake.json", encoding="utf-8") as f:
    data = json.load(f)

# 2. 提取经度、纬度和震级
longitudes = []
latitudes = []
magnitudes = []

for earthquake in data["features"]:
    coordinates = earthquake["geometry"]["coordinates"]

    longitudes.append(coordinates[0])
    latitudes.append(coordinates[1])
    magnitudes.append(earthquake["properties"]["mag"])

# 3. 找出最大震级及其在列表中的位置
max_magnitude = max(magnitudes)
max_index = magnitudes.index(max_magnitude)

# 4. 绘制散点图，颜色表示震级
fig, ax = plt.subplots(figsize=(9, 6))

points = ax.scatter(
    longitudes,
    latitudes,
    c=magnitudes,
    cmap="viridis",
    s=45,
    alpha=0.8,
)

fig.colorbar(points, ax=ax, label="Magnitude")

# 5. 用红色星号标记最强地震
ax.scatter(
    longitudes[max_index],
    latitudes[max_index],
    color="red",
    marker="*",
    s=250,
    edgecolors="black",
    label=f"Strongest earthquake: M {max_magnitude}",
    zorder=3,
)

ax.set_xlabel("Longitude (degrees)")
ax.set_ylabel("Latitude (degrees)")
ax.set_title("Earthquake locations, 2000-01-01 to 2018-10-11")
ax.legend()
ax.grid(alpha=0.3)

# 6. 保存图片并显示
fig.tight_layout()
fig.savefig("earthquake_locations.png", dpi=300)
plt.show()