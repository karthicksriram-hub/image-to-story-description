from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Predefined stories
stories = [
   """
    The ancient oaks stood sentinel, their gnarled branches clawing at the twilight sky. The wind, usually a gentle sigh, whispered with urgency tonight. Elara, a woman with hair the color of autumn leaves and eyes that mirrored the forest floor, felt a shiver crawl down her spine. Unlike the villagers who feared the rustling leaves, Elara understood the language of the woods. The wind spoke of danger, a predator stalking the hidden paths, or perhaps a storm brewing with teeth like lightning. Ignoring the chill that snaked down her spine like a serpent, Elara traced the wind's path, determined to warn the nearby village. Their safety, she knew, rested on her ability to decipher the forest's whispers.
    """,
    """
    Kai, a fisherman with sun-baked skin and eyes the color of the summer sky, cast his line into the shimmering river. Disappointment gnawed at him like a persistent fish. Days blurred together, each ending with empty nets and a gnawing hunger. As the sun dipped below the horizon, painting the water in hues of orange and purple, a flash of silver caught his eye. It wasn't a fish, but something far more extraordinary. Nestled amongst the smooth pebbles lay a magnificent pearl, its surface reflecting the dying sunlight with an ethereal glow. Unlike any he'd ever seen, it pulsed with an inner light. Gratitude washed over him, warm and unexpected. The river, in its own mysterious way, had provided. Perhaps tomorrow, the fish would return, but tonight, he held a treasure far more valuable.
    """,
    """
    Amara, a woman with hair the color of moonlight and eyes as vast as the ocean itself, stood sentinel in the solitary lighthouse tower. The salty wind whipped at her cloak, carrying the scent of brine and distant shores. Tonight, the sky was a canvas splashed with a million stars, their reflections dancing on the waves like celestial ballerinas. An irresistible pull, a yearning for the unknown, tugged at her heart. Curiosity, a constant companion, warred with the responsibility etched into her soul. Ignoring the usual protocol of maintaining a constant light, Amara lit a smaller fire on the ground, a faint beacon leading away from the lighthouse. Perhaps the ocean, vast and untamed, held secrets waiting to be discovered. But the consequences of venturing into the unknown were a risk she wasn't sure she was willing to take. Yet, the stars seemed to whisper promises of adventure, a melody too captivating to ignore.
    """,
    """
    Tenzing, a weathered guide with wrinkles etched by years of battling the elements, squinted at the darkening clouds gathering around the mountain's peak. The air, once crisp and clear, grew thick with an unsettling stillness. It was a sign, one he recognized all too well - a blizzard was brewing, its icy breath whispering a deadly promise. Fear flickered in his eyes, but he quickly masked it with a stern expression. He urged his clients, a group of thrill-seeking adventurers, to turn back. The summit, once a goal, now loomed like a hungry beast. Ignoring the warnings, a young woman with eyes full of misplaced bravado pressed on. The challenge, the thrill of conquering the peak, was too much to resist. Soon, the wind howled like a banshee, and blinding snow engulfed them. Tenzing knew he had to act fast. The mountain's fury was upon them, and survival hinged on his experience and his ability to lead them through the treacherous whiteout. 
    """,
    """
    The sun dipped below the horizon, painting the sky in a canvas of fiery oranges and soft pinks. Maya, a young artist with hair the color of wheat and eyes that captured the vibrant hues of nature, entered the meadow. This field, nestled beside a babbling brook, held a special magic for her. Every summer, a mesmerizing spectacle unfolded. As twilight descended, thousands of fireflies, like tiny lanterns, emerged from the tall grass. Their tiny lights blinked on and off in a synchronized rhythm, creating a breathtaking symphony of light. Maya, captivated by the ethereal dance, watched, her artist's soul yearning to capture the magic on canvas. The fireflies weren't just beautiful; they were a testament to nature's delicate balance, a fleeting display of wonder that would vanish with the first rays of dawn. They served as a reminder to Maya to cherish the fleeting beauty that surrounded her, to translate the whispers of the wind and the songs of the fireflies into art that could endure long after the magic of the night had faded.
    """
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        # Check if the post request has the file part
        if 'file' not in request.files:
            return render_template("index.html", message="No file part")
        
        file = request.files['file']
        # If user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return render_template("index.html", message="No selected file")

        # Generate a random story from the predefined list
        story = random.choice(stories)

        return render_template("result.html", story=story)

if __name__ == "__main__":
    app.run(debug=True)
