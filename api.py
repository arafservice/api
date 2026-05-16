    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route('/')
    def home():
        return "به API خوش آمدید! برای استفاده، به /greet/your_name مراجعه کنید."

    @app.route('/greet/<string:name>', methods=['GET'])
    def greet(name):
        """
        این نقطه پایانی یک پیام خوشامدگویی با نام ورودی برمی‌گرداند.
        مثال: GET /greet/Alice
        """
        response = {
            "message": f"سلام {name}! به API خوش آمدی."
        }
        return jsonify(response)

    @app.route('/add', methods=['POST'])
    def add_numbers():
        """
        این نقطه پایانی دو عدد را از body درخواست دریافت کرده و جمع آن‌ها را برمی‌گرداند.
        مثال درخواست POST:
        {
            "num1": 5,
            "num2": 10
        }
        """
        data = request.get_json()
        if not data or 'num1' not in data or 'num2' not in data:
            return jsonify({"error": "لطفاً num1 و num2 را در body درخواست ارسال کنید."}), 400

        try:
            num1 = float(data['num1'])
            num2 = float(data['num2'])
            result = num1 + num2
            response = {
                "message": f"نتیجه جمع {num1} و {num2} برابر است با: {result}"
            }
            return jsonify(response)
        except ValueError:
            return jsonify({"error": "مقادیر num1 و num2 باید عدد باشند."}), 400

    if __name__ == '__main__':
        # برای اجرای محلی، debug=True تنظیم شده. برای production باید False باشد.
        # host='0.0.0.0' باعث میشه API از بیرون هم قابل دسترس باشه (در صورت تنظیمات شبکه مناسب)
        app.run(debug=True, host='0.0.0.0', port=5000)
