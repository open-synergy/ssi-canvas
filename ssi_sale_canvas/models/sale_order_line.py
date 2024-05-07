# Copyright 2024 OpenSynergy Indonesia
# Copyright 2024 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    realization_line_ids = fields.One2many(
        comodel_name="sale_canvas_realization_line",
        inverse_name="sale_line_id",
        string="Sale Canvas Realization Line",
        copy=False
    )

    @api.constrains(
        "product_id",
        "product_uom",
        "product_uom_qty",
    )
    def _realization_check(self):
        if self.env.context.get("force_update"):
            return False
        for rec in self.filtered(lambda l: l.realization_line_ids):
            realization_line_id = rec.realization_line_ids[0]  # harusnya hanya dapat satu
            if (rec.product_id != realization_line_id.product_id
                or rec.product_uom != realization_line_id.uom_id
                    or rec.product_uom_qty != realization_line_id.uom_quantity):
                raise ValidationError(_("You cannot change item details that created from sale canvas menu."))
