# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Canvas",
    "version": "14.0.1.0.0",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "ssi_stock",
        "ssi_sale",
        "ssi_master_data_mixin",
        "ssi_transaction_confirm_mixin",
        "ssi_transaction_open_mixin",
        "ssi_transaction_done_mixin",
        "ssi_transaction_terminate_mixin",
        "ssi_transaction_cancel_mixin",
        "ssi_product_line_mixin",
        "base_automation",
        "ssi_product",
        "ssi_m2o_configurator_mixin",
        "ssi_stock_location_m2o_configurator_mixin",
        "ssi_stock_route_m2o_configurator_mixin",
        "ssi_stock_warehouse_m2o_configurator_mixin",
        "web_widget_x2many_2d_matrix",
        "sale_order_price_recalculation",
        "ssi_stock_canvas_operation",
        "ssi_res_currency_m2o_configurator_mixin",
    ],
    "data": [
        "security/ir_module_category_data.xml",
        "security/res_group_data.xml",
        "security/ir.model.access.csv",
        "security/ir_rule_data.xml",
        "data/ir_sequence_data.xml",
        "data/sequence_template_data.xml",
        "data/policy_template_data.xml",
        "data/approval_template_data.xml",
        "menu.xml",
        "views/sale_canvas_type_views.xml",
        "views/sale_canvas_views.xml",
        "data/ir_actions_server_data.xml",
        "data/base_automation_data.xml",
    ],
    "demo": [],
    "images": [],
}
