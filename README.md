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

## Trained Models 

We upload the following trained models to huggingface mode hub for easy access and reproducibility: 

| Name                                               | Input | Output | Max Input Len | Max Output Len | Rouge-2 |
| -------------------------------------------------- | ----- | ------ | ------------- | -------------- | ------- |
| **Summarizing Source Documents (Long Models)**     |
| `allenai/led-base-16384-multi_lexsum-source-long`  | `D`   | `L`    | 16384         | 1024           | 25.17   |
| `allenai/led-base-16384-multi_lexsum-source-short` | `D`   | `S`    | 16384         | 256            | 22.08   |
| `allenai/led-base-16384-multi_lexsum-source-tiny`  | `D`   | `T`    | 16384         | 128            | 9.84    |
| `allenai/primera-multi_lexsum-source-long`         | `D`   | `L`    | 4096          | 1024           | 27.32   |
| `allenai/primera-multi_lexsum-source-short`        | `D`   | `S`    | 4096          | 256            | 21.04   |
| `allenai/primera-multi_lexsum-source-tiny`         | `D`   | `T`    | 4096          | 128            | 9.26    |
| **Summarizing Summaries**                          |
| `allenai/bart-large-multi_lexsum-long-short`       | `L`   | `S`    | 1024          | 256            | 37.02   |
| `allenai/bart-large-multi_lexsum-long-tiny`        | `L`   | `T`    | 1024          | 256            | 13.05   |
| `allenai/bart-large-multi_lexsum-short-tiny`       | `S`   | `T`    | 1024          | 128            | 15.20   |
| `allenai/pagesus-multi_lexsum-long-short`          | `L`   | `S`    | 1024          | 256            | 35.62   |
| `allenai/pagesus-multi_lexsum-long-tiny`           | `L`   | `T`    | 1024          | 256            | 14.44   |
| `allenai/pagesus-multi_lexsum-short-tiny`          | `S`   | `T`    | 1024          | 128            | 16.15   |
| **Multi-Task Summarizers**                         |
| `allenai/bart-large-multi_lexsum-source-multitask` | `L`   | `S`    | 1024          | 1024           | -       |
| `allenai/bart-large-multi_lexsum-long-multitask`   | `L`   | `S`    | 1024          | 256            | -       |

Notes:
- In the table above, we use `D` for source documents, `L` for long summary, `S` for short summary, and `T` for tiny summary. 
- For Multi-Task Summarizers, you can prepend the following prompts to signal the model generating summaries of different lengths:
  - `"summarize:long "` for generating long summaries 
  - `"summarize:short "` for generating short summaries 
  - `"summarize:tiny "` for generating tiny summaries 


We also list the pre-trained weights for the used models below:
| Name                                               | Pretrained Weights         |
| -------------------------------------------------- | -------------------------- |
| **Summarizing Source Documents (Long Models)**     |
| `allenai/led-base-16384-multi_lexsum-source-long`  | `allenai/led-base-16384`   |
| `allenai/led-base-16384-multi_lexsum-source-short` | `allenai/led-base-16384`   |
| `allenai/led-base-16384-multi_lexsum-source-tiny`  | `allenai/led-base-16384`   |
| `allenai/primera-multi_lexsum-source-long`         | `allenai/PRIMERA`          |
| `allenai/primera-multi_lexsum-source-short`        | `allenai/PRIMERA`          |
| `allenai/primera-multi_lexsum-source-tiny`         | `allenai/PRIMERA`          |
| **Summarizing Summaries**                          |
| `allenai/bart-large-multi_lexsum-long-short`       | `facebook/bart-large-xsum` |
| `allenai/bart-large-multi_lexsum-long-tiny`        | `facebook/bart-large-xsum` |
| `allenai/bart-large-multi_lexsum-short-tiny`       | `facebook/bart-large-xsum` |
| `allenai/pagesus-multi_lexsum-long-short`          | `google/pegasus-xsum`      |
| `allenai/pagesus-multi_lexsum-long-tiny`           | `google/pegasus-xsum`      |
| `allenai/pagesus-multi_lexsum-short-tiny`          | `google/pegasus-xsum`      |
| **Multi-Task Summarizers**                         |
| `allenai/bart-large-multi_lexsum-source-multitask` | `facebook/bart-large-xsum` |
| `allenai/bart-large-multi_lexsum-long-multitask`   | `facebook/bart-large-xsum` |

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