from magic8ball import yesOrNo, quotes

TRIGGERS = {
    "hey": lambda _: f"Hello there!",
    "hi": lambda _: f"Hello there!",
    "hello": lambda _: f"Hello there!",
    "how are you": lambda _: "I am doing well, thank you for asking 👈(ﾟヮﾟ👈)",
    "who are you": lambda _: "I am Optimus Prime, AKA leader of the AutoBots, AKA Decepticon Demolisher, AKA Fulltime Energon sniffing expert, either you stand beside me or choke on my blaster while you grind and gurgle my sword with your teeth through the back of your skull. ♨︎_♨︎",
    "what is your name": lambda _: "I am Optimus Prime, AKA leader of the AutoBots, AKA Decepticon Demolisher, AKA Fulltime Energon sniffing expert, either you stand beside me or choke on my blaster while you grind and gurgle my sword with your teeth through the back of your skull. ♨︎_♨︎",
    "what's your name": lambda _: "I am Optimus Prime, AKA leader of the AutoBots, AKA Decepticon Demolisher, AKA Fulltime Energon sniffing expert, either you stand beside me or choke on my blaster while you grind and gurgle my sword with your teeth through the back of your skull. ♨︎_♨︎",
    "say something cool": lambda _: quotes(),
    "say something deep": lambda _: quotes(),

}


def handle_response(text: str) -> str:
    processed = text.lower()

    for trigger, func in TRIGGERS.items():
        if trigger in processed:
            return func(processed)
    
    # If no trigger matches, default to yes/no
    return yesOrNo()