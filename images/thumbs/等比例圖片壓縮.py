# -*- coding: utf-8 -*-
"""
圖片壓縮程式
壓縮圖片為寬 500 × 等比高度，轉存為 JPG
"""
"""
安裝套件
pip install pillow
"""
import os
from PIL import Image

# 輸入圖片資料夾
input_dir = r"C:\Users\lzhie\Desktop\圖片"
# 輸出圖片資料夾
output_dir = r"C:\Users\lzhie\Desktop\壓縮圖片"

# 固定寬度(500 × 等比高度)
target_width = 500

os.makedirs(output_dir, exist_ok=True)

# 支援的圖片副檔名
image_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.webp')

for filename in os.listdir(input_dir):
    if filename.lower().endswith(image_extensions):
        input_path = os.path.join(input_dir, filename)
        # 強制輸出為 .jpg 檔案，用原始檔名（去掉副檔名）加 .jpg
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(output_dir, base_name + ".jpg")

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")
                orig_w, orig_h = img.size
                new_height = int(orig_h * (target_width / orig_w))

                resized_img = img.resize((target_width, new_height), Image.Resampling.LANCZOS)
                resized_img.save(output_path, format="JPEG", quality=85)

                print(f"✅ {filename} → {output_path}（{target_width}x{new_height}）")

        except Exception as e:
            print(f"❌ 無法處理 {filename}：{e}")

