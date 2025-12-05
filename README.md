# Zen-Ask Backend

这是从 Aletheia 项目中提取的独立后端服务。

## 功能说明

Zen-Ask 是一个基于 FastAPI 的哲学式问答服务，提供直击灵魂的洞察回答。项目包含：

- **智能问答**：基于 OpenRouter 的多模型支持（默认 DeepSeek 免费模型）
- **陈词滥调过滤**：使用 sentence-transformers 模型过滤平庸回答
- **多模型支持**：支持 OpenRouter 平台上的所有模型（DeepSeek、Claude、GPT-4 等）
- **零配置运行**：无 API 密钥时自动使用本地哲学回答

## 快速开始

### 方式一：使用启动脚本（推荐）

```bash
# 直接运行启动脚本
./run.sh
```

启动脚本会：
1. 自动创建 Python 虚拟环境
2. 安装所有依赖包
3. 启动服务（默认端口 8000）

### 方式二：手动启动

```bash
# 1. 创建虚拟环境
python3 -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate

# 3. 安装依赖
pip install -r requirements.txt

# 4. 启动服务
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## 配置

### 环境变量

复制 `.env.example` 为 `.env` 并修改配置：

```bash
cp .env.example .env
```

必需配置项：
- `OPENROUTER_API_KEY`：OpenRouter API 密钥（可选，无密钥时使用本地保底回复）

可选配置项：
- `HTTP_REFERER`：HTTP 引用头（默认：http://localhost:8000）
- `APP_NAME`：应用名称（默认：Zen-Ask）
- `AI_MODEL`：使用的模型（默认：deepseek/deepseek-chat-v3-0324:free）
- `PORT`：服务端口（默认 8000）
- `HOST`：主机地址（默认 0.0.0.0）
- `MODE`：运行模式（默认 compatible）

### 获取 OpenRouter API 密钥

1. 访问 [OpenRouter.ai](https://openrouter.ai)
2. 注册账号并登录
3. 在 Keys 页面创建 API 密钥
4. 将密钥填入 `.env` 文件的 `OPENROUTER_API_KEY` 字段

### 无 API 密钥模式

即使没有配置 OpenRouter API 密钥，服务仍可以运行，此时会使用本地预定义的哲学回复作为保底回答。

### 推荐模型

**免费模型（推荐）：**
- `deepseek/deepseek-chat-v3-0324:free`：最优秀的免费中文模型
- `meta-llama/llama-3.2-3b-instruct:free`：轻量级英文模型

**付费模型：**
- `anthropic/claude-3-haiku`：快速高效
- `openai/gpt-4o-mini`：性价比高
- `anthropic/claude-3-opus`：最强模型

## API 使用

### 发送请求

```bash
curl -X POST "http://localhost:8000/api/ask" \
     -H "Content-Type: application/json" \
     -d '{"text": "人生的意义是什么？"}'
```

### 响应格式

```json
{
  "answer": "洞察性的哲学回答..."
}
```

## 项目结构

```
zen-ask/
├── main.py              # FastAPI 应用入口
├── requirements.txt     # Python 依赖包
├── core/               # 核心模块
│   ├── __init__.py
│   ├── brain.py        # AI 思考模块
│   └── gatekeeper.py   # 陈词滥调过滤器
├── .env.example        # 环境变量模板
├── run.sh             # 启动脚本
└── README.md          # 项目说明
```

## 依赖包

- fastapi：Web 框架
- uvicorn：ASGI 服务器
- pydantic：数据验证
- sentence-transformers：文本相似度模型
- torch：PyTorch 深度学习框架
- openai：OpenAI API 客户端
- python-dotenv：环境变量管理

## 注意事项

1. 首次运行需要下载模型，耗时较长
2. 如果使用 OpenAI API，需要确保网络可以3. 建议在虚拟访问 OpenAI
环境中运行项目
4. 生产环境请移除 `--reload` 参数

## 开发说明

### 修改代码

代码修改后会自动重载（开发模式）。

### 添加新功能

- 在 `main.py` 中添加新的路由
- 在 `core/` 目录中添加新的模块

## 许可证

本项目继承原 Aletheia 项目的许可证。
