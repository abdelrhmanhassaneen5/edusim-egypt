import os
import yaml
from datetime import datetime
from agents.egyptian_agent import EgyptianAgent

class EgyptEducationEnvironment:
    """البيئة التعليمية المصرية الكاملة في EduSim Egypt"""
    
    def __init__(self, num_agents: int = 500):
        self.agents = []
        self.day = 1
        self.current_event = None
        
        # تحميل إعدادات
        with open("config/llm.yaml", "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)
        
        print(f"✅ تم إنشاء بيئة تعليمية مصرية تحتوي على {num_agents} شخصية")

    def create_sample_agents(self):
        """إنشاء عينة من الشخصيات المصرية (للـdemo)"""
        sample_personas = [
            {"name": "أحمد محمد", "role": "طالب ثانوي", "age": 17, "school": "ثانوية الإسكندرية الحكومية", "personality": "مجتهد وقلقان من الثانوية العامة"},
            {"name": "أم أحمد", "role": "أم", "age": 42, "school": "أم طالب ثانوي", "personality": "خايفة جداً على مستقبل ولادها"},
            {"name": "الأستاذ خالد", "role": "معلم", "age": 35, "school": "ثانوية الإسكندرية الحكومية", "personality": "متعب من النظام الحالي"},
        ]
        
        for persona in sample_personas:
            agent = EgyptianAgent(persona)
            self.agents.append(agent)
        
        print(f"✅ تم إنشاء {len(self.agents)} شخصية مصرية جاهزة للمحاكاة")

    def inject_event(self, event_description: str):
        """حقن فكرة جديدة في المجتمع"""
        self.current_event = event_description
        print(f"\n🚨 حدث جديد تم حقنه: {event_description}\n")
        
        reactions = []
        for agent in self.agents:
            reaction = agent.react_to_event(event_description)
            reactions.append({"name": agent.name, "reaction": reaction})
        
        return reactions

    def run_one_day(self):
        """تشغيل يوم واحد في المحاكاة"""
        print(f"\n📅 يوم {self.day} في المحاكاة...")
        self.day += 1
        # هنا هتضاف التفاعلات اليومية في النسخة الكاملة
        return "تم تشغيل اليوم بنجاح"
