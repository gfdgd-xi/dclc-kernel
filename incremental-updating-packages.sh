#!/bin/bash
###### 这里要写绝对路径
REPO_DIR="$1"
DATA_DIR="$REPO_DIR/package-data"
LOCK_DIR="$REPO_DIR/package-lock"

######阶段1：检查data目录下的.deb.package文件，去仓库验证是否有对应的.deb
######如果有，则对比时间戳，若仓库的新于.deb.package，则更新，否则continue
######如果没有，则删除此文件
mkdir -p $DATA_DIR
rm -rf $LOCK_DIR

cd $DATA_DIR
for DEB_PACKAGE_INFO_PATH in `find . -name '*.deb.package'`;do

DEB_PATH=`echo ".${DEB_PACKAGE_INFO_PATH%%.package}"` 
if [ -e $DEB_PATH ];then
	if [ "$DEB_PACKAGE_INFO_PATH"  -ot "$DEB_PATH" ] ;then
		###时间戳校验
		echo "$DEB_PATH在生成package文件后发生了改变，将重新生成"
		rm $DEB_PACKAGE_INFO_PATH
	fi

else
echo "$DEB_PATH 已下架"
rm $DEB_PACKAGE_INFO_PATH
#####删除已下架的包

fi


done

##### 阶段2：反查deb，如果有.deb.package，则跳过，否则生成
cd $REPO_DIR

for DEB_PATH in `find . -name '*.deb'`;do

if [ -e $DATA_DIR/$DEB_PATH.package ];then
continue

else
mkdir -p $DATA_DIR/`dirname $DEB_PATH`
mkdir -p $LOCK_DIR/`dirname $DEB_PATH`
touch $LOCK_DIR/$DEB_PATH.lock
until [ "`find $LOCK_DIR -name '*.deb.lock' | wc -l `" -lt "15" ];do ###最多同时15进程
sleep 1.5
done


apt-ftparchive packages $DEB_PATH > $DATA_DIR/$DEB_PATH.package && echo "新包 $DEB_PATH 已生成package文件" && rm $LOCK_DIR/$DEB_PATH.lock &
fi
done

#####删除data目录下所有空文件夹
until [ -z "`find $LOCK_DIR -name '*.deb.lock'`"  ];do
sleep 1
done


rm -r $LOCK_DIR

find $DATA_DIR -type d -empty -exec rm -rf {} \;

##### 合成Packages
rm $REPO_DIR/Packages
cd $DATA_DIR
for DEB_PACKAGE_INFO_PATH in `find . -name '*.deb.package'`;do
cat $DEB_PACKAGE_INFO_PATH >> $REPO_DIR/Packages
done
