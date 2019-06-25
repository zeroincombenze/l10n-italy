from odoo import http
from odoo.addons.l10n_it_einvoice_send2sdi.models.attachment import Evolve

class Certdoc(http.Controller):

    @http.route('/certdoc', type='http', auth='public')
    def render_index_page(self, archive_id =  None):

        ret = self.header()

        if archive_id == "1":
            ret += self.filter_attive(archive_id)
            ret += self.get_attive()
        if archive_id == "2":
            ret += self.filter_attive(archive_id)

        return ret

    def filter_attive(self, archive_id):

        return '<br><form action="/certdoc?archive_id='+archive_id+'"><label for="from">From</label><input name="from"> <label for="to">To</label><input name="to"><input type="submit"></form>'

    def get_attive(self):

        send_channel = http.request.env.user.company_id.einvoice_sender_id
        headers = Evolve.header(send_channel)

    def get_passive(self):
        return "prova"

    def header(self):

        return '<a href="/certdoc?archive_id=1">Fatture attive</a> - <a href="/certdoc?archive_id=2">Passive</a>'
