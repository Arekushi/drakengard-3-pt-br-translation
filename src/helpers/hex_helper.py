import re


def replace_hex(
    file_path: str,
    search_hex: str,
    replace_hex: str,
    dest_file_path: str = None
):
    with open(file_path, 'rb+') as file:
        content = file.read().hex()
        search_hex = search_hex.replace(' ', '')
        replace_hex = replace_hex.replace(' ', '')
        
        pattern = re.compile(re.escape(search_hex), re.IGNORECASE)
        modified_content = pattern.sub(replace_hex, content)
        
        if modified_content != content:
            modified_bytes = bytes.fromhex(modified_content)
            new_file = file if not dest_file_path else open(dest_file_path, 'wb+')
            new_file.seek(0)
            new_file.write(modified_bytes)
            new_file.truncate()
            new_file.close()


def convert_str_to_hex(
    source_str: str,
    encoding = 'utf-8',
    delimiter = '000000'
) -> str:
    hex_str = source_str.encode(encoding).hex().upper()
    return f'{delimiter.join([hex_str[i:i+2] for i in range(0, len(hex_str), 2)])}{delimiter}'
