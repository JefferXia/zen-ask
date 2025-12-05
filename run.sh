#!/bin/bash

# Zen-Ask Backend 启动脚本

echo "正在启动 Zen-Ask Backend..."

# 检查Python版本
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
echo "检测到Python版本: $python_version"

# 检查是否安装了依赖
if [ ! -d "venv" ]; then
    echo "未检测到虚拟环境，正在创建..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "安装依赖包..."
pip install --upgrade pip --break-system-packages

# 逐步安装依赖，避免错误
echo "安装核心依赖..."
pip install fastapi uvicorn pydantic openai python-dotenv --break-system-packages

echo "尝试安装机器学习依赖..."
pip install sentence-transformers torch --break-system-packages 2>/dev/null || {
    echo "⚠️  警告：无法安装某些机器学习依赖，服务可能功能受限"
    echo "如需完整功能，请手动安装："
    echo "  pip install sentence-transformers torch --break-system-packages"
}

# 加载环境变量
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# 设置默认值
HOST=${HOST:-0.0.0.0}
PORT=${PORT:-8000}

# 启动服务
echo "启动服务在 ${HOST}:${PORT}..."
uvicorn main:app --host ${HOST} --port ${PORT} --reload
