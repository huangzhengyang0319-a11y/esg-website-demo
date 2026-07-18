# 引入我们刚刚安装的 Flask 和 CORS 工具
from flask import Flask, jsonify
from flask_cors import CORS

# 初始化 Flask 应用
app = Flask(__name__)
# 允许前端网页跨域访问我们的后端
CORS(app)

# 准备一份 ESG 的“假数据”（这就是我们的后厨菜单）
esg_data = [
    {
        "title": "环境 (E)",
        "children": [
            {"title": "碳排放管理", "content": "2023年温室气体排放量同比下降5%，全面推广绿色办公。"},
            {"title": "水资源保护", "content": "优化生产用水循环系统，水资源重复利用率提升至85%。"}
        ]
    },
    {
        "title": "社会 (S)",
        "children": [
            {"title": "员工权益", "content": "全年员工培训时长达40小时，女性高管占比提升至30%。"},
            {"title": "社区公益", "content": "投入100万元用于乡村教育支持，开展20场志愿者活动。"}
        ]
    },
    {
        "title": "治理 (G)",
        "children": [
            {"title": "商业道德", "content": "100%员工签署《反腐败合规承诺书》，零违规事件。"},
            {"title": "风险管理", "content": "建立全面风险预警机制，全年开展4次合规审查。"}
        ]
    }
]

# 定义一个“接口（API）”：当有人访问 /api/esg 时，就把数据返回给他
@app.route('/api/esg')
def get_esg_data():
    return jsonify(esg_data)

# 启动后端服务，运行在 5000 端口
if __name__ == '__main__':
    app.run(debug=True, port=5000)