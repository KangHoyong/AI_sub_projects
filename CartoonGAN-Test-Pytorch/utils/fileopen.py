import os 
import logging
import logging.handlers
import argparse

from loggerHandler import loggerHandler

# output save dir and log save dir
os.makedirs("./output" , exist_ok=True) 
os.makedirs("./server" , exist_ok=True)

# logging instance 생성 
logger = logging.getLogger("my")

streamHandler , fileHandler = loggerHandler()

# logger instance in handler set
logger.addHandler(streamHandler)
logger.addHandler(fileHandler)

# logging set
logger.setLevel(level=logging.DEBUG)

# ext Tyep
extTyep = [".jpg" , "png" , "jpeg"]

def searchfile(dirPath , savePath) : 

    # try : 풀더 접근 권한이 없는 경우 
    try : 
        fileNames = sorted(os.listdir(dirPath))
        for fileName in fileNames : 
            fullFilename = os.path.join(dirPath, fileName) 
            logger.debug(fullFilename)
            # logging.debug("FileName : " ,fileName)

            if os.path.isdir(fullFilename) : 
                """
                dataset(root)
                    - 1.png
                    - 0 (sub1)
                      |-------> 0.j
                하위 디렉토리 싹다 돌면서 이미지 파일 경로 찾아옴 

                """
                searchfile(fullFilename, savePath)
            else :
                # aaaa.jpg -> ext = .jpg
                ext = os.path.splitext(fullFilename)[-1]
                if ext not in extTyep : 
                    continue

                # image -> CatoonGan 
                logger.info(fullFilename)

    except PermissionError :
        pass


def main(config) : 

    searchfile(config.data , config.save)
    return 0 

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="dataset foloder  : get image file")

    # dataset floder path 
    parser.add_argument("--data" , type=str, default="./test_img")

    # data save path 
    parser.add_argument("--save" , type=str, default="./output")
    config = parser.parse_args()
    main(config)