import json
import os
from pandas import DataFrame

API_ENVIRONMENT: str | None = os.getenv(key="ENVIRONMENT")

# MARK: Response Builder
def response_builder(df: DataFrame | None = None) -> str:
    data = df.to_json(orient="records") if df is not None else "nothing"
    return data