from random import randint

def yesOrNo():
    Answer_list = ["It is certain", "d=====(￣▽￣*)b", "Without a doubt", "( •_•)>⌐■-■  (⌐■_■)  Yes", "You may rely on it",
                  "As I see it, yes ( ͡• ͜ʖ ͡• )", "Most likely", "Outlook good", "Yessssss 〜(￣▽￣〜)~(￣▽￣)~*(〜￣▽￣)〜", "Signs point to yes", "( ͡• ͜ʖ ͡• )(ʘ ͜ʖ ʘ)(ʘ ͟ʖ ʘ)",
                  "Come again? My audio receptors are tweaking or some shiiii", "Better not tell you now (￣o￣) . z Z", "¯\_(ツ)_/¯", "Concentrate and ask again",
                  "Don't count on it", "My sources say no", "Outlook not so good",
                  "Very doubtful", "Not in a million years (づ￣ 3￣)づ", "( •_•)>⌐■-■  (⌐■_■)  No", "Negative" "FAH NAW (╯°□°）╯︵ ┻━┻", "Not a chance", "Nuh-uh", "Fat chance", "Not on your life", "Over my dead body  (•_•)"]
    rand_answer = Answer_list[randint(0, len(Answer_list) - 1)]
    return rand_answer

def quotes():
    Quote_list = ["You're gay (┬┬﹏┬┬)"
                ]
    rand_quote = Quote_list[randint(0, len(Quote_list) - 1)]

    return rand_quote
