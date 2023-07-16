from datetime import datetime
import json

from app.core.config import settings
from app.services.database.models.rates import Rates


async def load_rates():
    with open(settings.BASE_DIR + '/rates.json') as f:
        rates = json.load(f)
        for k, v in rates.items():
            rate_date = datetime.strptime(k, '%Y-%m-%d')
            for rate_value in v:
                rate_value.update({'date': rate_date})
                await Rates.get_or_create(**rate_value)
