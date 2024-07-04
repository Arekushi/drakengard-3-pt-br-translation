import re
from abc import ABC
from rich.console import Console
from config.config import settings
from src.exceptions import EmptyMessageError


console = Console()


class LLMModelWrapper(ABC):
    async def init(self, reset=False):
        if reset:
            self.reset()
        
        await self.send_message(self.get_initial_message())

    def reset(self):
        raise NotImplementedError()
    
    async def _send_message(self, message):
        raise NotImplementedError()

    async def send_message(
        self,
        message: str,
        max_attempts: int = 5,
        do_print: bool = True
    ):
        attempts = 0
        
        while attempts < max_attempts:
            try:
                response = await self._send_message(message)
                
                if do_print:
                    console.print(f'\n[bold white on blue]CHATGPT:[/] {response}\n')
                
                return response
            except (EmptyMessageError, TimeoutError, ConnectionError) as e:
                attempts += 1
                
                console.print(e)
                console.print(
                    settings.CLI.TRANSLATE.repeted.replace('<i>', str(attempts))
                )
                
                await self.init(True)
                continue
        
        console.print(settings.CLI.TRANSLATE.null_return)
        raise EmptyMessageError()

    @staticmethod
    def get_initial_message():
        request_text = re.sub(r'\s+', ' ', settings.CHATGPT.request_text).strip()
        rules = [re.sub(r'\s+', ' ', rule).strip() for rule in settings.CHATGPT.rules]
        rules = '\n'.join('{}. {}'.format(*rule) for rule in enumerate(rules))
        request_text = request_text.replace('<rules>', f'\n{rules}\n')

        return request_text
