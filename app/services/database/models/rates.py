from tortoise.models import Model
from tortoise import fields


class Rates(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField(null=False)
    rate = fields.DecimalField(max_digits=10, decimal_places=4)
    cargo_type = fields.CharField(max_length=100)

    class Meta:
        unique_together = [('date', 'cargo_type')]
