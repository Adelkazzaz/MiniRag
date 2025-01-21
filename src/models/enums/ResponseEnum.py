from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file_validated_successfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    MAX_FILE_SIZE_EXCEEDED = "Max_file_size_exceeded"
    FILE_UPLOADED_SUCCESS = "file_uploaded_success"
    FILE_UPLOADED_FAILED = "file_uploaded_failed"
    FILE_PROCESSING_FAILED = "file_processing_failed"
    FILE_PROCESSING_SUCCESS = "file_processing_success"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    NO_FILE_ERROR = "files_not_found"
    INVALID_PARAMETERS="invalid_parameters"