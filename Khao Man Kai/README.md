## Prerequisites
- Python 3.x installed on your machine
- pip package manager installed

## Installation Steps
1. Open your terminal or command prompt.
2. Create a new directory for your project (if needed) and navigate to it.
3. Run the following command to create a virtual environment:
    ```
    python -m venv myenv
    ```
4. Activate the virtual environment:
    - For Windows:
      ```
      myenv\Scripts\activate
      ```
    - For macOS/Linux:
      ```
      source myenv/bin/activate
      ```
5. Install the required libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```

## Running the Streamlit App
1. Add API key and your own prompt to Streamlit app code (`app.py`).
2. In the terminal, navigate to the directory where your Streamlit app code (`app.py`) file is located.
3. Make sure your virtual environment is activated (if not, follow step 4 from the installation steps).
4. Run the following command to start the Streamlit app:
    ```
    streamlit run app.py
    ```
5. Streamlit will start a local development server and provide a URL. Open your web browser and visit the provided URL to view and interact with your app.