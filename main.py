# References
# https://github.com/facebookresearch/fairseq/tree/nllb
# https://github.com/facebookresearch/flores/blob/main/flores200/README.md
# https://huggingface.co/facebook/nllb-200-1.3B
# https://developer.nvidia.com/blog/training-localized-multilingual-llms-with-nvidia-nemo-part-1/

# Future

# https://huggingface.co/google/madlad400-10b-mt

# Import required libraries
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def translate_text(text, target_lang, checkpoint):
    try:
        # Initialize model and tokenizer
        model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)
        tokenizer = AutoTokenizer.from_pretrained(checkpoint)

        # Create translator pipeline
        translator = pipeline('translation',
                            model=model,
                            tokenizer=tokenizer,
                            src_lang='eng_Latn',  # English (Latin script)
                            tgt_lang=target_lang,
                            max_length=400)

        # Perform translation
        result = translator(text)
        return result[0]['translation_text']
    
    except Exception as e:
        return f"Translation error: {str(e)}"

if __name__ == "__main__":
    # Example usage
    # Choose one of the following checkpoints
    checkpoint = 'facebook/nllb-200-distilled-600M'  # Smaller, faster model
    # checkpoint = 'facebook/nllb-200-1.3B'         # Medium model
    # checkpoint = 'facebook/nllb-200-3.3B'         # Larger, more accurate model
    # checkpoint = 'facebook/nllb-200-distilled-1.3B' # Distilled medium model

    target_lang = 'sin_Sinh'  # Sinhala
    text = 'When everyone had boarded, the ship began its three-hour tour.'
    
    translated_text = translate_text(text, target_lang, checkpoint)
    print(f"\nOriginal text: {text}")
    print(f"Translated text: {translated_text}")