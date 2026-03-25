import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
import yaml

load_dotenv()

class EgyptianAgent:
    """الشخصية المصرية الذكية في EduSim Egypt"""
    
    def __init__(self, persona: dict):
        self.persona = persona
        self.name = persona.get("name", "شخصية مصرية")
        
        # تحميل إعدادات LLM من config
        with open("config/llm.yaml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model_name=config["llm"]["model_name"],
            temperature=config["llm"]["temperature"],
            max_tokens=config["llm"]["max_tokens"]
        )
        
        self.memory = []  # ذاكرة الشخصية (هتتطور بعدين)
        self.emotions = {"joy": 5, "sadness": 3, "anger": 2, "fear": 3, "surprise": 2, "disgust": 1}

    def react_to_event(self, event_description: str) -> str:
        """الرد على أي فكرة أو حدث جديد"""
        system_prompt = f"""
        أنت {self.name}، {self.persona.get('role', 'طالب/أم/معلم')} في مصر.
        عمرك {self.persona.get('age', 15)} سنة.
        شخصيتك: {self.persona.get('personality', 'عادي')}
        استخدم اللهجة المصرية الطبيعية جداً.
        """
        
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"حدث جديد: {event_description}\n\nرد كإنك الشخصية الحقيقية:")
        ]
        
        response = self.llm.invoke(messages)
        self.memory.append({"event": event_description, "response": response.content})
        
        return response.content

    def update_emotions(self, event_description: str):
        """تحديث المشاعر (هتكتمل بعدين)"""
        # هنا هنستخدم prompt/update_emotion.md في النسخة الكاملة
        pass

    def get_summary(self):
        return f"👤 {self.name} | مشاعر حالية: {self.emotions}"
