from domain.entites.rate import RateEntity
from infra.repositories.models.rate import RateModel


def convert_rate_to_dict(rate_entity: RateEntity):
    return {
        "cargo_type": rate_entity.cargo_type,
        "rate": rate_entity.rate,
        "date": rate_entity.date
    }


def convert_rate_model_to_entity(rate_model: RateModel) -> RateEntity:
    return RateEntity(id=rate_model.id,
                      cargo_type=rate_model.cargo_type,
                      rate=rate_model.rate,
                      date=rate_model.date)
