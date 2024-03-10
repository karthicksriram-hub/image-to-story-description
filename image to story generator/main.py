import gradio as gr
import model
from config import app_config
import mongo_utils as mongo

def clear():
    return None, 50, 0.7, None, None

def create_interface():
    with gr.Blocks(
        title=app_config.title, theme=app_config.theme, css=app_config.css
    ) as app:
        
        app.load()

        
        with gr.Row():
            
            with gr.Column():
                max_count = gr.Textbox(
                    label="Max allowed OpenAI requests:",
                    value=app_config.openai_max_access_count,
                )
                curr_count = gr.Textbox(
                    label="Used up OpenAI requests:",
                    value=app_config.openai_curr_access_count,
                )
                available_count = gr.Textbox(
                    label="Available OpenAI requests:",
                    value=app_config.openai_max_access_count
                    - app_config.openai_curr_access_count,
                )

        # Input section
        with gr.Row():
            with gr.Column():
                image = gr.Image(
                    type="file",
                )
                with gr.Row():
                    with gr.Column():
                        genre = gr.Dropdown(
                            label="Story Genre: ",
                            value="Poetry",
                            choices=app_config.genre + ["Poetry"],
                        )
                        style = gr.Dropdown(
                            label="Story Writing Style:",
                            value="Cinematic",
                            choices=app_config.writing_style_list + ["Cinematic"],
                        )
                    with gr.Column():
                        word_count = gr.Slider(
                            label="Story Length (words):",
                            minimum=30,
                            maximum=200,
                            value=50,
                            step=10,
                        )
                        creativity = gr.Slider(
                            label="Creativity Index:",
                            minimum=0.3,
                            maximum=1.0,
                            value=0.7,
                            step=0.1,
                        )
                with gr.Row():
                    submit_button = gr.Button(
                        value="Generate Story", 
                        label="Generate Story",
                        type="submit",
                        theme="success"
                    )
                    clear_button = gr.ClearButton(
                        value="Clear",
                        label="Clear",
                        type="reset",
                        theme="danger"
                    )
            with gr.Column():
                story = gr.Textbox(
                    label="Story:",
                    placeholder="Generated story will appear here.",
                    lines=21,
                    readonly=True
                )

        # Examples section
        with gr.Row():
            with gr.Accordion("Expand for examples:", open=False):
                gr.Examples(
                    examples=[
                        [
                            "assets/examples/cheetah-deer.jpg",
                            "Horror",
                            "Narrative",
                            80,
                            0.5,
                        ],
                        [
                            "assets/examples/man-child-pet-dog.jpg",
                            "Fiction",
                            "Formal",
                            100,
                            0.6,
                        ],
                        [
                            "assets/examples/man-child.jpeg",
                            "Children Literature",
                            "Symbolic",
                            120,
                            1.0,
                        ],
                        [
                            "assets/examples/men-fighting.jpg",
                            "Comedy",
                            "Experimental",
                            60,
                            0.6,
                        ],
                        [
                            "assets/examples/teacher-school.jpg",
                            "Surrealism",
                            "Non-linear",
                            100,
                            0.7,
                        ],
                    ],
                    fn=model.generate_story,
                    inputs=[image, genre, style, word_count, creativity],
                    outputs=[story, max_count, curr_count, available_count],
                    run_on_click=True,
                )

    return app

if __name__ == "__main__":
    mongo.fetch_curr_access_count()
    app = create_interface()
    app.launch()
