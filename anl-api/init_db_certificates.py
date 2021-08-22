import random
from datetime import datetime, timedelta
import pandas as pd
import app.models as models
from app.services import session_scope, Session


def parse_datetime(d: str) -> datetime:
    if d is None:
        return None
    return datetime.strptime(d.split(".")[0], r"%Y/%m/%d %H:%M:%S")


def prepare_dict(data: pd.Series) -> dict:
    d = dict(data)

    d = {k: v if v == v else None for k, v in d.items()}
    d["product_name_id"] = None

    cert_date = datetime(2020, 1, 15) + timedelta(
        random.randint(0, 200), random.randint(0, 24 * 3600)
    )

    cert_insert_date = cert_date + timedelta(0, random.randint(-30, 3596))
    if d["canceled_cert_date"] is not None:
        canceled_cert_date = min(
            datetime(2021, 5, 11, 11, 6, 52),
            cert_date + (parse_datetime(d["canceled_cert_date"]) - parse_datetime(d["cert_date"])),
        )
    else:
        canceled_cert_date = None

    if d["repair_cert_date"] is not None:
        repair_cert_date = min(
            datetime(2021, 5, 11, 11, 6, 52),
            cert_date + (parse_datetime(d["repair_cert_date"]) - parse_datetime(d["cert_date"])),
        )
    else:
        repair_cert_date = None

    d["cert_date"] = cert_date
    d["cert_insert_date"] = cert_insert_date
    d["canceled_cert_date"] = canceled_cert_date
    d["repair_cert_date"] = repair_cert_date

    return d


def insert_certificates_head(session: Session):
    certificates_head_df = pd.read_csv("csv/certificates_head.csv", sep=";")
    session.query(models.CertificateScore).delete()
    session.query(models.Certificate).delete()
    session.bulk_insert_mappings(
        models.Certificate,
        map(lambda r: prepare_dict(r[1]), certificates_head_df.iterrows()),
    )


if __name__ == "__main__":
    with session_scope() as session:
        insert_certificates_head(session)
