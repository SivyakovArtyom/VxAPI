from api.callers.api_caller import ApiCaller


class ApiReportDroppedFileRaw(ApiCaller):
    endpoint_url = '/report/$id/dropped-file-raw/$hash'
    endpoint_auth_level = ApiCaller.CONST_API_AUTH_LEVEL_DEFAULT
    request_method_name = ApiCaller.CONST_REQUEST_METHOD_GET
    api_expected_data_type = ApiCaller.CONST_EXPECTED_DATA_TYPE_FILE
