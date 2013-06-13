productapi
==========
Example API using piston to encode the JSON.

List all Products:
http://manta.colorsproject.com/api/products/all/

List Product by id:
http://manta.colorsproject.com/api/products/3/

Create Product with vendor_style_number, vendor_color, and vendor_size
http://manta.colorsproject.com/api/products/?action=create&vendor_style_number=ASDWER&vendor_color=BLACK&vendor_size=S

Update Product with vendor_style_number, vendor_color, and vendor_size
http://manta.colorsproject.com/api/products/3/?action=update&vendor_style_number=ASDWER&vendor_color=BLACK&vendor_size=S

Delete Product and all attributes
http://manta.colorsproject.com/api/products/3/?action=delete

Add Attribute on Create (attributes can have any value except vendor_style_number, vendor_color, vendor_size, and action)
http://manta.colorsproject.com/api/products/?action=create&vendor_style_number=ASDWER&vendor_color=BLACK&vendor_size=S&retail_price_USD=200&retail_price_GBP=450

Update or Add new Attributes
http://manta.colorsproject.com/api/products/3/?action=update&retail_price_GBP=350

Delete Attribute
NOT COMPLETED

Search
NOT COMPLETED




