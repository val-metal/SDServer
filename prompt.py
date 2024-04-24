class Prompt:
    text:str
    model=[]
    repeat:int
    isdone:bool
    def __init__(self,rawprompt) -> None:
        sep=rawprompt.split(";")
        if(len(sep)==3):
            self.text=sep[0]
            models=sep[1].split(",")
            for x in models:
                self.model.append(x)
            self.repeat=int(sep[2])
        isdone=False

    def isForModel(self,modelname):
        for x in self.model:
            if x==modelname:
                return True
            else:
                return False