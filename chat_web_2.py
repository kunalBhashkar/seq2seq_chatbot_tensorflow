import uvicorn
import datetime
from os import path
from fastapi import FastAPI, Request, APIRouter
from fastapi import APIRouter
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


import general_utils
import chat_command_handler
from chat_settings import ChatSettings
from chatbot_model import ChatbotModel
from vocabulary import Vocabulary

class ChatRequest(BaseModel):
    question: str



def build_routers() -> APIRouter:
    v1_router = APIRouter()

    v1_router.include_router(_build_chat_router())

    return v1_router


def _build_chat_router() -> APIRouter:
    router = APIRouter()
    checkpointfile = "models/trained_model_v2/best_weights_training.ckpt"
    model_dir, hparams, checkpoint = general_utils.initialize_session_server(checkpointfile)

    #Load the vocabulary
    print()
    print ("Loading vocabulary...")
    if hparams.model_hparams.share_embedding:
        shared_vocab_filepath = path.join(model_dir, Vocabulary.SHARED_VOCAB_FILENAME)
        input_vocabulary = Vocabulary.load(shared_vocab_filepath)
        output_vocabulary = input_vocabulary
    else:
        input_vocab_filepath = path.join(model_dir, Vocabulary.INPUT_VOCAB_FILENAME)
        input_vocabulary = Vocabulary.load(input_vocab_filepath)
        output_vocab_filepath = path.join(model_dir, Vocabulary.OUTPUT_VOCAB_FILENAME)
        output_vocabulary = Vocabulary.load(output_vocab_filepath)




    @router.post("/chat")
    async def chat(
        req: ChatRequest
    ):
        print ("Initializing model...")
        print()
        with ChatbotModel(mode = "infer",
                        model_hparams = hparams.model_hparams,
                        input_vocabulary = input_vocabulary,
                        output_vocabulary = output_vocabulary,
                        model_dir = model_dir) as model:

            #Load the weights
            print()
            print ("Loading model weights...")
            model.load(checkpoint)

            # Setting up the chat
            chatlog_filepath = path.join(model_dir, "chat_logs", "web_chatlog_{0}.txt".format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")))
            chat_settings = ChatSettings(hparams.model_hparams, hparams.inference_hparams)
            chat_command_handler.print_commands()
            
        is_command, terminate_chat, _ = chat_command_handler.handle_command(req.question, model, chat_settings)
        if terminate_chat:
            answer = "[Can't terminate from http request]"
        elif is_command:
            answer = "[Command processed]"
        else:
            #If it is not a command (it is a question), pass it on to the chatbot model to get the answer
            _, answer = model.chat(req.question, chat_settings)
            
            if chat_settings.inference_hparams.log_chat:
                chat_command_handler.append_to_chatlog(chatlog_filepath, req.question, answer)

        return answer
    
    return router





app = FastAPI()

# allow for browser connections
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(build_routers(), prefix="/v1")


uvicorn.run(app, host="0.0.0.0", port=8080)