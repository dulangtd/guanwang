from flask import Flask, request, jsonify
from PIL import Image
import os
import base64
from io import BytesIO

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # 获取上传的图片
        image_file = request.files['image']
        if not image_file:
            return jsonify({'error': '没有上传图片'}), 400
            
        # 打开图片
        img = Image.open(image_file)
        
        # 调整图片大小
        img.thumbnail((800, 800))
        
        # 转换为base64
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        return jsonify({
            'success': True,
            'image': img_str
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 