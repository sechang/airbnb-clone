from django.db import models


class TimeStampedModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """ 이걸 넣으므로, 해당 모델이 데이터 베이스에 들어가지 않게 함 = 추상모델"""

        abstract = True