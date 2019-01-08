# -*- coding: utf-8 -*-
# Copyright 2016 Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
#                Odoo Italian Community
#                Odoo Community Association (OCA)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models
from odoo import api


RPT_ACTION = [('odoo', 'odoo'),
              ('report', 'report'),
              ('company', 'company'),
              ('customer', 'customer')]


@api.model
def _lang_get(self):
    languages = self.env['res.lang'].search([])
    return [(language.code, language.name) for language in languages]


class MultireportSelectionRules(models.Model):
    _name = "multireport.selection.rules"
    _description = "Rules to select report name"

    name = fields.Char(
        'Rule Name',
        required=True,
        help="Brief name of document to print")
    model_id = fields.Many2one(
        'ir.model', 'Related Document Model',
        required=True,
        domain=[('osv_memory', '=', False)],
        help="Model to apply this rule")
    model = fields.related(
        'model_id', 'model', type="char", string='Model')
    reportname = fields.Char(
        'Internal report name',
        readonly=True,
        help="Set the report name formatted as module.reportname;"
             " i.e: 'account.report_invoice' like"
             " Odoo standard report name."
             " This field is applied if action is 'report'.")
    purpose = fields.Char(
        'Purpose',
        help="Report purpose: why, when use this report.")
    sequence = fields.Integer(
        'sequence',
        help="Rules are evaluated starting from lower sequence. "
             "Please, use values above 100 for default rules, "
             "from 10 to 100 for ordinary rules."
             "Sequences below 10 must be very important!")
    action = fields.Selection(
        RPT_ACTION,
        'report action',
        help="Set 'report' to get the internal report name field,"
             " 'company' to get preferred model of company (if any),"
             " 'customer' to get preferred model of customer (if any),"
             " 'odoo' to execute Odoo standard document printing.")
    journal_id = fields.Many2one(
        'account.journal',
        'If journal',
        help="Apply rule only if journal matches document;"
             " may be useful to print commercial invoices"
             " like Italian 'Fattura Accompagnatoria'.")
    partner_id = fields.Many2one(
        'res.partner',
        'If customer',
        help="Apply rule only if invoice of customer;"
             " may be useful to print specific model for customer.")
    lang = fields.Selection(
        _lang_get,
        'If language',
        help="Apply rule only if language matches customer;"
             " may be useful to print untranslated report models.")
    position_id = fields.Many2one(
        'account.fiscal.position',
        'If fiscal position',
        help="Apply rule only if fiscal position matches"
             " invoice position; may be useful to print"
             " models to satisfy some fiscal law.")
    section_id = fields.many2one(
        'crm.case.section',
        'If sales team',
        help="Apply rule only if sales team matches"
             " invoice position; may be useful to print"
             " models to customize sale documents.")
    since_date = fields.Date('From date')
    until_date = fields.Date('To date')
    active = fields.Boolean(
        'Active',
        help="Rule is evaluated only if is active.")


class Report(models.Model):
    _inherit = "report"

    @api.noguess
    def get_action(self, docids, report_name, data=None):
        rule_model = self.env['multireport.selection.rules']
        for rule in rule_model.search([('active', '=', True)],
                                      order='sequence'):
            if rule.action == 'odoo':
                break
            elif rule.reportname:
                report_name = rule.reportname
                break
        return super(Report, self).get_action(docids, report_name, data=data)