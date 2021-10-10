import os
import requests
import pandas as pd

import json
import typing as t

import pprint
from pathlib import Path
from pydantic import BaseModel
from urllib.parse import urljoin


class _Config(BaseModel):
    intput_dir: Path
    output_path: Path



class _RawDoc(BaseModel):
    """
    """
    # class _UserQuestion(BaseModel):
    #     count_answer: int
    #     question: t.Optional[str]
        
    company_industry_name: t.Optional[str]
    company_description: t.Optional[str]


# def chunker(seq, size):
#     return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def process_file(path: str) -> t.List[t.Dict]:
    """
    Given a file pointing to presidential_approvals, scan for validation issues
    Returns:
        If every record in the file is valid, we return (True, <validated_data>)
        If there is one invalid record, we return (False, None). This means we're not tolerating
        partial reads, I don't want to bring in that complexity
    """
    csv_rows: t.List[t.Dict[str, str]] = []
    pp = pprint.PrettyPrinter(indent=4)
    try:
        with open(path, 'r',  encoding="utf8") as fp:
            raw = json.load(fp)    

        for i, el in enumerate(raw):
            d = _RawDoc(**el)

            if d.company_industry_name is not None and d.company_description is not None:
                csv_rows.append({
                    "question": d.company_industry_name,
                    "answer": d.company_description,
                })


        
    except Exception as ex:
        print(ex)
        return []

    return csv_rows


# def publish_to_es(validated_data: t.List[ApprovalRatingDoc], config: _Config):
#     """
#     """
#     endpoint = f"/{config.destination_index}"
#     url = urljoin(config.es_host, endpoint)

#     # step 1: create index
#     r = requests.put(url)
#     if not r.ok:
#         raise Exception(f"error: {r.text}")

#     # step 2: iterate through 1-1
#     #         Eventually this will get slow, the _bulk API looks straight forward but will take some dev work to get going
#     #         A bigger problem here is we don't have id's for this sort of dataset. i think this will bite us in the form of accidental duplication, eventually.
#     for i, vd in enumerate(validated_data, config.chunk_size):
#         print(
#             f"processing datum {i} of {len(validated_data)}")

#         endpoint = f"/{config.destination_index}/doc"
#         url = urljoin(config.es_host, endpoint)

#         r = requests.post(
#             url=url,
#             json=vd.dict(),
#         )

#         if not r.ok:
#             raise Exception(f"error: {r.text}")


if __name__ == "__main__":
    config = _Config(
        intput_dir=Path(Path.home(), "data"),
        output_path=Path(Path.home(), "data/transformed/data.csv")
    )

    print(f"Starting glassdoor transformation pipeline")
    all_rows = []

    json_files = [f for f in os.listdir(config.intput_dir)]
    for f in json_files:
        path = Path(config.intput_dir, f)
        file_rows = process_file(path=path)
        for row in file_rows:
            all_rows.append(row)
    
    print(f"We have {len(all_rows)} rows")

    df = pd.DataFrame(all_rows)
    df = df.drop_duplicates()

    df.to_csv(config.output_path, index=False)
