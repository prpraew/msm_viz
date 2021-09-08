#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from kedro.pipeline import Pipeline, node

from .nodes import preprocess_companies, preprocess_shuttles

from .nodes import create_model_input_table, preprocess_companies, preprocess_shuttles

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs=["companies","company_names"],
                outputs="preprocessed_companies",
                name="preprocess_companies_node",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocess_shuttles_node",
            ),
            node(
                func=create_model_input_table,
                inputs=["preprocessed_shuttles", "preprocessed_companies", "reviews"],
                outputs="model_input_table",
                name="create_model_input_table_node",
            ),
        ]
    )

