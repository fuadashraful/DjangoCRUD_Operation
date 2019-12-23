# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Position,Employee
from django.contrib import admin

# Register your models here.
admin.site.register(Employee)
admin.site.register(Position)