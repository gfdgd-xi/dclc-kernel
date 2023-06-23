# Deepin Community Live CD New Kernel 系列仓库
> 地址：http://kernel.dclc.gfdgdxi.top
## 只加源
```bash
wget http://kernel.dclc.gfdgdxi.top/sources/github.sh ; bash github.sh ; rm github.sh
```
### 加源后如何安装？
```bash
sudo apt update
sudo apt install linux-kernel-dclc-gfdgdxi
```
## 镜像
正在制作ing
### 效果图（非最终效果，只供参考）
![图片.png](https://storage.deepin.org/thread/202306181811191603_图片.png)

![图片.png](https://storage.deepin.org/thread/202306181811355292_图片.png)

## 如何提交 DEB（PR）
需要在仓库根目录创建以内核版本号为文件名的文件夹，然后修改 `kernel.txt` 里的内容为内核版本号（不能有换行符，包括行尾）  
最后再修改仓库的 `head/deb/DEBIAN/control` 文件，修改 `Version:` 和 `Depends:` 字段为内核版本号和内核 deb 包包名  

## 鸣谢名单
### 提供内核
| 内核版本 | 提供用户 |
| :-: | :-: |
| 6.3.5-1、6.3.6、6.3.7、6.3.8、6.4.0-rc4、6.4.0-rc5 | [.](https://bbs.deepin.org/user/297983) |

## ©2022~2023 gfdgd xi
