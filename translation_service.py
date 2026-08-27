import deepl
def translate_joke(joke, target_language):
    DEEPL_API_KEY="3269b51f-770a-40b6-99b1-204f919ac290:fx"
    url="https://api.deepl.com/v2/translate"
    try:
        deepl_client = deepl.DeepLClient(DEEPL_API_KEY)
        result = deepl_client.translate_text(joke,target_lang=target_language)
        return result
    except Exception as e:
        return "The joke was received, but it could not be translated."