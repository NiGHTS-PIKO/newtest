#!/bin/bash

# 変更ファイルの確認
git status

# ステージング
if [ -z "$1" ]; then
    git add .
else
    git add "$1"
fi

# コミット（引数がない場合はデフォルトメッセージ）
if [ -z "$2" ]; then
    git commit -m "Auto commit from script"
else
    git commit -m "$2"
fi

# プッシュ
git push
