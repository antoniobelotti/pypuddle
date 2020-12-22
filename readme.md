# API


    DataPuddle
        pwd() -> str
        cd(path :str) -> str
        mkdir(path :str) -> str
        rmdir(path :str) -> str
        store(file :jsonfile, filename :str) -> str
        retrieve(filename: str) -> jsonfile

use just one DataPuddle object. Each method can throw an error if the command fails.
