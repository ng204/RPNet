import matplotlib.pyplot as plt

# 关键点坐标
keypoints = {
    "nose": (147.0, 75.0),
    "Head_top": (139.0, 59.0),
    "Spine": (96.0, 52.0),
    "Left_FTR": (85.0, 85.0),
    "Left_FK": (118.0, 102.0),
    "Left_FH": (128.0, 123.0),
    "Right_FTR": (89.0, 83.0),
    "Right_FK": (85.0, 103.0),
    "Right_FH": (81.0, 124.0),
    "Coccyx": (54.0, 52.0),
    "Left_HTR": (38.0, 60.0),
    "Left_HK": (53.0, 96.0),
    "Left_HH": (60.0, 121.0),
    "Right_HT": (48.0, 79.0),
    "Right_HK": (34.0, 93.0),
    "Right_HH": (24.0, 119.0)
}

# 假设的关键点连接关系
edges = [
    ("Head_top", "nose"),
    ("Head_top", "Spine"),
    ("Spine", "Coccyx"),
    ("Spine", "Left_FTR"),
    ("Left_FTR", "Left_FK"),
    ("Left_FK", "Left_FH"),
    ("Coccyx", "Left_HTR"),
    ("Left_HTR", "Left_HK"),
    ("Left_HK", "Left_HH"),
    ("Spine", "Right_FTR"),
    ("Right_FTR", "Right_FK"),
    ("Right_FK", "Right_FH"),
    ("Coccyx", "Right_HT"),
    ("Right_HT", "Right_HK"),
    ("Right_HK", "Right_HH")
]

# 提取坐标
x_coords = [keypoints[key][0] for key in keypoints]
y_coords = [keypoints[key][1] for key in keypoints]

# 绘制关键点
plt.figure(figsize=(6, 6))
plt.scatter(x_coords, y_coords, c='red')

# 添加关键点标签
for key, (x, y) in keypoints.items():
    plt.text(x, y, key, fontsize=12)

# 绘制连接关系
for edge in edges:
    point1 = keypoints[edge[0]]
    point2 = keypoints[edge[1]]
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'b-', lw=2)

# 设置图形参数
plt.title('Horse Keypoint Visualization and Connections')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.gca().invert_yaxis()  # 反转 y 轴以符合图像坐标系
plt.grid(True)

# 保存图像
plt.savefig('horse_keypoint_visualization.png')
plt.show()
