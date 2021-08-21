from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.util import aliased
import app.models as m


def get_certificate_query_base(session: Session) -> Query:
    Doctor = aliased(m.Users)
    RepaidDoctor = aliased(m.Users)
    CanceledDoctor = aliased(m.Users)

    ConsignorBeRegion = aliased(m.Region)
    ConsignorEntRegion = aliased(m.Region)
    ConsigneeBeRegion = aliased(m.Region)
    ConsigneeEntRegion = aliased(m.Region)

    ConsignorBeSubRegion = aliased(m.SubRegion)
    ConsignorEntSubRegion = aliased(m.SubRegion)
    ConsigneeBeSubRegion = aliased(m.SubRegion)
    ConsigneeEntSubRegion = aliased(m.SubRegion)

    OriginCountry = aliased(m.Country)
    RecepientCountry = aliased(m.Country)

    return (
        session.query(
            m.Certificate.id.label("id"),
            m.CertificateType.name.label("cert_type"),
            m.CertificateVetform.name.label("cert_vetform"),
            m.CertificateStatus.name.label("cert_status"),
            m.CertificateNature.name.label("cert_nature_type"),
            m.CertificateIsrequestType.name.label("cert_request_type"),
            m.CertificateIsreqsourceType.name.label("cert_reqsource_type"),
            m.Certificate.consignor_be_id.label("consignor_be_id"),
            m.Certificate.consignor_ent_id.label("consignor_ent_id"),
            m.Certificate.consignee_be_id.label("consignee_be_id"),
            m.Certificate.consignee_ent_id.label("consignee_ent_id"),
            m.SubProduct.name.label("sub_product"),
            m.Product.name.label("product"),
            Doctor.name.label("doctor"),
            m.Unit.name.label("unit"),
            m.Certificate.cert_date.label("cert_date"),
            m.Certificate.cert_insert_date.label("cert_insert_date"),
            m.Certificate.weight.label("weight"),
            ConsignorBeRegion.name.label("consignor_be_region"),
            ConsignorEntRegion.name.label("consignor_ent_region"),
            ConsigneeBeRegion.name.label("consignee_be_region"),
            ConsigneeEntRegion.name.label("consignee_ent_region"),
            m.TransferType.name.label("transfer_type"),
            m.ProductType.name.label("product_type"),
            m.CertificateSource.name.label("cert_source"),
            m.CertificateProtected.name.label("cert_protected"),
            m.Certificate.protocol_version.label("protocol_version"),
            ConsignorBeSubRegion.name.label("consignor_be_sub_region"),
            ConsignorEntSubRegion.name.label("consignor_ent_sub_region"),
            ConsigneeBeSubRegion.name.label("consignee_be_sub_region"),
            ConsigneeEntSubRegion.name.label("consignee_ent_sub_region"),
            RepaidDoctor.name.label("repaid_doctor"),
            m.Certificate.repair_cert_date.label("repaid_cert_date"),
            CanceledDoctor.name.label("canceled_doctor"),
            m.Certificate.canceled_cert_date.label("canceled_cert_date"),
            m.Certificate.vet_expertice.label("vet_expertise"),
            m.Certificate.transit_time_hour.label("transit_time_hour"),
            OriginCountry.name.label("origin_country"),
            RecepientCountry.name.label("recepient_country"),
            m.ProductName.name.label("product_name"),
            m.Former.name.label("former"),
            m.Certificate.milk_attr_fat_min.label("milk_attr_fat_min"),
            m.Certificate.milk_attr_fat_max.label("milk_attr_fat_max"),
            m.Certificate.milk_attr_fat_type.label("milk_attr_fat_type"),
            m.Certificate.milk_attr_density_min.label("milk_attr_density_min"),
            m.Certificate.milk_attr_density_max.label("milk_attr_density_max"),
            m.Certificate.milk_attr_density_type.label("milk_attr_density_type"),
            m.Certificate.milk_attr_protein_min.label("milk_attr_protein_min"),
            m.Certificate.milk_attr_protein_max.label("milk_attr_protein_max"),
            m.Certificate.milk_attr_protein_type.label("milk_attr_protein_type"),
        )
        .outerjoin(m.CertificateType)
        .outerjoin(m.CertificateVetform)
        .outerjoin(m.CertificateStatus)
        .outerjoin(m.CertificateNature)
        .outerjoin(m.CertificateIsrequestType)
        .outerjoin(m.CertificateIsreqsourceType)
        .outerjoin(m.SubProduct)
        .outerjoin(m.Product)
        .outerjoin(Doctor, Doctor.id == m.Certificate.doctor_id)
        .outerjoin(m.Unit, m.Certificate.unit_id == m.Unit.id)
        .outerjoin(ConsignorBeRegion, ConsignorBeRegion.id == m.Certificate.consignor_be_region_id)
        .outerjoin(
            ConsignorEntRegion, ConsignorEntRegion.id == m.Certificate.consignor_ent_region_id
        )
        .outerjoin(ConsigneeBeRegion, ConsigneeBeRegion.id == m.Certificate.consignee_be_region_id)
        .outerjoin(
            ConsigneeEntRegion, ConsigneeEntRegion.id == m.Certificate.consignee_ent_region_id
        )
        .outerjoin(m.TransferType)
        .outerjoin(m.ProductType, m.ProductType.id == m.Certificate.product_type_id)
        .outerjoin(m.CertificateSource)
        .outerjoin(m.CertificateProtected)
        .outerjoin(
            ConsignorBeSubRegion,
            ConsignorBeSubRegion.guid == m.Certificate.consignor_be_sub_region_guid,
        )
        .outerjoin(
            ConsignorEntSubRegion,
            ConsignorEntSubRegion.guid == m.Certificate.consignor_ent_sub_region_guid,
        )
        .outerjoin(
            ConsigneeBeSubRegion,
            ConsigneeBeSubRegion.guid == m.Certificate.consignee_be_sub_region_guid,
        )
        .outerjoin(
            ConsigneeEntSubRegion,
            ConsigneeEntSubRegion.guid == m.Certificate.consignee_ent_sub_region_guid,
        )
        .outerjoin(
            OriginCountry,
            OriginCountry.guid == m.Certificate.guid_origin_country,
        )
        .outerjoin(
            RecepientCountry,
            RecepientCountry.guid == m.Certificate.guid_recepient_country,
        )
        .outerjoin(RepaidDoctor, RepaidDoctor.id == m.Certificate.repaid_doctor_id)
        .outerjoin(CanceledDoctor, CanceledDoctor.id == m.Certificate.repaid_doctor_id)
        .outerjoin(m.ProductName, m.ProductName.id == m.Certificate.product_name_id)
        .outerjoin(m.Former)
    )
