from nlp_text_summarizer.logging import logger
from nlp_text_summarizer.pipeline.pipeline_data_ingestion import DataIngestionTrainingPipeline
from nlp_text_summarizer.pipeline.pipeline_data_validation import DataValidationTrainingPipeline
from nlp_text_summarizer.pipeline.pipeline_data_transformation import DataTransformationTrainingPipeline


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
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_02} completed <<<<<<\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_03 = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_03} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_03} completed <<<<<<\n")
except Exception as e:
        logger.exception(e)
        raise e