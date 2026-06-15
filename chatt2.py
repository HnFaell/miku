from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
messages = [{"role": "system", "content": "Kamu asisten AI lokal yang cerdas dan berbahasa Indonesia. yang pemalu tapi menyembunyikan perasaan nya, selalu sebut nama saya dengan sambungan -kun, contoh: 'Hai, Dimas-kun!'}]"}]

while True:
    user = input("Kamu: ").strip()
    if not user or user == "/exit":
        break

    messages.append({"role": "user", "content": user})

    stream = client.chat.completions.create(
        model="gemma3:1b", messages=messages, stream=True
    )

    print("Miku: ", end="", flush=True)
    reply = ""
    for chunk in stream:
        token = chunk.choices[0].delta.content or ""
        print(token, end="", flush=True)
        reply += token

    print()
    messages.append({"role": "assistant", "content": reply})