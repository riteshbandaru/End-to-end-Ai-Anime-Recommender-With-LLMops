from src.data_loader import AnimeDataLoader
from src.vector_store import VectorstoreDb
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger=get_logger(__name__)

def main():
    try:
        logger.info("Pipeline initialized!!")
        data_loader = AnimeDataLoader("data/anime_with_synopsis.csv","data/processed1.csv")
        data=data_loader.load_and_process()
        logger.info("Data loaded and processed!!")

        vector_store=VectorstoreDb(data)
        vector_store.vector_store_build()
        logger.info("Vector store Built sucesfully....")

        logger.info("Pipelien built sucesfuly....")
    except Exception as e:
            logger.error(f"Failed to execute pipeline {str(e)}")
            raise CustomException("Error during pipeline " , e)
    
if __name__=="__main__":
     main()

        



