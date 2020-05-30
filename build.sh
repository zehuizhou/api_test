#!/usr/bin/env bash
# 检测的文件
package=./requirements.txt
# 记录 md5值的文件
md5=package_md5
# 创建新的md5信息
package_md5_new=$(md5sum -b $package | awk '{print $1}'|sed 's/ //g')

# 创建md5的函数
function creatmd5()
{
        echo $package_md5_new > $md5
}

# 判断文件是否存在
if [ ! -f $md5 ] ; then
        echo "md5file is not exsit,create md5file......."
        creatmd5
        exit
fi

# 读取旧的md5信息
package_md5_old=$(cat $md5|sed 's/ //g')

echo $package_md5_new
echo $package_md5_old

# 对象对比判断
if [ "$package_md5_new" == "$package_md5_old" ];then
        echo "md5 is not changed"
else
        echo "md5 is changed"
        creatmd5
        docker build -t api_pytest .
fi
