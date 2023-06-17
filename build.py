#!/usr/bin/env python3
import os
import datetime
def Write(path: str):
    htmlstring = """<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta name="viewport" content="width=device-width" initial-scale="1" />
        <meta charset="UTF-8">
        <title>文件目录</title>
    </head>
    <body>
        <h1>文件目录</h1>
        <ul>
            <li><a href="..">../</a></li>
"""
    for i in os.listdir(path):
        if i == "index.html" or i == "CNAME" or i == "build.py" or i == "build.sh" or i == ".git" or i == ".github":
            continue
        if os.path.isdir(f"{path}/{i}"):
            htmlstring += f'\n          <li><a href="{i}">{i}/</a></li>'
        else:
            htmlstring += f'\n          <li><a href="{i}">{i}</a></li>'
    htmlstring += f"""     </ul>
        <hr/>
        <h3>更新时间：{datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}</h3>
        <hr/>
        <h1 id="copyright">©2020~2023 gfdgd xi</h1>
</body>
    </body>
</html>
<script>
    window.onload = function(){{
        var d = new Date();
        document.getElementById("copyright").innerHTML = "©2020~" + d.getFullYear() + " gfdgd xi";
    }}
</script>
<script>
var _hmt = _hmt || [];
(function() {{
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?807ee27dfca59506248e7f74c812ca3d";
  var s = document.getElementsByTagName("script")[0]; 
  s.parentNode.insertBefore(hm, s);
}})();
</script>"""
    with open(f"{path}/index.html", "w") as file:
        file.write(htmlstring)
def Dir(path: str):
    Write(path)
    for i in os.listdir(path):
        print(f"{path}/{i}")
        if os.path.isdir(f"{path}/{i}") and i != ".git" and i != ".github":
            Dir(f"{path}/{i}")
Dir(".")
print("构建完成！")