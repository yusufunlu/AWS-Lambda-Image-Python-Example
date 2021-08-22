import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Request: %s", event)
    body = event.get('body')

    response_code = 200
    responseBody = ""

    if body is not None:
        try:
            jsonBody = json.loads(body)
            decimalValue = jsonBody.get('decimal')
            decimalNumber = int(decimalValue)
        except Exception as e:
            logger.exception("Exception occured: %s", e.__class__)
            response_code = 400
            responseBody = json.dumps({'message': str(e), 'rawRequest': event})
        else:
            decimalArray = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
            romanSymbolArray = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
            roman_num = ''

            i = 0
            while  decimalNumber > 0:
                for _ in range(decimalNumber // decimalArray[i]):
                    roman_num += romanSymbolArray[i]
                    decimalNumber -= decimalArray[i]
                i += 1
            responseBody = json.dumps({'roman': roman_num})

    response = {
        'statusCode': response_code,
        'body': responseBody
    }

    logger.info("Response: %s", response)
    return response
