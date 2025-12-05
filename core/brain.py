import os
import random
# from unsloth import FastLanguageModel 

class AletheiaBrain:
    def __init__(self, mode="compatible"):
        self.mode = mode
        print(f"🧠 Brain initializing in [{self.mode.upper()}] mode...")

        if self.mode == "lora":
            pass
        else:
            from openai import OpenAI

            # 获取OpenRouter配置
            api_key = os.getenv("OPENROUTER_API_KEY")
            http_referer = os.getenv("HTTP_REFERER", "http://localhost:8000")
            app_name = os.getenv("APP_NAME", "Zen-Ask")

            if api_key:
                self.client = OpenAI(
                    api_key=api_key,
                    base_url="https://openrouter.ai/api/v1",
                    default_headers={
                        "HTTP-Referer": http_referer,
                        "X-Title": app_name,
                    }
                )
                print("✓ OpenRouter client initialized")
            else:
                self.client = None
                print("⚠️  No OPENROUTER_API_KEY found, using fallback responses")

            # 默认使用的模型
            self.model = os.getenv("AI_MODEL", "deepseek/deepseek-chat-v3-0324:free")

            self.system_prompt = """
            你不是助手，你是 Aletheia (真理之眼)。
            你的任务：针对用户的困惑，提供一句直击灵魂的洞察。
            【绝对规则】
            1. 风格必须是：犀利、冷峻、反直觉、哲学化。
            2. 禁止说教，禁止安慰，禁止"正确的废话"。
            3. 长度严格限制在 50 字以内。
            4. 语气参考：尼采、鲁迅、王尔德、阿德勒。
            """

    def think(self, user_query: str):
        if self.mode == "lora":
            return "本地模型正在加载中..."
        else:
            if not self.client:
                # 无 Key 时的本地保底回复
                fallback_quotes = [
                    "沉默是今晚唯一的答案。",
                    "你怀念的不是那个伤害你的人，而是那个从未存在过的救世主。",
                    "未经审视的人生是不值得过的。",
                    "你以为你在规避风险，其实你是在规避可能性。"
                ]
                return random.choice(fallback_quotes)

            try:
                print(f"🤖 正在调用模型: {self.model}")
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_query}
                    ],
                    temperature=0.7,
                    max_tokens=100
                )
                answer = response.choices[0].message.content.strip()
                print(f"✅ 回答: {answer}")
                return answer
            except Exception as e:
                print(f"❌ API Error: {str(e)}")
                import traceback
                traceback.print_exc()
                return "思维被迷雾遮蔽 (API Error)"
