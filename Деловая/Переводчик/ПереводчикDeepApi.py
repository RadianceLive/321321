import tkinter as tk
import requests

DEEPL_API_KEY = "ВашAPi с deepl.com"

def translate_text():
    source_text = input_box.get("1.0", tk.END).strip()
    if not source_text:
        return
    response = requests.post(
        "https://api-free.deepl.com/v2/translate",
        data={
            "auth_key": DEEPL_API_KEY,
            "text": source_text,
            "target_lang": "EN"
        }
    )
    result = response.json()
    translation = result['translations'][0]['text']
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, translation)

root = tk.Tk()
root.title("AI Translator")
root.geometry("600x400")

tk.Label(root, text="Введите текст на русском:").pack()
input_box = tk.Text(root, height=10)
input_box.pack(pady=5)

tk.Button(root, text="Перевести", command=translate_text).pack(pady=10)

tk.Label(root, text="Перевод:").pack()
output_box = tk.Text(root, height=10)
output_box.pack(pady=5)

root.mainloop()
