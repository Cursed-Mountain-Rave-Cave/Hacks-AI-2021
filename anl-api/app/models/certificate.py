from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import BigInteger, DateTime, Float, Integer, String
from .base import Base
from .certificate_type import CertificateType
from .certificate_vetform import CertificateVetform
from .certificate_status import CertificateStatus
from .certificate_nature import CertificateNature
from .certificate_isrequest_type import CertificateIsrequestType
from .certificate_isreqsource_type import CertificateIsreqsourceType
from .product import Product
from .sub_product import SubProduct
from .users import Users
from .unit import Unit
from .region import Region
from .transfer_type import TransferType
from .product_type import ProductType
from .product_name import ProductName
from .certificate_source import CertificateSource
from .certificate_protected import CertificateProtected
from .sub_region import SubRegion
from .country import Country
from .former import Former


class Certificate(Base):
    __tablename__ = "certificate"

    id = Column(Integer, primary_key=True)
    cert_type_id = Column(ForeignKey(CertificateType.id))
    cert_vetform_id = Column(ForeignKey(CertificateVetform.id))
    cert_status_id = Column(ForeignKey(CertificateStatus.id))
    cert_nature_type_id = Column(ForeignKey(CertificateNature.id))
    cert_request_type_id = Column(ForeignKey(CertificateIsrequestType.id))
    cert_reqsource_type_id = Column(ForeignKey(CertificateIsreqsourceType.id))
    consignor_be_id = Column(Integer)
    consignor_ent_id = Column(Integer)
    consignee_be_id = Column(Integer)
    consignee_ent_id = Column(Integer)
    sub_product_id = Column(ForeignKey(SubProduct.id))
    product_id = Column(ForeignKey(Product.id))
    doctor_id = Column(ForeignKey(Users.id))
    unit_id = Column(ForeignKey(Unit.id))
    base_unit_id = Column(ForeignKey(Unit.id))
    cert_date = Column(DateTime)
    cert_insert_date = Column(DateTime)
    weight = Column(Float)
    base_weight = Column(Float)
    consignor_be_region_id = Column(ForeignKey(Region.id))
    consignor_ent_region_id = Column(ForeignKey(Region.id))
    consignee_be_region_id = Column(ForeignKey(Region.id))
    consignee_ent_region_id = Column(ForeignKey(Region.id))
    transfer_type_id = Column(ForeignKey(TransferType.id))
    product_type_id = Column(ForeignKey(ProductType.id))
    cert_source_id = Column(ForeignKey(CertificateSource.id))
    cert_protected_id = Column(ForeignKey(CertificateProtected.id))
    protocol_version = Column(String(36))
    consignor_be_sub_region_guid = Column(ForeignKey(SubRegion.guid))
    consignor_ent_sub_region_guid = Column(ForeignKey(SubRegion.guid))
    consignee_be_sub_region_guid = Column(ForeignKey(SubRegion.guid))
    consignee_ent_sub_region_guid = Column(ForeignKey(SubRegion.guid))
    repaid_doctor_id = Column(ForeignKey(Users.id))
    repair_cert_date = Column(DateTime)
    canceled_doctor_id = Column(ForeignKey(Users.id))
    canceled_cert_date = Column(DateTime)
    vet_expertice = Column(Integer)
    transit_time_hour = Column(BigInteger)
    guid_origin_country = Column(ForeignKey(Country.guid))
    product_name_id = Column(ForeignKey(ProductName.id))
    former_id = Column(ForeignKey(Former.id))
    guid_recepient_country = Column(ForeignKey(Country.guid))
    milk_attr_fat_min = Column(Float)
    milk_attr_fat_max = Column(Float)
    milk_attr_fat_type = Column(Integer)
    milk_attr_density_min = Column(Float)
    milk_attr_density_max = Column(Float)
    milk_attr_density_type = Column(Integer)
    milk_attr_protein_min = Column(Float)
    milk_attr_protein_max = Column(Float)
    milk_attr_protein_type = Column(Integer)
