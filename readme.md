# API


    DataPuddle
        pwd() -> str
        cd(path :str)
        mkdir(path :str)
        rmdir(path :str)
        store(file :jsonfile, filename :str, overwrite=False)
        retrieve(filename: str) -> jsonfile
        rm(filename:str) 

use just one DataPuddle object. Each method can throw an error if the command fails.
