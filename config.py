import dataclasses
import pathlib
import typing


@dataclasses.dataclass
class Config:
    version: str = '0.0.2'

    template_path: str = './template.txt'
    final_dataset_path: str = './data/dataset'

    raw_data_dir: str = './data/raw'

    topic: str = 'Protecting of personal information regarding data privacy'
    models: typing.List[str] = dataclasses.field(default_factory=lambda: [
        'llama2:70b', 'mixtral:8x7b', 'falcon:40b', 'qwen:72b'
    ])

    samples_per_permutation: int = 30
    n_grams_analysis: int = 1

    def __post_init__(self):
        self.template: str = open(self.template_path).read().strip()

        self.raw_data_dir = f'{self.raw_data_dir}/{self.version}'
        self.final_dataset_path = f'{self.final_dataset_path}-{self.version}'

        pathlib.Path(self.raw_data_dir).mkdir(parents=True, exist_ok=True)
