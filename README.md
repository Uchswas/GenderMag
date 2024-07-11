## Installation

1. Run the following command to install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Copy `.env.example` to `.env`
3. Add your `OPENAI_API_KEY` and `PROMPTLAYER_API_KEY`.

## How to Run

1. Navigate to the `src` folder:
    ```bash
    cd src
    ```

2. Run the project:
    ```bash
    python3 main.py
    ```

## Steps to Reproduce

1.  All the sessions are saved in the `inputs` folder, structured and named with their tag.

2. Copy the desired session to `subgoals_actions.py`

3. Run the main.py:
    ```bash
    python3 main.py
    ```

4. It will reproduce the result and the output can be found in your Promptlayer Dashboard.



## Accessibility of the Images

The images required for the GenderMag sessions are saved in the `html/images` folder. These images must be public so that the LLM can access them.

You can make the repository public while running the sessions. While making your repository public temporarily can be a quick solution, it poses security risks.

### Alternative Solution:

1. Copy all the image files to a permanent hosting location (e.g., another GitHub repository or a different hosting service).
2. Update the `BASE_IMAGE_PATH` variable in `constant.py` to reflect the new image folder link.

---



