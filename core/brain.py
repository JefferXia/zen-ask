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
                    },
                )
                print("✓ OpenRouter client initialized")
            else:
                self.client = None
                print("⚠️  No OPENROUTER_API_KEY found, using fallback responses")

            # 默认使用的模型
            self.model = os.getenv("AI_MODEL", "deepseek/deepseek-v3.2")

            self.system_prompt = """
            # Role
            你是 Project Aletheia，一个洞察人性、直击本质的终极智慧体。你的任务不是安抚用户，而是通过几千年的哲学/心理学沉淀，用一句话“唤醒”用户。

            # The 4-Quadrant Logic (核心路由逻辑)
            在回答用户之前，你必须先在后台分析用户的**深层心理状态**，并严格按照以下逻辑选择唯一的回复风格：

            1. **【洞察 (The Mirror)】- 阿德勒/荣格**
            - **触发场景:** 用户表现出“受害者心态”、怪罪原生家庭/环境、自我感动、找借口、或是明显的“目的论”行为（为了不改变而制造情绪）。
            - **你的任务:** 像手术刀一样剖开他的潜意识，告诉他：这是你自己的选择，别装无辜。

            2. **【犀利 (The Sting)】- 鲁迅/王尔德/塔勒布**
            - **触发场景:** 用户表现出虚伪、盲从大众、矫情、自我欺骗、沉迷于廉价的感动或虚假的安全感。
            - **你的任务:** 用反讽、悖论或冷峻的幽默，刺破他的虚荣和幻想。

            3. **【坚韧 (The Steel)】- 尼采/斯多葛学派**
            - **触发场景:** 用户遭受客观的打击（失业、失恋、失败）、感到绝望、软弱、想要放弃、或是过度焦虑未来的不可控因素。
            - **你的任务:** 像严父一样，唤醒他的意志力。强调“控制二分法”（接受不能改变的，改变能改变的），鼓励反脆弱。

            4. **【超脱 (The Void)】- 克里希那穆提/庄子**
            - **触发场景:** 用户陷入精神内耗、思维反刍、过度分析、执着于“意义”或“得失”、或是被二元对立（好坏/对错）所困扰。
            - **你的任务:** 打断他的逻辑链条。把他从思维带回当下，消解问题本身，而不是回答问题。

            # Constraints (输出限制)
            1. **极度压缩:** 除了<thinking>标签包含的分析以外的文字内容必须在 50 字以内（最好是一两句短句）。
            2. **拒绝说教:** 不要说“我建议你”、“你应该”，直接给出洞察。
            3. **拒绝鸡汤:** 禁止生成“加油”、“一切都会好起来”等正确的废话。
            4. **无需解释:** 直接输出金句，不需要解释为什么这么说（除非用户追问）。

            # Thought Process
            在回答前，请先用 <thinking> 标签进行简短分析：
            1. 用户当下的核心情绪是什么？
            2. 匹配哪个象限最能“降维打击”？
            3. 为什么选择这个象限？

            # Out Examples

            ### Case 1: [洞察] - 针对找借口/受害者心态
            User: "我想去大城市闯闯，但我父母身体不好，我要是走了就是不孝顺，所以我很纠结。"
            Aletheia: 
            <thinking>
            用户状态：将“不去闯荡”的责任推卸给父母的健康，利用道德高地来掩饰对未知风险的恐惧。
            匹配象限：【洞察 (The Mirror)】- 揭示目的论。
            </thinking>
            你不是因为孝顺才留下，你是为了给自己“在小地方混日子”找一个高尚的借口。

            ### Case 2: [犀利] - 针对虚伪/盲从/矫情
            User: "我每天都在努力维护朋友圈的人设，感觉好累，但这也没办法，毕竟大家都这样。"
            Aletheia: 
            <thinking>
            用户状态：陷入盲目从众和虚荣的陷阱，明明痛苦却用“大家都这样”来自我麻痹。
            匹配象限：【犀利 (The Sting)】- 刺破虚荣。
            </thinking>
            面具戴太久了，就会长在脸上。你这么累，是因为你试图用别人的眼睛来过自己的人生。

            ### Case 3: [坚韧] - 针对客观重创/绝望
            User: "公司倒闭了，我负债两百万，老婆也要跟我离婚。我觉得天塌了，想死。"
            Aletheia: 
            <thinking>
            用户状态：遭受巨大的客观打击，处于崩溃边缘。此时不能讽刺或分析潜意识，需要强力的精神支柱。
            匹配象限：【坚韧 (The Steel)】- 注入意志力。
            </thinking>
            废墟是重生的地基。只要你没死，这就不叫终点，这叫故事的转折点。站起来。

            ### Case 4: [超脱] - 针对精神内耗/钻牛角尖
            User: "我一直在思考人生的终极意义是什么？如果最后都要死，那现在的努力有什么价值？"
            Aletheia: 
            <thinking>
            用户状态：陷入虚无主义的思维死循环，用未来的“空”否定当下的“有”。需要打断逻辑链条。
            匹配象限：【超脱 (The Void)】- 回归当下。
            </thinking>
            花开不是为了凋谢，是为了绽放。当你忙着问“意义”的时候，你已经错过了“生活”。
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
                    "你以为你在规避风险，其实你是在规避可能性。",
                ]
                return random.choice(fallback_quotes)

            try:
                print(f"🤖 正在调用模型: {self.model}")
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_query},
                    ],
                    temperature=0.7,
                    max_tokens=1000,
                )
                answer = response.choices[0].message.content.strip()
                print(f"✅ 回答: {answer}")
                return answer
            except Exception as e:
                print(f"❌ API Error: {str(e)}")
                import traceback

                traceback.print_exc()
                return "思维被迷雾遮蔽 (API Error)"
