from nlp_text_summarizer.config.configuration import ConfigurationManager
from nlp_text_summarizer.components.Data_Validation import DataValiadtion
from nlp_text_summarizer.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info("Data Validation Step is started")
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()
        logger.info("Data Validation is Done")