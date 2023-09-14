from flask import Flask, request, render_template, flash, redirect, url_for
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':
        image_url = request.form['url']  # Retrieve the image URL from the form

        # Initialize OCR client and credentials
        ak = "GVWM2NWD6DIEBDGM1UY6"
        sk = "Alvtv4QXmZa2KiZtjL9q7qaX9HB3pXsBFbIQ5udo"
        credentials = BasicCredentials(ak, sk)

        client = OcrClient.new_builder() \
            .with_credentials(credentials) \
            .with_region(OcrRegion.value_of("ap-southeast-2")) \
            .build()

        try:
            ocr_request = RecognizeThailandIdcardRequest()
            ocr_request.body = ThailandIdcardRequestBody(
                url=image_url
            )
            response = client.recognize_thailand_idcard(ocr_request)
            result = response.result

            # Return the OCR result as JSON
            return {'ocr_result': result}
        except exceptions.ClientRequestException as e:
            return {'error': f"Error: {e.error_msg}"}

if __name__ == '__main__':
    app.run(debug=True)
