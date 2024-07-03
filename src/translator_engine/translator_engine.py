from abc import ABC
from rich.console import Console

from config import settings


console = Console()


class TranslatorEngine(ABC):
    async def init(self):
        raise NotImplementedError()
    
    async def translate_multiple_files(self, files):
        await self.init()
        
        count_all = len(files)

        for i, file in enumerate(files):
            console.print(
                settings.CLI.TRANSLATOR.translating_file
                    .replace('<file>', str(file))
                    .replace('<i>', str(i + 1))
                    .replace('<count_all>', str(count_all))
            )
            
            await self.translate_single_file(file)

    async def translate_single_file(self, file):
        raise NotImplementedError()
