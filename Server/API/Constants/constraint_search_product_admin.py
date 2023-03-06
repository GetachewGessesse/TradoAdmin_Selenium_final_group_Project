class ConstraintProduct:
    url = "https://qa-api.trado.co.il/api/product/filter"
    valid_data_json = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"milk","info":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    invalid_jason_non_exsting = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"dwgqhqvu","info":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    invalid_special_characters = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"@$$@","info":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    input_from_the_user = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"gghkk;l;e","info":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    number_from_the_user = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"12345":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    empty_item_from_the_user = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    single_letter = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    sorting_products = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"goats milk ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    multiple_products = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":"goats milk ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    repeated_letters = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" mmilk ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    display_correctly = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" goats milk ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    upper_case = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" MILK ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    lower_case = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" milk ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'
    lower_and_upper_case = '{"from":0,"limit":50,"sort":{"createdAt":-1},"filter":{},"search":" miLK ":{"uid":"pslie6ckppafmkm","sid":"1010101011rh","lng":"hebrew","getTypes":true,"platform":"admin","isMobile":false,"screenHeight":864,"screenWidth":1536,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/products","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/products"}}}'