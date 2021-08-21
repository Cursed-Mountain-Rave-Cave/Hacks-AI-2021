import pandas as pd
import app.models as models
from app.services import session_scope, Session


def prepare_dict(data: pd.Series) -> dict:
    d = dict(data)

    d = {k: v if v == v else None for k, v in d.items()}
    d["product_name_id"] = None

    return d


def insert_certificates_head(session: Session):
    certificates_head_df = pd.read_csv("csv/certificates_head.csv", sep=";")
    session.bulk_insert_mappings(
        models.Certificate,
        map(lambda r: prepare_dict(r[1]), certificates_head_df.iterrows()),
    )


if __name__ == "__main__":
    with session_scope() as session:
        insert_certificates_head(session)
