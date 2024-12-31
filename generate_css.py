import os

# 配置参数
GITHUB_USERNAME = "ZicongCheung"  # 替换为你的 GitHub 用户名
REPO_NAME = "ZicCDN"  # 替换为你的 GitHub 仓库名
FONT_NAME = "HarmonyOS_Sans/HarmonyOS_Sans_SC"  # 替换为你的字体名
CDN_BASE_URL = f"https://jsd.cdn.zzko.cn/gh/{GITHUB_USERNAME}/{REPO_NAME}@latest/fonts/{FONT_NAME}/"

# 定义字体族名
FONT_FAMILY = "HarmonyOS_Sans_SC"

# 要生成的 CSS 文件名
CSS_FILENAME = "result.css"


def generate_css(font_folder):
    font_files = {}  # 用于存储每个 font-weight 对应的 .woff 和 .woff2 文件
    css_lines = []

    # 遍历字体文件夹
    for file_name in os.listdir(font_folder):
        if file_name.endswith(".woff") or file_name.endswith(".woff2"):
            font_weight = extract_font_weight(file_name)

            # 初始化字典
            if font_weight not in font_files:
                font_files[font_weight] = {"woff": None, "woff2": None}

            # 根据文件类型存储路径
            if file_name.endswith(".woff2"):
                font_files[font_weight]["woff2"] = file_name
            elif file_name.endswith(".woff"):
                font_files[font_weight]["woff"] = file_name

    # 生成 CSS 内容
    for font_weight, files in font_files.items():
        woff2_url = CDN_BASE_URL + files["woff2"] if files["woff2"] else None
        woff_url = CDN_BASE_URL + files["woff"] if files["woff"] else None

        css_lines.append("@font-face {")
        css_lines.append(f"    font-family: '{FONT_FAMILY}';")
        css_lines.append(f"    font-weight: {font_weight};")
        css_lines.append(f"    font-style: normal;")

        # 构建 src
        src_parts = []
        if woff2_url:
            src_parts.append(f"url('{woff2_url}') format('woff2')")
        if woff_url:
            src_parts.append(f"url('{woff_url}') format('woff')")
        css_lines.append(f"    src: {', '.join(src_parts)};")
        css_lines.append("}\n")

    # 写入 CSS 文件
    with open(CSS_FILENAME, "w", encoding="utf-8") as css_file:
        css_file.writelines("\n".join(css_lines))
    print(f"CSS 文件已生成：{CSS_FILENAME}")


def extract_font_weight(file_name):
    """根据文件名提取字体粗细（可自定义扩展）"""
    if "Thin" in file_name:
        return 100
    elif "Light" in file_name:
        return 300
    elif "Regular" in file_name:
        return 400
    elif "Medium" in file_name:
        return 500
    elif "SemiBold" in file_name:
        return 600
    elif "Bold" in file_name:
        return 700
    elif "ExtraBold" in file_name:
        return 800
    elif "Heavy" in file_name:
        return 900
    elif "Black" in file_name:
        return 950
    return 400  # 默认权重


# 执行生成
if __name__ == "__main__":
    FONT_FOLDER = "E:/GitHub/ZicCDN/fonts/HarmonyOS_Sans/HarmonyOS_Sans_SC"  # 替换为存放字体文件的文件夹路径
    if os.path.exists(FONT_FOLDER):
        generate_css(FONT_FOLDER)
    else:
        print(f"错误：文件夹 {FONT_FOLDER} 不存在！")