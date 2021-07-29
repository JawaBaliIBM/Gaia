import nltk
import re

import pandas as pd
import numpy as np


def replace_newlines_with_space(text):
    return re.sub("\n+", " ", text)


def sanitize_tokenized_sentences(sentences):
    return [replace_newlines_with_space(s) for s in sentences]


def clean_dataset_entities(filename):
    df = pd.read_json(filename)
    df = df[df.brand_entities.astype(bool)]

    df["article"] = df["article"].apply(replace_newlines_with_space)

    clean_filename = filename.replace(".csv", "-clean.csv")
    df.to_csv(clean_filename)
    return clean_filename


def get_entities_in_paragraph(brand_entities, paragraph):
    entities = []
    for brand_entity in brand_entities:
        if brand_entity["text"] in paragraph:
            entities.append(brand_entity["text"])

    return entities


def get_row_for_split_paragraph(row):
    article_split_by_paragraph = sanitize_tokenized_sentences(nltk.sent_tokenize(row["article"]))
    url = row["url"]
    return [
        {
            "paragraph": paragraph,
            "brand_entities": ", ".join(get_entities_in_paragraph(row["brand_entities"], paragraph)),
            "url": url
        }
    for paragraph in article_split_by_paragraph]


def split_by_paragraph(filename):
    df = pd.read_json(filename)
    df = df[df.brand_entities.astype(bool)]

    df_split_by_paragraph = pd.concat([pd.DataFrame(get_row_for_split_paragraph(row))             
                for _, row in df.iterrows()]).reset_index()

    df_split_by_paragraph = df_split_by_paragraph[df_split_by_paragraph.brand_entities.astype(bool)]

    split_filename = filename.replace(".csv", "-by-paragraph.csv")
    df_split_by_paragraph.to_csv(split_filename, index=False)
    return split_filename

# clean_dataset_entities()
# split_by_paragraph()