from sparv.api import Config
from . import sentence_bert

__config__ = [
    Config(
        "sentence_bert.model",
        description="KBLabs sentence transformers model",
        default="KBLab/sentence-bert-swedish-cased",
        ),
    Config(
        "sentence_bert.all_model",
        description="Sentence transformers main model",
        default="all-mpnet-base-v2"
    )
]