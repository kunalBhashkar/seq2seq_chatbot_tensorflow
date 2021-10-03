# seq2seq-chatbot
A sequence2sequence chatbot implementation with TensorFlow.

## Chatting with a trained model

For console chat: 
1. Run `chat_console_best_weights_training.bat` or `chat_console_best_weights_validation.bat`

For web chat:
1. Run `chat_web_best_weights_training.bat` or `chat_web_best_weights_validation.bat`

2. Open a browser to the URL indicated by the server console, followed by `/chat_ui.html`. This is typically: [http://localhost:8080/chat_ui.html](http://localhost:8080/chat_ui.html)

### To chat with a trained model from a python console:

1. Set console working directory to the **seq2seq-chatbot** directory. This directory should have the **models** and **datasets** directories directly within it.

2. Run chat.py with the model checkpoint path:
```shell
run chat.py models\cornell_movie_dialog\trained_model\best_weights_training.ckpt
```

## Training a model
To train a model from a python console:

1. To train a new model, run train.py with the dataset path:
```shell
run train.py --datasetdir=datasets\dataset_name
```

Or to resume training an existing model, run train.py with the model checkpoint path:
```shell
run train.py --checkpointfile=models\dataset_name\model_name\checkpoint.ckpt
```
## Visualizing a model in TensorBoard

To start TensorBoard from a terminal:
```shell
tensorboard --logdir=model_dir
```
## Dependencies
The following python packages are used in seq2seq-chatbot:
(excluding packages that come with Anaconda)

- [TensorFlow](https://www.tensorflow.org/)
    ```shell
    pip install --upgrade tensorflow
    ```
    For GPU support: [(See here for full GPU install instructions including CUDA and cuDNN)](https://www.tensorflow.org/install/)
    ```shell
    pip install --upgrade tensorflow-gpu
    ```

- [jsonpickle](https://jsonpickle.github.io/)
    ```shell
    pip install --upgrade jsonpickle
    ```

- [flask 0.12.4](http://flask.pocoo.org/) and [flask-restful](https://flask-restful.readthedocs.io/en/latest/) (required to run the web interface)
    ```shell
    pip install flask==0.12.4
    pip install --upgrade flask-restful
    ```


Forked after cloning, configured new repo according to this guide: https://gist.github.com/jagregory/710671
