# This is a tool that can automatically download models from Hugging Face(Windows or Linux).You can download single model or make batch download.

- ## Download "roberta-base" from Hugging face to "models" 
    ```
    import saodownload as sd
    sd.download_models('models', ['gpt2'])
    ```
  ### And then, the whole gpt2 model in pytorch will be stored in "models" direct.
- ## Batch Download pytorch models from Hugging Face
    ```
    import saodownload as sd
    sd.download_models('models', ['roberta-base', 'gpt2', 'bert-base-uncased'])
    ```
  ### This code will download roberta-base、 gpt2、 bert-base-uncased into "models"