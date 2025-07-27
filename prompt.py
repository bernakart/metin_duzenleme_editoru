def create_prompt(dil_mesajlari, tarz_mesajlari, dil, tarz, baslik, ozet):
    prompt = "Sen profesyonel bir yazı editörüsün. "
    prompt += dil_mesajlari.get(dil, "")
    prompt += " " + tarz_mesajlari.get(tarz, tarz_mesajlari["hicbiri"])
    if baslik:
        prompt += " Metne uygun etkileyici bir başlık oluştur."
    if ozet:
        prompt += " Metni özetle ve ana noktaları vurgula."
    return prompt
