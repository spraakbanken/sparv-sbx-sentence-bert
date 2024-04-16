from sparv.api import Annotation, Output, annotator, get_logger, Text, Config, modelbuilder

from sentence_transformers import SentenceTransformer

MODEL_NAME_ALL = "all-mpnet-base-v2"
MODEL_NAME_SWE = "KBLab/sentence-bert-swedish-cased"

logger = get_logger(__name__)


@annotator("Document vector using BERT sentence transformers")
def vectorize_full_text(
        corpus_text: Text = Text(),
        texts: Annotation = Annotation("{chunk}"),
        out: Output = Output("{chunk}:sentence_bert.vector"),
        model: str = Config("sentence_bert.model")
):
    corpus_text = corpus_text.read()
    text_spans = texts.read_spans()
    result = []
    vectorHandler = VectorData(model=model)
    for span in text_spans:
        doc = corpus_text[span[0]:span[1]]
        vectors = vectorHandler.run(doc=doc)
        result.append(str(vectors))
        logger.progress()

    out.write(result)


class DocHandler:
    def __init__(self, path):
        self.path = path

    def read_doc(self):
        with open(self.path, 'r') as file:
            return file.read()

class VectorData:
    def __init__(self, model):
        self.model = model

    def run(self, doc: str):
        model_swe = SentenceTransformer(self.model)
        return model_swe.encode(doc)
