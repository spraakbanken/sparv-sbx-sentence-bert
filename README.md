# Sparv-sbx-sentence-bert
Sparv plugin to generate document vectors using KBLab sentence transformers


## Installation

### Sparv pipeline

Sparv pipeline is a text analysis tool developed by [`Språkbanken Text`](https://spraakbanken.gu.se/) and can be installed using the command:

```bash
pip install sparv-pipeline
```

### Sentence BERT plugin

This plugin uses the sentence-transformers model developed by [`KBLab`](https://kb-labb.github.io/posts/2021-08-23-a-swedish-sentence-transformer/) to generate 768 dimensional dense vector for the given text. 

Use the command below to install the plugin:

```bash
pip install git+https://github.com/spraakbanken/sparv-sbx-sentence-bert
```

## Usage

Currently, the plugin can be used to generate dense vector for sentences, paragraphs and texts. To use it together with other annotations you need to add the below configuration to the `config.yaml` under the `export` section.

```yaml
# Dense vector on text level
export:
    annotations:
        - <text>:sentence_bert.vector
        ...
```
```yaml
# Dense vector on paragraph level
export:
    annotations:
        - <paragraph>:sentence_bert.vector
        ...
```
```yaml
# Dense vector on sentence level
export:
    annotations:
        - <sentence>:sentence_bert.vector
        ...
```

## Model
[`KBLab/sentence-bert-swedish-cased`](https://huggingface.co/KBLab/sentence-bert-swedish-cased)














