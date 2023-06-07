from deep_translator import MyMemoryTranslator

def english_to_french(text):
    return MyMemoryTranslator(source="english", target="french").translate(text)

def french_to_english(text):
    return MyMemoryTranslator(source="french", target="english").translate(text)
