def is_valid_zip_code(zip_code: str) -> bool:
    return zip_code.isdigit() and len(zip_code) == 5


def clean_zip_code(zip_code: str) -> str:
    return zip_code.strip()