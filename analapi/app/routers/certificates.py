from fastapi import APIRouter

from pydantic import BaseModel

class Certificate(BaseModel):
    id: int = 0
    cert_type: str = "Certificate type"
    cert_vetform: str = "Certificate vetform" # Форма сертификата Integer certificate_vetform
    cert_status: str = "Certificate status" # Статус сертификата Integer certificate_status
    cert_nature_type: str = "Certificate nature type" # Вид сертификата Integer certificate_nature
    cert_request_type: str = "Certificate request type" # Сертификат/заявка Integer certificate_isrequest_type
    cert_reqsource_type: str = "Certificate reqsource type" # Происхождение сертификата Integer certificate_isreqsource_type
    consignor_be: str = "Consignor be" # ХС-отправитель Integer business_entity
    consignor_ent: str = "Consignor ent" # Предприятие-отправитель Integer enterprise
    consignee_be: str = "Consignee be" # ХС-получатель Integer business_entity
    consignee_ent: str = "Consegnee ent" # Предприятие-получатель Integer enterprise
    sub_product: str = "Sub product id" # Вид продукции Integer sub_product
    product: str = "Product" # Продукция Integer product
    doctor: str  = "Doctor" # Пользователь, оформивший ВСД Integer users
    unit_guid: str = "Unit guid" # guid единицы измерения String(36) unit
    unit: str = "Unit" # Единица изменения, указанная в ВСД Integer unit
    base_unit: str = "Base unit" # Базовая единица измерения Integer unit
    cert_date: str = "Cert date" # Дата оформления ВСД Timestamp
    cert_insert_date: str = "Cert insert date" # Дата добавления записи в базу Меркурия Timestamp
    weight: str = "Wight" # Объем, в единицах указанных в ВСД Number
    base_weight: str = "Base wight" # Объем, приведенный к базовой единице измерения Number
    consignor_be_region: str = "Consignor be region" # ХС.Отправитель.Субъект РФ Integer region
    consignor_ent_region: str = "Consignor ent region" # Площадка.Отправитель.Субъект РФ Integer region
    consignee_be_region: str = "Consignee be region" # ХС.Получатель.Субъект РФ Integer region
    consignee_ent_region: str = "Consignee ent region" # Площадка.Получатель.Субъект РФ Integer region
    transfer_type: str = "Transfer type" # Тип перемещения Integer transfer_type
    product_type: str = "Product type" # Тип продукции Integer product_type
    cert_source: str = "Cert source" # Источник сертификата Integer certificate_source
    cert_protected: str = "Cert protected" # Защищенность сертификата Integer certificate_protected
    protocol_version: str = "Protocol vertion" # Версия протокола ВетИС.API String(36)
    consignor_be_sub_region: str = "Consignor be sub region" # ХС.Отправитель.Район String(36) SubRegion
    consignee_be_sub_region: str = "Consegnee be sub region" # ХС.Получатель.Район String(36) SubRegion
    consignor_ent_sub_region: str = "Consegnor ent sub region" # Площадка.Отправитель.Район String(36) SubRegion
    consignee_ent_sub_region: str = "Consignee ent sub region" # Площадка.Получатель.Район String(36) SubRegion
    repaid_doctor: str = "Repaid doctor" # Пользователь, погасивший ВСД Integer users
    repaid_cert_date: str = "Repaid cert date" # Дата погашения ВСД Timestamp
    canceled_doctor: str = "Canceled doctor" # Пользователь, погасивший ВСД Integer users
    canceled_cert_date: str = "Canceled cert date" # Дата погашения ВСД Timestamp
    vetExpertise: str = "Vet expertise" # Вет экспертиза Integer vetExpertise
    transit_time_hour: str = "Transit time hour" # Время в часах с момента оформления до погашения BigNumber
    OriginCountry: str = "Origin country" # Страна происхождения String(36) country
    product_name: str = "Product name" # Номенклатура Integer product_name
    former_id: str = "Former" # Тип пользователя, оформившего ВСД Integer former
    RecipientCountry: str = "RecepientCountry" # Страна назначения String(36) country
    milk_attr_fat_min: int = 0 # Массовая доля жира минимальное значение Decimal
    milk_attr_fat_max: int = 0 # Массовая доля жира максимальное значение Decimal
    milk_attr_fat_type: int = 0 # Массовая доля жира тип интервала Integer
    milk_attr_density_min: int = 0 # Плотность минимальное значение Decimal
    milk_attr_density_max: int = 0 # Плотность максимальное значение Decimal
    milk_attr_density_type: int = 0 # Плотность тип интервала Integer
    milk_attr_protein_min: int = 0 # Массовая доля белка минимальное значение Decimal
    milk_attr_protein_max: int = 0 # Массовая доля белка максимальное значение Decimal
    milk_attr_protein_type: int = 0 # Массовая доля белка тип интервала Integer


CERTIFICATES = [
    Certificate(**{
        "id": 1
    }),
    Certificate(**{
        "id": 2
    }),
    Certificate(**{
        "id": 3
    })
]


router = APIRouter()

@router.get("/certificates")
async def get_cerificates():
    return CERTIFICATES;


@router.get("/certificates/{certificate_id}")
async def get_certificate(certificate_id: int):
    return CERTIFICATES[certificate_id]