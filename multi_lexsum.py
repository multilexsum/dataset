from typing import List, Union, Dict, Any, Tuple
import json
import os

import datasets
from datasets.tasks import Summarization

logger = datasets.logging.get_logger(__name__)


def _load_jsonl(filename):
    with open(filename, "r") as fp:
        jsonl_content = fp.read()

    result = [json.loads(jline) for jline in jsonl_content.splitlines()]
    return result


def _load_json(filepath):

    with open(filepath, "r") as fp:
        res = json.load(fp)
    return res


_CITATION = """
"""  # TODO

_DESCRIPTION = """
Multi-LexSum is a multi-doc summarization dataset for civil rights litigation lawsuits with summaries of three granularities. 
"""  # TODO: Update with full abstract 

_HOMEPAGE = "https://multilexsum.github.io"

_BASE_URL = "https://ai2-s2-research.s3.us-west-2.amazonaws.com/multilexsum/releases"
_FILES = {
    "train": "train.json",
    "dev": "dev.json",
    "test": "test.json",
    "sources": "sources.json",
}


class MultiLexsumConfig(datasets.BuilderConfig):
    """BuilderConfig for LexSum."""

    def __init__(self, **kwargs):
        """BuilderConfig for LexSum.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(MultiLexsumConfig, self).__init__(**kwargs)


class MultiLexsum(datasets.GeneratorBasedBuilder):
    """MultiLexSum Dataset: a multi-doc summarization dataset for 
    civil rights litigation lawsuits with summaries of three granularities. 
    """

    BUILDER_CONFIGS = [
        MultiLexsumConfig(
            name="v20220616",
            version=datasets.Version("1.0.0", "Public v1.0 release."),
            description="The v1.0 Multi-LexSum dataset",
        ),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "sources": datasets.Sequence(datasets.Value("string")),
                    "summary/long": datasets.Value("string"),
                    "summary/short": datasets.Value("string"),
                    "summary/tiny": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
            homepage=_HOMEPAGE,
            citation=_CITATION,
            task_templates=[
                Summarization(text_column="source", summary_column="summary/long")
            ],
        )

    def _split_generators(self, dl_manager):

        base_url = _BASE_URL if self.config.data_dir is None else self.config.data_dir
        downloaded_files = dl_manager.download_and_extract(
            {
                name: f"{base_url}/{self.config.name}/{filename}"
                for name, filename in _FILES.items()
            }
        )
        # Given sources is a large file, we read it first
        sources = _load_json(downloaded_files["sources"])

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                gen_kwargs={
                    "subset_file": downloaded_files["train"],
                    "sources": sources,
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                gen_kwargs={
                    "subset_file": downloaded_files["dev"],
                    "sources": sources,
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                gen_kwargs={
                    "subset_file": downloaded_files["test"],
                    "sources": sources,
                },
            ),
        ]

    def _generate_examples(self, subset_file: str, sources: Dict[str, Dict]):
        """This function returns the examples in the raw (text) form."""
        logger.info(f"generating examples from = {subset_file}")

        subset_cases = _load_jsonl(subset_file)
        for case_data in subset_cases:
            case_sources = [
                sources[source_id]["doc_text"]
                for source_id in case_data["case_documents"]
            ]
            yield case_data["case_id"], {
                "id": case_data["case_id"],
                "sources": case_sources,
                "summary/long": case_data["summary/long"],
                "summary/short": case_data["summary/short"],
                "summary/tiny": case_data["summary/tiny"],
            }