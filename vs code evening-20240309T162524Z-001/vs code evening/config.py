# config.py

class AppConfig:
    title = "Image to Story Converter"
    theme = "light"  # or "dark"
    css = "path/to/custom.css"  # Path to custom CSS file
    genre = ["Horror", "Fiction", "Children Literature", "Comedy", "Surrealism"]
    writing_style_list = ["Narrative", "Formal", "Symbolic", "Experimental", "Non-linear"]
    openai_max_access_count = 1000  # Maximum allowed OpenAI requests
    openai_curr_access_count = 500  # Currently used OpenAI requests

app_config = AppConfig()
