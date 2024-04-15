import dataclasses
import json
import pathlib
import typing


@dataclasses.dataclass
class Config:
    version: str = '0.0.3'

    template_path: str = './template.txt'
    questionary_path: str = './questionary.json'

    dataset_name: str = 'dataset'
    data_dir: str = './data'
    report_dir: str = './report'

    topic: str = 'Protecting of personal information regarding data privacy'

    models: typing.List[str] = dataclasses.field(default_factory=lambda: [
        'llama2:70b-chat-q6_K',
        'falcon:40b-instruct-q5_1',
        'mixtral:8x7b-instruct-v0.1-q6_K',
        'qwen:72b-chat-v1.5-q6_K'
    ])

    samples_per_permutation: int = 3500
    n_grams_analysis: int = 1

    def __post_init__(self):
        self.template: str = open(self.template_path).read().strip()

        self.data_dir = f'{self.data_dir}/{self.version}'
        self.data_raw_dir = f'{self.data_dir}/raw'
        self.report_dir = f'{self.report_dir}/{self.version}'

        pathlib.Path(self.data_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.data_raw_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(self.report_dir).mkdir(parents=True, exist_ok=True)

        self.questionary: typing.Dict = json.loads(open(self.questionary_path).read())
