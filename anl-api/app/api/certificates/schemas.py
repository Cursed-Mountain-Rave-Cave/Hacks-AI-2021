from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class Certificate(BaseModel):
    id: Optional[int]

    cert_type: Optional[str]
    cert_vetform: Optional[str]  # Форма сертификата Integer certificate_vetform
    cert_status: Optional[str]  # Статус сертификата Integer certificate_status
    cert_nature_type: Optional[str]  # Вид сертификата Integer certificate_nature
    cert_request_type: Optional[str]  # Сертификат/заявка Integer certificate_isrequest_type
    cert_reqsource_type: Optional[
        str
    ]  # Происхождение сертификата Integer certificate_isreqsource_type

    consignor_be_id: Optional[str]  # ХС-отправитель Integer business_entity
    consignor_ent_id: Optional[str]  # Предприятие-отправитель Integer enterprise
    consignee_be_id: Optional[str]  # ХС-получатель Integer business_entity
    consignee_ent_id: Optional[str]  # Предприятие-получатель Integer enterprise

    sub_product: Optional[str]  # Вид продукции Integer sub_product
    product: Optional[str]  # Продукция Integer product
    doctor: Optional[str]  # Пользователь, оформивший ВСД Integer users
    unit: Optional[str]  # Единица изменения, указанная в ВСД Integer unit
    cert_date: Optional[datetime]  # Дата оформления ВСД Timestamp
    cert_insert_date: Optional[datetime]  # Дата добавления записи в базу Меркурия Timestamp
    weight: Optional[float]  # Объем, в единицах указанных в ВСД Number

    consignor_be_region: Optional[str]  # ХС.Отправитель.Субъект РФ Integer region
    consignor_ent_region: Optional[str]  # Площадка.Отправитель.Субъект РФ Integer region
    consignee_be_region: Optional[str]  # ХС.Получатель.Субъект РФ Integer region
    consignee_ent_region: Optional[str]  # Площадка.Получатель.Субъект РФ Integer region

    transfer_type: Optional[str]  # Тип перемещения Integer transfer_type
    product_type: Optional[str]  # Тип продукции Integer product_type
    cert_source: Optional[str]  # Источник сертификата Integer certificate_source
    cert_protected: Optional[str]  # Защищенность сертификата Integer certificate_protected
    protocol_version: Optional[str]  # Версия протокола ВетИС.API String(36)

    consignor_be_sub_region: Optional[str]  # ХС.Отправитель.Район String(36) SubRegion
    consignee_be_sub_region: Optional[str]  # ХС.Получатель.Район String(36) SubRegion
    consignor_ent_sub_region: Optional[str]  # Площадка.Отправитель.Район String(36) SubRegion
    consignee_ent_sub_region: Optional[str]  # Площадка.Получатель.Район String(36) SubRegion

    repaid_doctor: Optional[str]  # Пользователь, погасивший ВСД Integer users
    repaid_cert_date: Optional[datetime]  # Дата погашения ВСД Timestamp
    canceled_doctor: Optional[str]  # Пользователь, погасивший ВСД Integer users
    canceled_cert_date: Optional[datetime]  # Дата погашения ВСД Timestamp

    vet_expertise: Optional[int]  # Вет экспертиза Integer vetExpertise
    transit_time_hour: Optional[int]  # Время в часах с момента оформления до погашения BigNumber
    origin_country: Optional[str]  # Страна происхождения String(36) country
    recipient_country: Optional[str]  # Страна назначения String(36) country
    product_name: Optional[str]  # Номенклатура Integer product_name
    former: Optional[str]  # Тип пользователя, оформившего ВСД Integer former

    milk_attr_fat_min: Optional[float]  # Массовая доля жира минимальное значение Decimal
    milk_attr_fat_max: Optional[float]  # Массовая доля жира максимальное значение Decimal
    milk_attr_fat_type: Optional[int]  # Массовая доля жира тип интервала Integer
    milk_attr_density_min: Optional[float]  # Плотность минимальное значение Decimal
    milk_attr_density_max: Optional[float]  # Плотность максимальное значение Decimal
    milk_attr_density_type: Optional[int]  # Плотность тип интервала Integer
    milk_attr_protein_min: Optional[float]  # Массовая доля белка минимальное значение Decimal
    milk_attr_protein_max: Optional[float]  # Массовая доля белка максимальное значение Decimal
    milk_attr_protein_type: Optional[int]  # Массовая доля белка тип интервала Integer
