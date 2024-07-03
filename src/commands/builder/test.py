import asyncio
from src.chat_gpt.g4f_wrapper import G4FWrapper
from src.helpers.pandas_helper import read_csv_file
from src.translator_engine.chat_gpt_translator import ChatGPTTranslator


def test():
    
    translator = ChatGPTTranslator(G4FWrapper())
    asyncio.run(translator.translate_single_file('.\\texts\\translation\\Ability_Name.csv'))
    # print(read_csv_file('./texts/translation/Ability.csv'))
    # gpt = G4FBot()
    # asyncio.run(gpt.init())
    # response = asyncio.run(gpt.send_message(message='''
                                            
    #                                             Então traduza essas frases, OBEDECENDO o contexto que lhe informei e as REGRAS também.
    # (Não se esqueça de sempre manter a sua resposta dentro de um BLOCO DE CÓDIGO em Python)
    # (Lembre-se de manter a MESMA QUANTIDADE de frases que eu mandar, se eu te enviei 30, me responda com 30)
    # (Strings que estiverem em BRANCO, VAZIAS "" ou " " é para deixar assim, NÃO MUDE isso!)
    # (Mantenha o índice dentro da sublista, por exemplo [1, 'Uma frase qualquer'], para cada item da lista)
    # (Não precisa colocar as frases originais, só responda com as traduções dentro de uma lista em Python, por favor):

    # ```python
    # [0, "Defeat the monster now, bastard"]
    # ```
                                            
    #                                         ''', do_print=False))
    # print(response)
    
    # client = Client()
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": "Hello"}]
    # )
    # print(response.choices[0].message.content)
