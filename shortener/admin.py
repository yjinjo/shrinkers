from django.contrib import admin

from shortener.models import PayPlan, Users, Statistic

admin.site.register(PayPlan)
admin.site.register(Users)
admin.site.register(Statistic)
