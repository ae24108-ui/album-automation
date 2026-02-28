import os
from PIL import Image, ImageOps

#設定
INPUT_FOLDER = r"C:\Users\mentu\OneDrive\画像\アルバム用\アルバム写真"
OUTPUT_FOLDER = r"C:\Users\mentu\OneDrive\画像\アルバム用\processed"

TARGET_RATIO = 3 / 4  # width / height（横:縦）
OUTPUT_SIZE = (1500, 2000)  # 最終リサイズサイズ

#元画像を3:4にリサイズ
def process_image_to_3_4(input_path, output_path):
    img = Image.open(input_path)
    img = ImageOps.exif_transpose(img)

    width, height = img.size
    current_ratio = width / height

    # 横長なら回転
    if width > height:
        img = img.rotate(90, expand=True)
        width, height = img.size
        current_ratio = width / height

    # 比率調整（中央トリミング）
    if current_ratio > TARGET_RATIO:
        new_width = int(height * TARGET_RATIO)
        left = (width - new_width) // 2
        right = left + new_width
        img = img.crop((left, 0, right, height))

    elif current_ratio < TARGET_RATIO:
        new_height = int(width / TARGET_RATIO)
        top = (height - new_height) // 2
        bottom = top + new_height
        img = img.crop((0, top, width, bottom))

    # リサイズ
    img = img.resize(OUTPUT_SIZE, Image.LANCZOS)

    img.save(output_path, quality=95)


def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    for filename in os.listdir(INPUT_FOLDER):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(INPUT_FOLDER, filename)
            output_path = os.path.join(OUTPUT_FOLDER, filename)

            print(f"Processing: {filename}")
            process_image_to_3_4(input_path, output_path)

    print("All images processed.")


if __name__ == "__main__":
    main()