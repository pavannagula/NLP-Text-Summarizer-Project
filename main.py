from nlp_text_summarizer.logging import logger
from nlp_text_summarizer.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline
from nlp_text_summarizer.pipeline.pipeline_data_validation import DataValidationTrainingPipeline


STAGE_01 = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_01} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_01} completed <<<<<<\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_02 = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_02} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_01} completed <<<<<<\n")
except Exception as e:
        logger.exception(e)
        raise e
