# app/schemas/prediction.py

from pydantic import BaseModel, Field
from typing import Literal

# This schema defines the structure for a single prediction request.
# FastAPI uses this for validation and documentation.
# The 'example' values will be shown in the interactive API docs (Swagger UI).
class PredictionInput(BaseModel):
    Item_Weight: float = Field(..., example=9.3)
    Item_Fat_Content: Literal['Low Fat', 'Regular'] = Field(..., example='Low Fat')
    Item_Visibility: float = Field(..., example=0.016047)
    Item_Type: Literal[
        'Baking Goods', 'Breads', 'Breakfast', 'Canned', 'Dairy', 'Frozen Foods',
        'Fruits and Vegetables', 'Hard Drinks', 'Health and Hygiene', 'Household',
        'Meat', 'Others', 'Seafood', 'Snack Foods', 'Soft Drinks', 'Starchy Foods'
    ] = Field(..., example='Snack Foods')
    Item_MRP: float = Field(..., example=249.8092)
    Outlet_Identifier: Literal[
        'OUT010', 'OUT013', 'OUT017', 'OUT018', 'OUT019', 'OUT027',
        'OUT035', 'OUT045', 'OUT046', 'OUT049'
    ] = Field(..., example='OUT049')
    Outlet_Establishment_Year: int = Field(..., example=1999)
    Outlet_Size: Literal['High', 'Medium', 'Small'] = Field(..., example='Medium')
    Outlet_Location_Type: Literal['Tier 1', 'Tier 2', 'Tier 3'] = Field(..., example='Tier 1')
    Outlet_Type: Literal[
        'Grocery Store', 'Supermarket Type1', 'Supermarket Type2', 'Supermarket Type3'
    ] = Field(..., example='Supermarket Type1')
    Item_Category: Literal['DR', 'FD', 'NC'] = Field(..., example='FD')

# This schema defines the structure of the prediction response.
class PredictionOutput(BaseModel):
    prediction: float
