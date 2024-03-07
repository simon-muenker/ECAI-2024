import hashlib
import json

import ollama
import tqdm

import config


def generate(model: str, prompt: str):
    return (
        ollama
        .chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                },
            ]
        )
        ['message']
        ['content']
    )


if __name__ == '__main__':
    CFG = config.Config()

    for model in CFG.models:
        for _ in tqdm.tqdm(range(CFG.samples_per_permutation), desc=f'Generating w/ {model}'):
            datapoint: dict = {
                'model': model,
                'response': generate(model, CFG.template.format(topic=CFG.topic)),
            }

            file_name: str = hashlib.shake_256(str.encode(json.dumps(datapoint))).hexdigest(24)
            open(f'{CFG.data_path}/{file_name}.json', 'w').write(json.dumps(datapoint, indent=4))
