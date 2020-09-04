import logging

def loggerHandler() : 
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')

    # handler 생성 (stream, file)
    streamHandler = logging.StreamHandler()
    fileHandler = logging.FileHandler("./server/server.log")

    # logger instance in fomatter set
    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    return streamHandler, fileHandler
