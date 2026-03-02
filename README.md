# album-automation
> 画像フォルダからWordアルバムを自動生成するPythonツール

---

## 🚩概要

Wordでアルバムを作る際、写真を１枚１枚手作業で並べるのは効率が悪く、膨大な時間がかかってしまうという課題があります。

本ツールではその工程を自動化・効率化しています。

また、基本的に4:3(縦：横)の画像によるアルバムを想定しているので、それ以外の画像比率の場合image_preprocess.pyの段階で、
4:3(縦：横)に修正されます。

---

## 🎯背景・目的

- **なぜこのプロジェクトを作ったのか**

  友人と一年間の振り返りアルバムを作る際、写真枚数が350枚以上となってしまい、手作業
  では難しい状況になりました。
  そこで現在勉強しているPython,Pythonのライブラリの知識を用いて自動化ツールの開発
  を始めました。

  
- **想定ユーザー**
  
  家族、友人、恋人などの親しい人とアルバムを作る際、写真データが膨大になり、手作業
  でWordに配置することが難しいと悩んでいる人。

  ---

## ⚙️使用技術

- Python 3.13
- python-docx: Wordファイル作成・編集
- Pillow: 画像のリサイズ・回転
- os: ファイル操作・パス管理

---

## ✨主な機能

1. 画像のリサイズ・回転 : image_preprocess.py
2. Wordファイルに画像の貼り付け : album_creation.py

---

## 💻実行方法

1. **リポジトリをクローン**

```bash
git clone https://github.com/ae2418-ui/album-automation.git
cd album-automation
```

---

2. **必要なライブラリをインストール**

```bash
python -m pip install -r requirements.txt
```

---

3. **画像の準備**

- imagesフォルダにアルバムに追加したい画像(jpg/png)を入れる。

---

4. **画像の整形**

- image_preprocess.pyを実行することで、images内の全ての画像を4:3(縦：横)に整形できる。


- 処理された画像は、processed_imagesファイルに格納される。

```bash
python image_preprocess.py
```

---

5. **アルバム作成**

- album_creation.pyを実行することで、album.docxというwordファイルが作成され、写真が配置される。

```bash
python album_creation.py
```

---

6. **出力結果の確認**

- スクリプト実行後、`output/` フォルダに Word ファイル(album.docx)が生成されることを確認します。
- 生成された Word ファイルを開き、写真が正しく配置されているかチェックします。
- 問題がある場合は、画像フォルダ内の写真の形式や名前を確認してください。
   
