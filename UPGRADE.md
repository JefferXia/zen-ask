# Zen-Ask OpenRouter 升级指南

## 升级概述

✅ **已完成 OpenRouter 集成并测试通过**

已将 Zen-Ask 后端从 OpenAI 迁移至 OpenRouter，提供更多模型选择和更好的性价比。

## 主要变更

### 1. API 提供商
- **之前**：OpenAI（仅 GPT 系列模型）
- **现在**：OpenRouter（支持 100+ 模型）

### 2. 依赖包
- **无需额外依赖**：OpenRouter 使用标准的 OpenAI 客户端库
- 继续使用：`openai` 库

### 3. 环境变量变更

#### 新增配置：
```bash
OPENROUTER_API_KEY=your_key_here    # OpenRouter API 密钥
HTTP_REFERER=http://localhost:8000  # 引用头（可选）
APP_NAME=Zen-Ask                    # 应用名称（可选）
AI_MODEL=deepseek/deepseek-chat-v3  # 模型选择
```

#### 移除配置：
```bash
# OPENAI_API_KEY（不再使用）
```

### 4. 默认模型
- **新默认模型**：`deepseek/deepseek-chat-v3`
- 优势：高质量中文模型、理解能力强
- 原默认模型：`gpt-4o-mini`

## 代码变更

### brain.py 主要修改：

```python
# 之前
self.client = OpenAI(api_key=api_key)

# 现在
self.client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": http_referer,
        "X-Title": app_name,
    }
)
```

### main.py 添加环境变量加载：

```python
from dotenv import load_dotenv
load_dotenv()
```

## 使用步骤

### 1. 获取 OpenRouter API 密钥
1. 访问 [https://openrouter.ai](https://openrouter.ai)
2. 注册/登录账号
3. 在 Keys 页面创建 API 密钥
4. 将密钥添加到 `.env` 文件

### 2. 配置 `.env` 文件

```bash
# 编辑 .env 文件
OPENROUTER_API_KEY=sk-or-v1-your-key-here
AI_MODEL=deepseek/deepseek-chat-v3
```

### 3. 重启服务

```bash
# 方式一：使用启动脚本
./run.sh

# 方式二：手动重启
source venv/bin/activate
python main.py
```

## 推荐模型

### 🆓 免费模型（推荐）
- `meta-llama/llama-3.2-3b-instruct:free` ⭐
  - 轻量级
  - 快速响应
  - 英文效果好

- `microsoft/wizardlm-2-8x22b:free`
  - 强大的推理能力
  - 多语言支持

### 💰 付费模型
- `deepseek/deepseek-chat-v3` ⭐ 最佳中文模型
- `anthropic/claude-3-haiku` - $0.25/1M tokens
- `openai/gpt-4o-mini` - $0.15/1M tokens
- `anthropic/claude-3-opus` - $15/1M tokens
- `openai/gpt-4o` - $5/1M tokens

## 测试结果

✅ 代码导入正常
✅ FastAPI 应用启动正常
✅ OpenRouter 客户端初始化正常
✅ 环境变量加载正常
✅ API 问答功能正常
✅ 过滤器工作正常
✅ 无 API 密钥时自动降级到本地模式

### 实际测试输出

**示例问题 1：**
```
用户: "什么是真正的自由？"
AI: "笼中鸟歌唱时，笼子就消失了——自由是你忘记镣铐的每一秒。"
```

**示例问题 2：**
```
用户: "为什么努力没有回报？"
AI: "努力是场自欺欺人的哑剧，回报不过是命运随手扔的骨头。"
```

**示例问题 3：**
```
用户: "爱情是什么？"
AI: "爱情是两具相互取暖的骷髅，却以为自己是永恒的火炬。"
```

## 兼容模式

系统支持三种模式：

1. **OpenRouter 模式**：配置 `OPENROUTER_API_KEY`，使用高质量 AI 回答
2. **本地模式**：无 API 密钥，使用本地预定义哲学回答
3. **LoRA 模式**：未来扩展，本地模型模式

## 优势

✅ **成本更低**：可使用免费模型或低成本模型
✅ **选择更多**：100+ 模型可选
✅ **中文优化**：DeepSeek 中文能力出色
✅ **零配置**：无密钥时自动降级到本地模式
✅ **向后兼容**：使用相同 OpenAI 客户端库
✅ **自动加载环境变量**：使用 python-dotenv

## 注意事项

⚠️ **API 密钥**：如果需要 AI 回答，必须配置 `OPENROUTER_API_KEY`
⚠️ **网络**：OpenRouter 需要稳定的网络连接
⚠️ **模型名称**：确保使用有效的模型名称
⚠️ **模型费用**：部分模型需要付费，使用前请查看价格

## 故障排除

### 问题：模型不存在 (404 错误)
```
Error: No endpoints found for model-name
```
**解决**：更新 `.env` 文件中的 `AI_MODEL` 为有效模型名称

### 问题：API 密钥无效
```
Error: Invalid API key
```
**解决**：检查 `.env` 文件中的 `OPENROUTER_API_KEY` 是否正确

### 问题：网络超时
```
Error: Connection timeout
```
**解决**：检查网络连接，或尝试使用更稳定的网络

## 下一步

- [ ] 根据需要切换不同模型
- [ ] 设置 API 使用限制
- [ ] 监控 API 调用成本
- [ ] 集成更多功能

---

🎉 **升级完成！** Zen-Ask 现在支持 OpenRouter 平台的所有模型，并已通过完整测试。
