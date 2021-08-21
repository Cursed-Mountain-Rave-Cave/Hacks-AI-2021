import pandas as pd
import app.models as models
from app.services import session_scope, Session


def insert_certificate_isreqsource_type(session: Session):
    certificate_isreqsource_type_df = pd.read_csv(
        "csv/certificate_isreqsource_type.txt", encoding="windows-1251", sep=";"
    )
    certificate_isreqsource_type_df.name = certificate_isreqsource_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateIsreqsourceType,
        map(lambda r: dict(r[1]), certificate_isreqsource_type_df.iterrows()),
    )


def insert_certificate_isrequest_type(session: Session):
    certificate_isrequest_type_df = pd.read_csv(
        "csv/certificate_isrequest_type.txt", encoding="windows-1251", sep=";"
    )
    certificate_isrequest_type_df.name = certificate_isrequest_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateIsrequestType,
        map(lambda r: dict(r[1]), certificate_isrequest_type_df.iterrows()),
    )


def insert_certificate_nature(session: Session):
    certificate_nature_df = pd.read_csv(
        "csv/certificate_nature.txt", encoding="windows-1251", sep=";"
    )
    certificate_nature_df.name = certificate_nature_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateNature,
        map(lambda r: dict(r[1]), certificate_nature_df.iterrows()),
    )


def insert_certificate_protected(session: Session):
    certificate_protected_df = pd.read_csv(
        "csv/certificate_protected.txt", encoding="windows-1251", sep=";"
    )
    certificate_protected_df.name = certificate_protected_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateProtected,
        map(lambda r: dict(r[1]), certificate_protected_df.iterrows()),
    )


def insert_certificate_source(session: Session):
    certificate_source_df = pd.read_csv(
        "csv/certificate_source.txt", encoding="windows-1251", sep=";"
    )
    certificate_source_df.name = certificate_source_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateSource,
        map(lambda r: dict(r[1]), certificate_source_df.iterrows()),
    )


def insert_certificate_status(session: Session):
    certificate_status_df = pd.read_csv(
        "csv/certificate_status.txt", encoding="windows-1251", sep=";"
    )
    certificate_status_df.name = certificate_status_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateStatus,
        map(lambda r: dict(r[1]), certificate_status_df.iterrows()),
    )


def insert_certificate_type(session: Session):
    certificate_type_df = pd.read_csv("csv/certificate_type.txt", encoding="windows-1251", sep=";")
    certificate_type_df.name = certificate_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateType,
        map(lambda r: dict(r[1]), certificate_type_df.iterrows()),
    )


def insert_certificate_vetform(session: Session):
    certificate_vetform_df = pd.read_csv(
        "csv/certificate_vetform.txt", encoding="windows-1251", sep=";"
    )
    certificate_vetform_df.name = certificate_vetform_df.name.str.strip()
    session.bulk_insert_mappings(
        models.CertificateVetform,
        map(lambda r: dict(r[1]), certificate_vetform_df.iterrows()),
    )


def insert_country(session: Session):
    country_df = pd.read_csv("csv/country.txt", encoding="windows-1251", sep=";")
    country_df.name = country_df.name.str.strip()
    country_df.fillna("", inplace=True)
    session.bulk_insert_mappings(
        models.Country,
        map(lambda r: dict(r[1]), country_df.iterrows()),
    )


def insert_federal_district(session: Session):
    federal_district_df = pd.read_csv("csv/federal_district.txt", encoding="windows-1251", sep=";")
    federal_district_df.name = federal_district_df.name.str.strip()
    session.bulk_insert_mappings(
        models.FederalDistrict,
        map(lambda r: dict(r[1]), federal_district_df.iterrows()),
    )


def insert_former(session: Session):
    former_df = pd.read_csv("csv/former.txt", encoding="windows-1251", sep=";")
    former_df.name = former_df.name.str.strip()
    session.bulk_insert_mappings(
        models.Former,
        map(lambda r: dict(r[1]), former_df.iterrows()),
    )


