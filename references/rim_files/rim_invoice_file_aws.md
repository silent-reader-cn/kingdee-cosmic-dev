# aws发票文件-rim_invoice_file_aws

## aws发票文件-主表 t_rim_invoice_file_aws

- **表名称：** aws发票文件-主表
- **表名：** t_rim_invoice_file_aws

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fsnapshot_url | 快照url | varchar | 300 |  | √ | ' ' | 快照url |
| 5 | fdownload_url | 原文件url | varchar | 300 |  | √ | ' ' | 原文件url |
| 6 | fpixel | 像素 | varchar | 20 |  | √ | ' ' | 像素 |
| 7 | fdeal_times | 处理次数 | int8 | 64 |  | √ | 0 | 处理次数 |
| 8 | frotation_angle | 旋转角度 | int8 | 64 |  | √ | 0 | 旋转角度 |
| 9 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 0 :待处理 1 :处理成功 2 :处理失败 |
| 10 | fserial_no | 发票流水号 | varchar | 50 |  | √ | ' ' | 发票流水号 |
| 11 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | ffile_type | 文件类型 | varchar | 4 |  | √ | ' ' | 文件类型,枚举: 1 :pdf 2 :图片 4 :ofd |
| 13 | fregion | 发票区域 | varchar | 35 |  | √ | ' ' | 发票区域 |
| 14 | foriginal_file_name | 原文件名称 | varchar | 100 |  | √ | ' ' | 原文件名称 |
| 15 | fdown_type | 下载类型 | varchar | 20 |  | √ | ' ' | 下载类型,枚举: down :下载进项发票文件 att :下载附件 cov :下载封面 gen :生成地址文件 img :生成快照 img2 :下载销项发票文件 |
| 16 | fofd_url | pdfurl | varchar | 300 |  | √ | ' ' | pdfurl |
| 17 | fattachment_name | 附件名称 | varchar | 50 |  | √ | ' ' | 附件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_invoice_file_aws |  | fserial_no |
| 2 | pk_rim_invoice_file_aws |  | fid |
