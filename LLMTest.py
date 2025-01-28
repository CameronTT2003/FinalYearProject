"""
LM Studio Tool Use Demo: Prompt and Text Processing
Send a prompt and a list of texts to LM Studio.
"""

# Standard library imports
import json
import sys
import threading
import time
import itertools

# Third-party imports
from openai import OpenAI

# Initialize LM Studio client
client = OpenAI(base_url="http://127.0.0.1:1234/v1", api_key="lm-studio")
MODEL = "llama-3.2-1b-instruct"

# Class for displaying the state of model processing
class Spinner:
    def __init__(self, message="Processing..."):
        self.spinner = itertools.cycle(["-", "/", "|", "\\"])
        self.busy = False
        self.delay = 0.1
        self.message = message
        self.thread = None

    def write(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def _spin(self):
        while self.busy:
            self.write(f"\r{self.message} {next(self.spinner)}")
            time.sleep(self.delay)
        self.write("\r\033[K")  # Clear the line

    def __enter__(self):
        self.busy = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.busy = False
        time.sleep(self.delay)
        if self.thread:
            self.thread.join()
        self.write("\r")  # Move cursor to beginning of line


def send_prompt_with_texts(prompt: str, texts: list):
    """
    Sends a prompt and a list of texts to the LM Studio model.
    
    Args:
        prompt (str): The prompt guiding the model's response.
        texts (list): A list of input texts to process.
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are an assistant that processes user-provided comments. "
                "Respond to the prompt and summerise the list of comments provided focussing on sentiment."
                "You are to only give a paragraph and no statistical data."
            ),
        },
        {"role": "user", "content": f"{prompt}\n\nTexts: {json.dumps(texts)}"},
    ]

    try:
        with Spinner("Processing..."):
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=True,
            )

        print("\nAssistant:", end=" ", flush=True)
        collected_content = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                print(content, end="", flush=True)
                collected_content += content
        print()  # New line after streaming completes

    except Exception as e:
        print(
            f"\nError communicating with LM Studio!\n\n"
            f"Please ensure:\n"
            f"1. LM Studio server is running at 127.0.0.1:1234 (hostname:port)\n"
            f"2. Model '{MODEL}' is downloaded\n"
            f"3. Model '{MODEL}' is loaded, or that just-in-time model loading is enabled\n\n"
            f"Error details: {str(e)}\n"
            "See https://lmstudio.ai/docs/basics/server for more information"
        )
        exit(1)


if __name__ == "__main__":
    # Example usage
    prompt = "Look at all these comments and give me a paragraph"
    texts = ['I loved reading "her" tweets!', 'Don’t tempt me', 'To be fair, the transsexuals have been falling in love with each other on here since day one', 'I can play the part, maybe uncle though. Not aunt', 'A long-time poster needs to die by suicide by cop and a debate between "he was mentally ill, this is a tragedy" and "fuck that guy, he was an asshole" has to rage on in the comments to his wife\'s eulogy post. That\'s the end game here.', 'Oh.', "Well, I've already been DM'd by some rando woman who insisted she met me at a conference we allegedly attended together in Las Vegas, if that counts for something. She could have been my middle aged aunt if I used Uncle Rico's time machine to go 35 years back before I was born.", 'I will get a sitcom based on things my fake father posts', 'I’m game … who needs a mommy?', 'Its sounding like I need to make my feelings more obvious, Hippo.', 'I agree, sign lady. The "sins of omission" often surpass the "sins of commission"!', ' 😂🤣🤦🏼\u200d♀️', 'Bzzt wrongo, won’t fully be twitter until the Group Chat Wars begin', 'We need to have a sex tour freak', 'Needs more palace intrigue.', 'We also need Italian Elon musk, Biden  insult bot, and that one really good Ted cruz parody account', '💕hey💕', 'Someone gotta have a crazy road trip to Florida with a pimp and a stripper.', 'Chicago Party Aunt', "I'm getting to it, geez. Now you took all the fun out of it,  you telling me to do it.", '', 'I’ll do a wife email', 'Elon? That you?', 'I wish I understood this joke 😂', 'i know that is a sarcastic joke , but when/where did this happen', "I'm a middle aged aunt 😬", 'Well I love everybody, so deal with that.', 'we need heroes, and if not heroes, someone who will relentlessly fundraise to fund an unruly fake service dog', 'bsky.app/profile/beav...', 'Please pay no attention to my handsome nephew', 'Save time and combine operations.\n\nyoutu.be/420C_Nq1-dA?...', 'generalstrikeus.com/strikecard', "I can and I will, will you? Let's show them that WE THE PEOPLE are the real power in this country!", "I give off certain aunt-like vibes at times, but, I don't pretend to be one.", 'Best I can do is bad bean-oriented parenting', '¡Viva Gretchen!', 'Not enough wife guys', "Or a crypto queen trying to convince you it's a good thing", 'That sounds like bluesky 2023', 'I will pretend to be an inebriated uav', 'nc Auntie ☺️', 'remember the drama with the nice lady who fell for the guy who claimed he was in the Israel army and single, but had a wife and child, who he both abused?', 'Does anyyone want it to be fully twitter?', 'I had a Pretty Lady Bot show up in my mentions with a "hey," does that count', 'Got to say, my favorite thread of the day', "But I'm already in love with you Internet Hippo", 'If nobody has already called dibs, I’ll do the aunt thing', 'I’m personally calling dibs on cosplaying as an IRA member while really being a random dude from the southern US.', "Jokes on you.  \n\nI am a middle aged aunt but I'm pretending to be a 40 year old punk.", 'Here’s the plan. First I write an email demeaning him. Then I go on legacy media and say he’s a good boy. Then I refuse to answer yes or no at the confirmation hearing', "It's me. You're Authentic Middle Aged Italian Aunt™️", '🤣🤣🤣🤣🤣🤣🤣🤣', "In the UK we have a tv show called 'Cash in the Attic'.   Stick them up there for a while and wait till they turn into 'Collectables'.  Sorted!\nFull disclosure, most people refer to it as 'Crap in the Attic'. 🦉", 'Spoken like a lovable shit posting hippo 😍', "Someone also needs to say the F slur in some obscure part of the website (It won't be me).", 'I miss the glory days, of wife emails, podcast boob callout threads and a large account that pretended to be a single dad but it was actually his sister’s kid', 'Bahahaha...', 'I never noticed that happening in Twitter.', 'I will be happy if this place is never “fully Twitter”.', 'I was severely disappointed by the lack of Watto discourse yesterday.', "I can't wait", 'That last one is super specific.', 'I want to be catfished by a 40+ year old lady. I just think it makes me feel wanted… please?', '🤞', 'And at least a couple fall in love with the middle aged aunt', 'It’s me, your auntie!!! Send me all of your money!!!   Oh, and I love you!!!  /jk', 'I am going to start pretending to be a PT Cruiser', 'Has blue sky had a member of Congress get caught pretending to be a person of color yet?', "..or a Congressman's cow.", 'I’m furiously moving my birthday until we get juuust the right tempo here.', 'Old enough to remember this', 'I technically love the butterfly 🦋', 'Bwahahahaha', 'chef tip: pretend to be a middle aged aunt to make bluesky twitter.', "If I wanted crazy, I would've stayed there.\nNo thanks.", 'If the neighbor chili thing happens again I’m deleting my account', 'I volunteer as tribute! ✌', 'It isn’t fully Twitter until I have to close my entire app in a panic because some dude’s dick and balls showed up at the top of my feed at 8AM for some fucking reason', 'Where\'s that one person pretending to be conjoined twins who "married" each other?', 'Lets keep it that way then', "We don't want it to be Twitter though", 'I fall in love easily, who wants to fall in love?', 'Someone’s going to have to drive to Temecula or something']
    send_prompt_with_texts(prompt, texts)
