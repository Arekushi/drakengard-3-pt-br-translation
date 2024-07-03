import re
from g4f.client import AsyncClient, Client
from g4f.local import LocalClient
from g4f.Provider import ChatgptAi, Aichatos, You, Bing, Blackbox, RetryProvider

from src.chat_gpt.llm_model_wrapper import LLMModelWrapper
from config import settings


class G4FWrapper(LLMModelWrapper):
    def __init__(self):
        self.client = AsyncClient(
            provider=Blackbox
        )
        super().__init__()

    async def _send_message(self, message):
        completion = await self.client.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=[
                {
                    'role': 'user',
                    'content': re.sub(r'\s+', ' ', message)
                }
            ]
        )

        return completion.choices[0].message.content
