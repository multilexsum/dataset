# Multi-LexSum: Real-world Summaries of Civil Rights Lawsuits at Multiple Granularities

<a href="https://arxiv.org/abs/2206.10883"><img src="https://img.shields.io/badge/arXiv-2206.10883-b31b1b.svg" title="Multi-LexSum Paper"></a>

Multi-LexSum is a multi-doc summarization dataset for civil rights litigation lawsuits with summaries of three granularities. 

**Update: Multi-LexSum is now on HuggingFace Datasets Hub! Check [allenai/multi_lexsum](https://huggingface.co/datasets/allenai/multi_lexsum).**

## Quick Start 

```python
from datasets import load_dataset
# please install HuggingFace datasets by pip install datasets 

multi_lexsum = load_dataset("allenai/multi_lexsum", name="v20220616")
# Download multi_lexsum locally and load it as a Dataset object 

example = multi_lexsum["validation"][0] # The first instance of the dev set 
example["sources"] # A list of source document text for the case

for sum_len in ["long", "short", "tiny"]:
    print(example["summary/" + sum_len]) # Summaries of three lengths
```
You can start using the dataset via the provided [example.ipynb](example.ipynb). 

## License 

The Multi-LexSum dataset is distributed under the [Open Data Commons Attribution License (ODC-By)](https://opendatacommons.org/licenses/by/1-0/). 
The case summaries and metadata are licensed under the [Creative Commons Attribution License (CC BY-NC)](https://creativecommons.org/licenses/by-nc/4.0/), and the source documents are already in the public domain. 
Commercial users who desire a license for summaries and metadata can contact [info@clearinghouse.net](mailto:info@clearinghouse.net), which will allow free use but limit summary re-posting. 
The corresponding code for downloading and loading the dataset is licensed under the Apache License 2.0. 

## Reference 

```
@article{Shen2022MultiLexSum,
  author    = {Zejiang Shen and
               Kyle Lo and
               Lauren Yu and
               Nathan Dahlberg and
               Margo Schlanger and
               Doug Downey},
  title     = {Multi-LexSum: Real-World Summaries of Civil Rights Lawsuits at Multiple Granularities},
  journal   = {CoRR},
  volume    = {abs/2206.10883},
  year      = {2022},
  url       = {https://doi.org/10.48550/arXiv.2206.10883},
  doi       = {10.48550/arXiv.2206.10883}
}
```