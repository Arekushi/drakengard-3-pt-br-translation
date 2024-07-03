import pandas as pd
from rich.console import Console

from config import settings, ROOT_DIR
from src.exceptions.empty_message_exception import EmptyMessageError
from src.helpers.path_helper import update_dir
from src.helpers.pandas_helper import read_csv_file, save_df_csv
from src.helpers.list_helper import group_phrases
from src.helpers.string_helper import get_list_from_response
from src.chat_gpt.llm_model_wrapper import LLMModelWrapper
from src.translator_engine import TranslatorEngine


max_characters_phrases = settings.CHATGPT.max_characters_phrases
translate_text_request = settings.CHATGPT.translate_text_request


console = Console()


class ChatGPTTranslator(TranslatorEngine):
    def __init__(self, wrapper: LLMModelWrapper):
        super().__init__()
        self.wrapper = wrapper

    async def init(self):
        await self.wrapper.init()

    async def translate_single_file(self, file_path):
        df = read_csv_file(file_path)
        grouped_phrases_list = list(group_phrases(df['translation'].to_list(), max_characters_phrases))
        translation_column = []
        
        for _, grouped_phrases in enumerate(grouped_phrases_list):
            translated_phrases = await self.send_message_to_translate(grouped_phrases)
            translation_column.extend([phrase[1] for phrase in translated_phrases])
            df_temp = df.assign(translation=translation_column)
            save_df_csv(df_temp, update_dir(file_path, f'{ROOT_DIR}\\temp'))
        
        df = df.assign(translation=translation_column)
        save_df_csv(df, file_path)

    async def send_message_to_translate(self, grouped_phrases: list[str]) -> list[str]:
        message_to_send = translate_text_request.replace('<phrases>', str(grouped_phrases))
        attempts = 0
        max_attempts = 5
        
        while attempts < max_attempts:
            try:
                message_response = await self.wrapper.send_message(message_to_send)
                translated_phrases = get_list_from_response(message_response)
                
                if (len(translated_phrases) != len(grouped_phrases)):
                    console.print(settings.CLI.TRANSLATOR.wrong_response)
                    attempts += 1
                    continue
                
                return translated_phrases

            except (Exception):
                return grouped_phrases
        
        return grouped_phrases
