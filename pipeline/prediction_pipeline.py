from src.prompt_template import get_anime_prompt
from src.recommender import AnimeRecommender
from src.vector_store import VectorstoreDb
from config.config import GROQ_API_KEY,MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger=get_logger(__name__)

class AnimePredictionPipeline:

    def __init__(self,persist_dir:str="chroma_db"):

        try:
            logger.info("Anime Prediction Pipeline initialized!!")
            
            vector_build= VectorstoreDb(csv_path="",persist_dir=persist_dir)

            retriever = vector_build.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipleine intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to intialize pipeline {str(e)}")
            raise CustomException("Error during pipeline intialization" , e)
        
    def recommend(self,query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfulyy...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation" , e)



