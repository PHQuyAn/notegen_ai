from huggingface_hub import InferenceClient
from autocorrect import Speller

def checkNumber_of_Spelling(content):
   spell = Speller(lang='en')
   words = content.split()

   num_errors = 0
   for word in words:
      if spell(word) != word:
         num_errors += 1
         #print(f"Found error: {word}. Corrected to: {spell(word)}")

   return num_errors

def show_spells_error(content):
   spell = Speller(lang='en')
   words = content.split()

   result = ""
   for word in words:
      if spell(word) != word:
         result += f"Found error: {word}. Corrected to: {spell(word)}\n" + " \n"
         # print(f"Found error: {word}. Corrected to: {spell(word)}")

   return result


def fix_Spelling(content):
   spell = Speller(lang='en')
   text_correct = spell(content)

   return text_correct

def summarize_note(content):
   client = InferenceClient(api_key="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")

   inputs = f"""Summarize this note:
   {content}
   """

   result = ""

   # Gọi API và lưu kết quả vào biến result
   for message in client.chat_completion(
           model="microsoft/Phi-3.5-mini-instruct",
           messages=[{"role": "user", "content": inputs}],
           max_tokens=500,
           stream=True,
   ):
      result += message.choices[0].delta.content

   return result.strip()

def outline_note(content):
   client = InferenceClient(api_key="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")

   inputs = f"""Outline to enhance this note:
   {content}
   """

   result = ""

   # Gọi API và lưu kết quả vào biến result
   for message in client.chat_completion(
           model="microsoft/Phi-3.5-mini-instruct",
           messages=[{"role": "user", "content": inputs}],
           max_tokens=500,
           stream=True,
   ):
      result += message.choices[0].delta.content

   return result.strip()

def prompt_enhance_note(prompt,content):
   client = InferenceClient(api_key="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")

   inputs = f"""{prompt}:
   {content}
   """

   result = ""

   # Gọi API và lưu kết quả vào biến result
   for message in client.chat_completion(
           model="microsoft/Phi-3.5-mini-instruct",
           messages=[{"role": "user", "content": inputs}],
           max_tokens=600,
           stream=True,
   ):
      result += message.choices[0].delta.content

   return result.strip()



def read_note_file(file_path):
   # Mở và đọc file
   with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read()
   return content

def main():

   # Read note
   file = "note.txt"
   content = read_note_file(file)


   # Check Spelling by autocorrect
   num_of_spell = checkNumber_of_Spelling(content)
   print("Number of spell errors",num_of_spell)

   content_spellCorrect = fix_Spelling(content)
   print(content_spellCorrect)

   # Summarize note
   print()
   print()
   print("III. Summary:")
   content_summary = summarize_note(content_spellCorrect)
   print(content_summary)


   # Outline note
   print()
   print()
   print("IV. Outline note:")
   content_outline = outline_note(content_spellCorrect)
   print(content_outline)

def main2():
   prompt = input()
   content = read_note_file("note.txt")

   enhanced_content = prompt_enhance_note(prompt, content)

   print(enhanced_content)

if __name__=="__main__":
   main2()
