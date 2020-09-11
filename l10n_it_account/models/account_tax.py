# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class AccountTax(models.Model):
    _inherit = 'account.tax'

    cee_type = fields.Selection([
        ('sale', 'Sale'),
        ('purchase', 'Purchase')
    ], string='Include in VAT register',
        help="Use in the case of tax with 'VAT integration'. This "
             "specifies the VAT register (sales / purchases) where the "
             "tax must be computed.")
    parent_tax_ids = fields.Many2many(
        'account.tax', 'account_tax_filiation_rel', 'child_tax', 'parent_tax',
        string='Parent Taxes')

    def _evaluate_tax_amount(self, rec_id):
        rec = self.browse(rec_id)
        data = self.env.context
        move_line_model = self.env['account.move.line']
        domain = ['|',
                  ('tax_line_id', '=', rec_id),
                  ('tax_ids', '!=', False)]
        if data.get('vat_registry_journal_ids'):
            domain.append((
                'move_id.journal_id', 'in', data['vat_registry_journal_ids']))
        if data.get('from_date'):
            domain.append((
                'move_id.date_apply_vat', '>=', str(data['from_date'])))
        if data.get('to_date'):
            domain.append((
                'move_id.date_apply_vat', '<=', str(data['to_date'])))
        base_balance = 0.0
        balance = 0.0
        for line in move_line_model.search(domain):
            if line.tax_ids and rec_id in [x.id for x in line.tax_ids]:
                base_balance += (line.credit - line.debit)
            elif rec_id == line.tax_line_id.id:
                balance += (line.credit - line.debit)
        rec.base_balance = base_balance
        rec.balance = balance
        return rec

    def _get_tax_amount(self):
        self.ensure_one()
        res = 0.0
        if self.amount_type == 'group':
            for child in self.children_tax_ids:
                res += child.amount
        else:
            res = self.amount
        return res

    def _get_tax_name(self):
        self.ensure_one()
        name = self.name
        if self.parent_tax_ids and len(self.parent_tax_ids) == 1:
            name = self.parent_tax_ids[0].name
        return name

    def _compute_totals_tax(self, data):
        """
        Args:
            data: date range, journals and registry_type
        Returns:
            A tuple: (tax_name, base, tax, deductible, undeductible)

        """
        self.ensure_one()
        context = {
            'from_date': data['from_date'],
            'to_date': data['to_date'],
        }
        registry_type = data.get('registry_type', 'customer')
        if data.get('journal_ids'):
            context['vat_registry_journal_ids'] = data['journal_ids']

        if data.get('date_apply_vat'):
            tax = self.env['account.tax'].with_context(
                context)._evaluate_tax_amount(self.id)
        else:
            tax = self.env['account.tax'].with_context(context).browse(self.id)
        tax_name = tax._get_tax_name()
        if not tax.children_tax_ids:
            base_balance = tax.base_balance
            balance = tax.balance
            if registry_type == 'supplier':
                base_balance = -base_balance
                balance = -balance
            return (
                tax_name, base_balance, balance, balance, 0
            )
        else:
            base_balance = tax.base_balance

            tax_balance = 0
            deductible = 0
            undeductible = 0
            for child in tax.children_tax_ids:
                child_balance = child.balance
                if (
                    (
                        data['registry_type'] == 'customer' and
                        child.cee_type == 'sale'
                    ) or
                    (
                        data['registry_type'] == 'supplier' and
                        child.cee_type == 'purchase'
                    )
                ):
                    # Prendo la parte di competenza di ogni registro e lo
                    # sommo sempre
                    child_balance = child_balance

                elif child.cee_type:
                    continue

                tax_balance += child_balance
                if child.account_id:
                    deductible += child_balance
                else:
                    undeductible += child_balance
            if registry_type == 'supplier':
                base_balance = -base_balance
                tax_balance = -tax_balance
                deductible = -deductible
                undeductible = -undeductible
            return (
                tax_name, base_balance, tax_balance, deductible, undeductible
            )
