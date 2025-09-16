# app/core/preprocessing.py

import pandas as pd
from app.schemas.prediction import PredictionInput

# These mappings are derived from the original dataset and the LabelEncoder logic.
# They MUST match the encoding used during model training.
# The LabelEncoder sorts values alphabetically before assigning integers.

ITEM_FAT_CONTENT_MAP = {'Low Fat': 0, 'Regular': 1}
ITEM_CATEGORY_MAP = {'DR': 0, 'FD': 1, 'NC': 2}
OUTLET_SIZE_MAP = {'High': 0, 'Medium': 1, 'Small': 2}
OUTLET_LOCATION_TYPE_MAP = {'Tier 1': 0, 'Tier 2': 1, 'Tier 3': 2}

ITEM_TYPE_MAP = {
    'Baking Goods': 0, 'Breads': 1, 'Breakfast': 2, 'Canned': 3, 'Dairy': 4,
    'Frozen Foods': 5, 'Fruits and Vegetables': 6, 'Hard Drinks': 7,
    'Health and Hygiene': 8, 'Household': 9, 'Meat': 10, 'Others': 11,
    'Seafood': 12, 'Snack Foods': 13, 'Soft Drinks': 14, 'Starchy Foods': 15
}

OUTLET_IDENTIFIER_MAP = {
    'OUT010': 0, 'OUT013': 1, 'OUT017': 2, 'OUT018': 3, 'OUT019': 4,
    'OUT027': 5, 'OUT035': 6, 'OUT045': 7, 'OUT046': 8, 'OUT049': 9
}

OUTLET_TYPE_MAP = {
    'Grocery Store': 0, 'Supermarket Type1': 1,
    'Supermarket Type2': 2, 'Supermarket Type3': 3
}


def preprocess_input(input_data: PredictionInput) -> pd.DataFrame:
    """
    Transforms raw input data from the API into a pandas DataFrame
    with the correct encoding for model prediction.
    """
    # Convert Pydantic model to a dictionary
    data = input_data.model_dump()

    # Apply all the mappings to convert categorical strings to integers
    data['Item_Fat_Content'] = ITEM_FAT_CONTENT_MAP[data['Item_Fat_Content']]
    data['Item_Category'] = ITEM_CATEGORY_MAP[data['Item_Category']]
    data['Outlet_Size'] = OUTLET_SIZE_MAP[data['Outlet_Size']]
    data['Outlet_Location_Type'] = OUTLET_LOCATION_TYPE_MAP[data['Outlet_Location_Type']]
    data['Item_Type'] = ITEM_TYPE_MAP[data['Item_Type']]
    data['Outlet_Identifier'] = OUTLET_IDENTIFIER_MAP[data['Outlet_Identifier']]
    data['Outlet_Type'] = OUTLET_TYPE_MAP[data['Outlet_Type']]

    # Create a pandas DataFrame from the processed dictionary
    df = pd.DataFrame([data])

    # Ensure the column order matches the order used during model training
    # This is crucial for the model to work correctly.
    expected_columns = [
        'Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
        'Item_MRP', 'Outlet_Identifier', 'Outlet_Establishment_Year',
        'Outlet_Size', 'Outlet_Location_Type', 'Outlet_Type', 'Item_Category'
    ]
    df = df[expected_columns]

    return df
