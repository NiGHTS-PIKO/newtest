#!/bin/bash

# 変更ファイルの確認
git status

# ステージング
git add .

# コミット（引数がない場合はデフォルトメッセージ）
if [ -z "$1" ]; then
    git commit -m "Auto commit from script"
else
    git commit -m "$1"
fi

# プッシュ
git push
