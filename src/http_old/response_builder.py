# import os
# from pandas import DataFrame

# API_ENVIRONMENT = os.getenv("ENVIRONMENT")


# # MARK: Response Builder - Final
# def response_builder(df: DataFrame | None = None, query: str = "") -> dict:
#     """_summary_: This function builds a response dictionary for an API endpoint. It takes in a type, data, and status code and returns a dictionary."""
#     if API_ENVIRONMENT != "PROD":  # DEV or TEST
#         return {
#             "query": query,
#             "data": df.to_json(orient="records") if df is not None else "nothing",
#         }
#     else:  # PROD
#         return {
#             "data": df.to_json(orient="records") if df is not None else "nothing",
#         }
