# NiuDownload
> This is a tool that can automatically download models from Hugging Face(Windows or Linux).You can download single model or make batch download. The project is powered by NEU(China) NLPLAB master students: Peinan Feng, Junhao Ruan and Peizhuo Liu. Any issue is welcomed.
**Only pytorch version models are supported now**
## Use in python script
### Single Download
    from sao_download import download as sd
    sd.batch_download_models('models', 'gpt2')
   In this way, the whole gpt2 model in pytorch version will be stored in "models" directory.
### Batch Download
    from sao_download import download as sd
    sd.batch_download_models('models', ['roberta-base', 'gpt2', 'bert-base-uncased'])
    #or 
    sd.batch_download_models('models', 'roberta-base, gpt2, bert-base-uncased')
  In this way, roberta-base、 gpt2、 bert-base-uncased will be stored in "models" directory.
### Use in command line
     niudownload -m bert-base-uncased,gpt2 -d /mnt/lpz/download/
  "-m" means the model(s) from Huggingface you want to download
  "-d" means the output dirct you want to store the model(s)
