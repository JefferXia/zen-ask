# Zen-Ask 快速部署指南

## 项目概述

Zen-Ask 是从 Aletheia 项目中提取的独立后端服务，提供哲学式问答功能。

## 已完成设置

✅ 项目结构创建完成
✅ 所有源代码文件已复制
✅ 虚拟环境已初始化 (`venv/`)
✅ 核心依赖已安装（FastAPI、Uvicorn、Pydantic、OpenAI、Python-dotenv）
✅ 启动脚本已创建并可执行
✅ 环境变量配置文件已创建
✅ README文档已编写
✅ 服务测试通过

## 文件结构

```
zen-ask/
├── main.py              # FastAPI应用入口（含根路由、健康检查、问答API）
├── requirements.txt     # 依赖包列表
├── core/               # 核心模块目录
│   ├── __init__.py
│   ├── brain.py        # AI大脑模块（OpenAI集成）
│   └── gatekeeper.py   # 过滤器（AI模式/关键词模式自动切换）
├── .env                # 环境变量配置
├── .env.example        # 环境变量模板
├── run.sh             # 启动脚本（自动创建venv、安装依赖、启动服务）
├── README.md          # 详细说明文档
├── SETUP.md           # 本文件
└── venv/              # Python虚拟环境（已创建）
```

## 快速启动

### 方法一：使用启动脚本（推荐）

```bash
cd zen-ask
./run.sh
```

### 方法二：手动启动

```bash
cd zen-ask
source venv/bin/activate
python main.py
```

## 测试结果

✅ 服务成功启动在 http://0.0.0.0:8000
✅ 根路径响应正常：GET /
✅ 健康检查响应正常：GET /health
✅ 问答API响应正常：POST /api/ask

**示例测试：**

```bash
curl -X POST "http://localhost:8000/api/ask" \
     -H "Content-Type: application/json" \
     -d '{"text": "人生的意义是什么？"}'
```

返回示例：
```json
{"answer":"未经审视的人生是不值得过的。"}
```

## 可选配置

### 配置 OpenAI API

1. 复制环境变量模板：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件：
```bash
OPENAI_API_KEY=your_api_key_here
```

3. 重启服务

### 完整安装机器学习依赖（可选）

如需启用AI过滤器功能：

```bash
source venv/bin/activate
pip install sentence-transformers torch --break-system-packages
```

## 技术特点

- ✅ 依赖智能降级：缺少ML库时自动切换到关键词过滤模式
- ✅ 无API密钥模式：未配置OpenAI时使用本地哲学回答
- ✅ 自动化脚本：一键创建环境、安装依赖、启动服务
- ✅ 健康检查：内置根路径和健康检查端点
- ✅ 跨域支持：默认允许所有来源的CORS请求

## 下一步

项目已准备就绪，可以：
1. 直接运行使用（已测试通过）
2. 配置OpenAI API密钥获得更好的回答质量
3. 集成到前端应用
4. 部署到生产环境

## 故障排除

**问题：端口被占用**
- 修改 `.env` 文件中的 `PORT` 值
- 或杀死占用8000端口的进程

**问题：依赖安装失败**
- 确保使用 `--break-system-packages` 标志
- 或使用管理员权限安装

**问题：服务无法启动**
- 检查Python版本（推荐3.8+）
- 检查虚拟环境是否激活：`source venv/bin/activate`
- 查看详细错误信息

---

🎉 项目提取完成！所有功能正常运行。
