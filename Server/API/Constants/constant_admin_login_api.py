
class AdminLoginConstants:
    url = "https://qa-api.trado.co.il/api/admin-user/login"
    valid_data = '{"phone":"1950000000","code":"1234","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    invalid_phone_invalid_code = '{"phone":"1950000356","code":"6758","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_and_code_field_null = '{"phone":"","code":"","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    valid_phone_and_invalid_code = '{"phone":"1950000000","code":"6758","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    invalid_phone_and_valid_code = '{"phone":"1950000356","code":"1234","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    valid_phone_and_code_null = '{"phone":"1950000000","code":"","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_null_code_valid = '{"phone":"","code":"1234","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    invalid_phone_code_null = '{"phone":"1950000356","code":"","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_null_code_invalid = '{"phone":"","code":"6758","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_longValue_and_code_valid = '{"phone":"1950000000000000","code":"1234","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_shortValue_and_code_valid = '{"phone":"1950","code":"1234","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_longValue_and_code_invalid = '{"phone":"195000000000","code":"6758","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_shortValue_and_code_invalid = '{"phone":"1950","code":"6758","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_longValue_and_code_null = '{"phone":"1950000000000","code":"","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_insert_shortValue_and_code_null = '{"phone":"19500","code":"","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_valid_and_code_insert_longValue = '{"phone":"1950000000","code":"123455666","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_valid_and_code_insert_shortValue = '{"phone":"1950000000","code":"12","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_null_and_code_insert_longValue = '{"phone":"","code":"1234567","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_null_and_code_insert_shortValue = '{"phone":"","code":"12","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_invalid_and_code_insert_longValue = '{"phone":"1950000356","code":"12345678","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_invalid_and_code_insert_shortValue = '{"phone":"1950000356","code":"12","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_and_code_both_insert_longValue = '{"phone":"19500000000000000","code":"12345678","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    phone_and_code_both_insert_shortValue = '{"phone":"1950","code":"12","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    both_fields_insert_character = '{"phone":"@@@####","code":"@@@@@$$##","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
    both_fields_insert_string_character_and = '{"phone":"@@@1111&&&","code":"1234@#$#$","rememberMe":true,"info":{"lng":"hebrew","getTypes":false,"platform":"admin","isMobile":false,"screenHeight":1080,"screenWidth":1920,"location":{"ancestorOrigins":{},"href":"https://qa-admin.trado.co.il/#/login","origin":"https://qa-admin.trado.co.il","protocol":"https:","host":"qa-admin.trado.co.il","hostname":"qa-admin.trado.co.il","port":"","pathname":"/","search":"","hash":"#/login"}}}'
