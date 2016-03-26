#!/usr/bin/python

#------------------------------------------------------------------------------
# hello - Alternative Hello World program
# Copyright (C) 2016  Domagoj Marsic
#
# Released under the MIT License.
#------------------------------------------------------------------------------

"""Hello prints a random Futurama quote.

Sometimes you need a test program that will execute, let you know
that everything is running and exit with no other side-effect.
Basically a hello world program. But it doesn''t have to be the boring
old 'Hello World'.

Here is the shiny metal script that can be used for all your test
purposes. Or at least some of them.

Usage:
    hello.py

Quote sources:
* https://en.wikiquote.org/wiki/Futurama
* http://www.imdb.com/title/tt0149460/quotes
* https://twitter.com/QuotesFuturama
"""

import random

quotes = [
"Good news everyone!",
"Bite my shiny metal ass!",
"Sweet zombie Jesus!",
"So long, jerkwads",
"I don't want to live on this planet anymore.",
"There's no scientific consensus that life is important.",
"You took away his robot humanity!",
"Bring me a bag of Bigfoot's droppings or shut up!",
"Evolution is under attack in our schools? To the science mobile!",
"I can't be mad. I'm on way too many painkillers.",
"I spent a semester in Africa harpooning giraffes, and giraffes are basically just land space whales.",
"Your mistletoe is no match for my TOW missile!",
"What? A fella can't drop in on old friends and hold them hostage?",
"Pathetic humans, prepare to write down the recipe!",
"I don't like the feeling of this gang-infested neighborhood. There might be spiders!",
"I blame today's violent media.",
"Live free or Dont.",
"Robo-Puppy commencing two hour yipping session.",
"Death by Snu-Snu!",
"The spirit is willing, but the flesh is spongy and bruised.",
"Brannigan's Law is like Branigan's love - fast and hard!",
"Anyone who laughs is a communist!",
"Time for you to shut up!",
"It's not just safe; it's 40% safe.",
"I choose to believe what I was programmed to believe!",
"He's opening our minds to new ideas. Kill him!",
"Oh dear, she's stuck in an infinite loop and he's an idiot! Oh well, that's love for you, I guess.",
"I choose to believe they're alive in some other dimension. Screamin' in agony.",
"You changed the outcome by measuring it.",
"Shut up, baby. You love it.",
"Feelings are dumb and should be hated.",
"Fire all weapons and set a transmission frequency for my victory yodel.",
"Goodbye, friends. I never thought I'd die like this. But I always really hoped.",
"You win again, gravity!",
"What planet is this, anyway?",
"Why didn't they build it with 6,001 hulls?! When will they learn?",
]

if __name__ == '__main__':
    r = random.randint(0, len(quotes))
    print quotes[r]
