# 回单下载连接监控-receipt_connect_monitor

## 回单下载连接监控-主表 t_receipt_connect_monitor

- **表名称：** 回单下载连接监控-主表
- **表名：** t_receipt_connect_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 4 | freceipt_way | 回单获取方式 | varchar | 50 |  | √ | ' ' | 回单获取方式,枚举: bank_login :前置机代理获取 sftp :远程SFTP获取 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fuser | sftp登录用户 | varchar | 255 |  | √ | ' ' | sftp登录用户 |
| 7 | ferror_msg | 失败详情 | varchar | 512 |  | √ | ' ' | 失败详情 |
| 8 | fprivate_cert_path | sftp私钥文件路径 | varchar | 255 |  | √ | ' ' | sftp私钥文件路径 |
| 9 | fip | IP地址 | varchar | 255 |  | √ | ' ' | IP地址 |
| 10 | fpassword | sftp登录密码 | varchar | 255 |  | √ | ' ' | sftp登录密码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fmonitor_time | 检测时间 | timestamp | 0 |  |  | null | 检测时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  |  | 0 | 主数据内码 |
| 16 | fport | 端口号 | varchar | 50 |  | √ | ' ' | 端口号 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fmonitor_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: SUCCESS :连接正常 FAIL :连接异常 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_connect_monitor_pkey |  | fid |

---

## 回单下载连接监控-多语言表 t_receipt_connect_monitor_l

- **表名称：** 回单下载连接监控-多语言表
- **表名：** t_receipt_connect_monitor_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_receipt_connect_monitor_l_pkey |  | fpkid |
