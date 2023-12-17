from nlp_text_summarizer.config.configuration import ConfigurationManager
from nlp_text_summarizer.components.Data_Transformation import DataTransformation
from nlp_text_summarizer.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info("Data Transformation Step is started")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        logger.info("Data Transformation Step is Done!!")