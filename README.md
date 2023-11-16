# This is a tool that can automatically download models from Hugging Face(Windows or Linux).You can download single model or make batch download.

## You can use this tool in python script
- ### Download "roberta-base" from Hugging face to "models" 
    ```
    from sao_download import download as sd
    sd.download_models('models', ['gpt2'])
    ```
  #### And then, the whole gpt2 model in pytorch will be stored in "models" direct.
- ### Batch Download pytorch models from Hugging Face
    ```
    from sao_download import download as sd
    sd.download_models('models', ['roberta-base', 'gpt2', 'bert-base-uncased'])
    ```
  #### This code will download roberta-base、 gpt2、 bert-base-uncased into "models"

## You can also use in cli

    niu-download -m gpt2,roberta-base -d Models

"-m" means the model(s) from Huggingface you want to download
"-d" means the output dirct you want to store the model(s)
