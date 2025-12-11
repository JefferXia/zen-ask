class ClicheFilter:
    def __init__(self):
        print("Initializing Gatekeeper (Cliche Filter)...")
        self.use_ai_filter = False
        self.model = None
        self.util = None
        self.cliche_embeddings = None
        self.threshold = 0.60

        self.cliches = [
            "你要相信自己",
            "一切都会好起来的",
            "失败是成功之母",
            "建议你制定一个计划",
            "作为AI语言模型",
            "你要学会爱自己",
            "风雨之后见彩虹",
            "心态最重要",
            "生活不止眼前的苟且",
            "加油，你是最棒的",
            "要辩证地看问题",
        ]

        print("✓ Gatekeeper initialized (keyword-based filter)")

    def is_cliche(self, text: str) -> bool:
        # 基础规则过滤
        # if len(text) > 100: return True
        if "作为AI" in text or "我是AI" in text:
            return True

        # 如果没有AI过滤器，使用简化的关键词匹配
        if not self.use_ai_filter:
            return any(cliche in text for cliche in self.cliches)

        # AI过滤
        try:
            text_embedding = self.model.encode(text, convert_to_tensor=True)
            cosine_scores = self.util.cos_sim(text_embedding, self.cliche_embeddings)
            # 将 torch tensor 转换为 numpy 并计算最大值
            max_score = cosine_scores.numpy().max()
            return max_score > self.threshold
        except Exception:
            # 如果AI过滤出错，使用基础过滤
            return any(cliche in text for cliche in self.cliches)
