from odoo import fields, models,api
from odoo.exceptions import UserError

from uuid import uuid4
import qrcode
import base64
import logging

from lxml import etree

from odoo import fields, models
import requests
import json
from datetime import datetime,date
import convert_numbers


class AccountMove(models.Model):
    _inherit = 'account.move'


    def amount_tax_per(self):
        tax_amount =  self.amount_untaxed - float(self.advance) - float(self.discount_value)
        value = tax_amount * 0.15
        return value
    def amount_net_amount(self):
        net_amount = self.amount_untaxed - float(self.advance) - float(self.discount_value)
        return convert_numbers.english_to_arabic(int(net_amount))

    def amount_tax_per_arabic(self):
        m= self.amount_untaxed - float(self.advance) - float(self.discount_value)
        value = m * 0.15
        before, after = str(value).split('.')
        before_int = int(before)
        after_int = int(after)
        before_ar = convert_numbers.english_to_arabic(before_int)
        after_ar = convert_numbers.english_to_arabic(after_int)
        ar_total_tax_amount = before_ar + '.' + after_ar
        return before_ar + '.' + after_ar

    def net_amount_with_vat(self):
        tax_amount =  self.amount_untaxed - float(self.advance) - float(self.discount_value)
        value = tax_amount * 0.15
        return tax_amount+value
    def ar_net_amount_with_vat(self):
        tax_amount = self.amount_untaxed - float(self.advance) - float(self.discount_value)
        value = tax_amount * 0.15
        with_vat = tax_amount + value
        return convert_numbers.english_to_arabic(int(with_vat))

