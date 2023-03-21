from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    AmazonProduct = fields.Integer(string='Amazon', compute='_get_external_amazon_product')
    EbayProduct = fields.Integer(string='Ebay', compute='_get_external_ebay_product')
    LTProduct = fields.Integer(string='LT', compute='_get_external_LT_product')
    LVProduct = fields.Integer(string='LV', compute='_get_external_LV_product')
    EEProduct = fields.Integer(string='EE', compute='_get_external_EE_product')


    # Method that will crash if the image a linked image exists to a product
    # The crash is intentional and cought in try/except statement
    def get_image_binary(self):
        product_image = self.image_1920
        image_data = product_image and product_image.datas or False
        return False


    # Computes the progress bar value of amazon product
    @api.depends('weight', 'uom_id', 'list_price', 'image_1920')
    @api.model
    def _get_external_amazon_product(self):
        for record in self:
            set_fields = 0
            try:
                record.get_image_binary()
                pass
            # If the image exists and is linked to the product get_image_binary() will crash
            except:
                set_fields += 25
                    
            if record.weight:
                set_fields += 25
            if record.uom_id:
                set_fields += 25
            if record.list_price:
                set_fields += 25

            record.AmazonProduct = set_fields

    # Computes the progress bar value of ebay product
    @api.depends('list_price', 'image_1920', 'allow_out_of_stock_order')
    @api.model
    def _get_external_ebay_product(self):
        for record in self:
            set_fields = 0

            try:
                record.get_image_binary()
                pass
            # If the image exists and is linked to the product get_image_binary() will crash
            except:
                set_fields += 25
                    
            if record.list_price:
                set_fields += 25

            if record.allow_out_of_stock_order:
              set_fields += 25

            record.EbayProduct = set_fields


    # Computes the progress bar value of LT product
    @api.depends('uom_id', 'list_price', 'image_1920', 'alternative_product_ids')
    @api.model
    def _get_external_LT_product(self):
        for record in self:
            set_fields = 0

            if record.uom_id:
                set_fields += 25

            try:
                record.get_image_binary()
                pass
            # If the image exists and is linked to the product get_image_binary() will crash
            except:
                set_fields += 25
                    
            if record.list_price:
                set_fields += 25
            try:
              if record.alternative_product_ids:
                  set_fields += 25
            except:
                pass
            
            record.LTProduct = set_fields

    # Computes the progress bar value of LV product
    @api.depends('weight', 'list_price', 'image_1920', 'volume')
    @api.model
    def _get_external_LV_product(self):
        for record in self:
            set_fields = 0
            try:
                record.get_image_binary()
                pass
            # If the image exists and is linked to the product get_image_binary() will crash
            except:
                set_fields += 40
                    
            if record.weight:
                set_fields += 20
            if record.list_price:
                set_fields += 20
            if record.volume:
                set_fields += 20

            record.LVProduct = set_fields

    # Computes the progress bar value of EE product
    @api.depends('weight', 'list_price', 'image_1920', 'volume', 'alternative_product_ids')
    @api.model
    def _get_external_EE_product(self):
        for record in self:
            set_fields = 0
            try:
                record.get_image_binary()
                pass
            # If the image exists and is linked to the product get_image_binary() will crash
            except:
                set_fields += 20
                    
            if record.weight:
                set_fields += 20
            if record.list_price:
                set_fields += 20
            if record.volume:
                set_fields += 20
            try:
              if record.alternative_product_ids:
                  set_fields += 20
            except:
                pass

            record.EEProduct = set_fields