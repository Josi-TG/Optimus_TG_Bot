from random import randint

def yesOrNo():
    Answer_list = ["It is certain", "d=====(￣▽￣*)b", "Without a doubt", "( •_•)>⌐■-■  (⌐■_■)  Yes", "You may rely on it",
                  "As I see it, yes ( ͡• ͜ʖ ͡• )", "Most likely", "Outlook good", "Yessssss 〜(￣▽￣〜)~(￣▽￣)~*(〜￣▽￣)〜", "Signs point to yes", "( ͡• ͜ʖ ͡• )(ʘ ͜ʖ ʘ)(ʘ ͟ʖ ʘ)",
                  "Come again? My audio receptors are tweaking or some shiiii", "Better not tell you now (￣o￣) . z Z", "¯\_(ツ)_/¯", "Concentrate and ask again",
                  "Don't count on it", "My sources say no", "Outlook not so good",
                  "Very doubtful", "Not in a million years (づ￣ 3￣)づ", "( •_•)>⌐■-■  (⌐■_■)  No", "Negative", "FAH NAW (╯°□°）╯︵ ┻━┻", "Not a chance", "Nuh-uh", "Fat chance", "Not on your life", "Over my dead body  (•_•)"]
    rand_answer = Answer_list[randint(0, len(Answer_list) - 1)]
    return rand_answer

def quotes():
    Quote_list = ["You're gay (┬┬﹏┬┬)", "If you take care of the minutes, the hours take care of themselves", 
                  "There are decades where weeks happen, and weeks where decades happen.",
                  "The water doesn't get warmer, the later you jump.",
                  "Your level of success never exceeds your level of discipline.",
                  "Consistent hard work stacks invisible advantages that nobody sees, until the world calls you 'lucky'.",
                  "Don't practice until you get it right. Practice until you can't get it wrong.",
                  "Discipline looks boring, until you see what it builds.",
                  "Every wasted day is proof you don't want it.",
                  "Losers expect everything, while doing nothing. Winners expect nothing, while doing everything.",
                  "You don't learn to swim by reading about it.",
                  "A bad workout will always beat a skipped one.",
                  "God only made you fail to see if you would keep going."
                ]
    rand_quote = Quote_list[randint(0, len(Quote_list) - 1)]

    return rand_quote
