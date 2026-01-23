from urllib.parse import quote_plus

def fetch_image_url(keyword: str) -> str:
    """
    Returns a reliable placeholder image with the keyword rendered as text.
    This avoids external image failures and improves readability for dyslexic learners.
    """
    text = quote_plus(keyword.capitalize())
    return f"https://placehold.co/600x400/1e1e1e/ffffff?text={text}"
