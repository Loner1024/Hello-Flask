from flask import Flask,render_template #引入渲染函数

@app.route('/watchlist')
def watchlist():
   return render_template('watchlist.html',user=user,movies=movies)
'''
flask会自动到templates文件夹寻找模板文件
'''