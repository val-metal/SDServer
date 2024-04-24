from diffusers import StableDiffusionPipeline
import torch
import time
import os
from prompt import Prompt
from diffusionsettigs import DiffusionSettings

class DiffusionModel:
    path:str
    name:str
    def __init__(self,path,name) -> None:
        self.path=path
        self.name=name
    
    def check_file(self,string):
        for file in os.listdir("./"):
            if file == string:
                return True
        return False
    def diffuse(self,prompt:Prompt): 
        settings = DiffusionSettings()
        for i in range(prompt.repeat):
            pipe = StableDiffusionPipeline.from_pretrained(self.path)
            pipe = pipe.to(settings.pipeto)
            pipe.max_inference_steps = settings.interference
            image = pipe(prompt.text).images[0]
            save_name=prompt.text+".png"
            namecounter=0
            while(self.check_file(save_name)):
                namecounter+=1
                save_name=prompt.text+str(namecounter)+".png"
            image.save(save_name)