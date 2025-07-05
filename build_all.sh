#!/bin/bash

# 设置项目路径
SRC_DIR="source/NXP iMX8MP"
OUT_DIR="docs/NXP-iMX8MP"

# 启用错误中止
set -e

# 清理旧构建
echo "🧹 清理旧的构建目录: $OUT_DIR"
rm -rf "$OUT_DIR"
mkdir -p "$(dirname "$OUT_DIR")"

# 构建文档
echo "🔨 正在构建文档..."
sphinx-build -b html "$SRC_DIR" "$OUT_DIR"

echo "✅ 构建完成，HTML 文件位于 $OUT_DIR"


