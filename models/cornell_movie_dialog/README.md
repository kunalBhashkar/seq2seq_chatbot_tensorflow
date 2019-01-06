# Trained Models for Cornell Movie Dialog Corpus

## Trained Model v2 (Jul 21 2018)
This model was initialized using the [nnlm_en](../../embeddings/nnlm_en/README.md) pre-trained word embedding vectors. Embeddings were updated during training.

You can download it from [here](https://drive.google.com/uc?id=1y1b1vXeSti5lpBACNdYlo8HbVJDUO3ir&export=download).

After download, unzip the folder **trained_model_v2** into this directory.

## Trained Model v1 (Mar 29 2018)
You can download it from [here](https://drive.google.com/uc?id=1Ig-sgdka5QpgE-b9g4ZQqnGGCrE-2f4p&export=download).

After download, unzip the folder **trained_model_v1** into this directory.

To chat with the trained cornell movie dialog model **trained_model_v2**:

1. Download and unzip [trained_model_v2](seq2seq-chatbot/models/cornell_movie_dialog/README.md) into the [seq2seq-chatbot/models/cornell_movie_dialog](seq2seq-chatbot/models/cornell_movie_dialog) folder

2. Set console working directory to the **seq2seq-chatbot** directory

3. Run:
```shell
run chat.py models\cornell_movie_dialog\trained_model_v2\best_weights_training.ckpt
```