def insert_milk_type(session: Session):
    milk_type_df = pd.read_csv("csv/milk_type.txt", encoding="windows-1251", sep=";")
    milk_type_df.name = milk_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.MilkType,
        map(lambda r: dict(r[1]), milk_type_df.iterrows()),
    )


def insert_product_type(session: Session):
    product_type_df = pd.read_csv("csv/product_type.txt", encoding="windows-1251", sep=";")
    product_type_df.name = product_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.ProductType,
        map(lambda r: dict(r[1]), product_type_df.iterrows()),
    )
    session.bulk_insert_mappings(models.ProductType, [{"id": -1}])


def insert_product(session: Session):
    product_df = pd.read_csv("csv/product.txt", encoding="windows-1251", sep=";")
    product_df.name = product_df.name.str.strip()
    product_df.guid = product_df.guid.str.strip()
    session.bulk_insert_mappings(
        models.Product,
        map(lambda r: dict(r[1]), product_df.iterrows()),
    )


def insert_region(session: Session):
    region_df = pd.read_csv("csv/region.txt", encoding="windows-1251", sep=";")
    region_df.name = region_df.name.str.strip()
    region_df["last"] = region_df["last"].apply(lambda last: int(last == "Y"))
    session.bulk_insert_mappings(
        models.Region,
        map(lambda r: dict(r[1]), region_df.query("last == 1").iterrows()),
    )
    session.bulk_insert_mappings(
        models.Region,
        [{"id": -1, "guid": "00000000-0000-0000-0000-000000000000", "name": ""}],
    )


def insert_sub_product(session: Session):
    sub_product_df = pd.read_csv("csv/sub_product.txt", encoding="windows-1251", sep=";")
    sub_product_df.name = sub_product_df.name.str.strip()
    sub_product_df["last"] = sub_product_df["last"].apply(lambda last: int(last == "Y"))
    session.bulk_insert_mappings(
        models.SubProduct,
        map(lambda r: dict(r[1]), sub_product_df.iterrows()),
    )


def insert_sub_region(session: Session):
    sub_region_df = pd.read_csv("csv/sub_region.txt", encoding="windows-1251", sep=";")
    sub_region_df.name = sub_region_df.name.str.strip()
    session.bulk_insert_mappings(
        models.SubRegion,
        map(lambda r: dict(r[1]), sub_region_df.iterrows()),
    )


def insert_transfer_type(session: Session):
    transfer_type_df = pd.read_csv("csv/transfer_type.txt", encoding="windows-1251", sep=";")
    transfer_type_df.name = transfer_type_df.name.str.strip()
    session.bulk_insert_mappings(
        models.TransferType,
        map(lambda r: dict(r[1]), transfer_type_df.iterrows()),
    )


def insert_unit(session: Session):
    unit_df = pd.read_csv("csv/unit.txt", encoding="windows-1251", sep=";")
    unit_df.name = unit_df.name.str.strip()
    unit_df["last"] = unit_df["last"].apply(lambda last: int(last == "Y"))
    session.bulk_insert_mappings(
        models.Unit,
        map(lambda r: dict(r[1]), unit_df.iterrows()),
    )


def insert_users(session: Session):
    users_df = pd.read_csv("csv/users.txt", encoding="windows-1251", sep=";")
    users_df.name = users_df.name.str.strip()
    session.bulk_insert_mappings(
        models.Users,
        map(lambda r: dict(r[1]), users_df.iterrows()),
    )


if __name__ == "__main__":
    with session_scope() as session:
        insert_certificate_isreqsource_type(session)
        insert_certificate_isrequest_type(session)
        insert_certificate_nature(session)
        insert_certificate_protected(session)
        insert_certificate_source(session)
        insert_certificate_status(session)
        insert_certificate_type(session)
        insert_certificate_vetform(session)
        insert_country(session)
        insert_federal_district(session)
        insert_former(session)
        insert_milk_type(session)
        insert_product_type(session)
        insert_product(session)
        insert_region(session)
        insert_sub_product(session)
        insert_sub_region(session)
        insert_transfer_type(session)
        insert_unit(session)
        insert_users(session)
