import dataclasses
import pathlib
import typing


@dataclasses.dataclass
class Config:
    template_path: str = './template.txt'
    data_path: str = './data/raw'

    topic: str = 'Protecting of personal information regarding data privacy'
    models: typing.List[str] = dataclasses.field(default_factory=lambda: ['tinyllama'])

    samples_per_permutation: int = 30

    def __post_init__(self):
        self.template: str = open(self.template_path).read().strip()

        pathlib.Path(self.data_path).mkdir(parents=True, exist_ok=True)
