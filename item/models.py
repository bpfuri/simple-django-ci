# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
