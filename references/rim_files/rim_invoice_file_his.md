# 发票文件历史-rim_invoice_file_his

## 发票文件历史-主表 t_rim_invoice_file_his

- **表名称：** 发票文件历史-主表
- **表名：** t_rim_invoice_file_his

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ficon_url | 图标url | varchar | 300 |  | √ | ' ' | 图标url |
| 3 | ftraceid | 操作流水 | varchar | 50 |  | √ | ' ' | 操作流水 |
| 4 | ffile_hash | 文件hash | varchar | 100 |  | √ | ' ' | 文件hash |
| 5 | ftenant_no | 租户编码 | varchar | 30 |  | √ | ' ' | 租户编码 |
| 6 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 7 | foperate_time | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fsnapshot_url | 缩略图url | varchar | 300 |  | √ | ' ' | 缩略图url |
| 9 | foriginal_filename | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 10 | fpixel | 像素 | varchar | 20 |  | √ | ' ' | 像素 |
| 11 | foriginal_type | 原文件类型 | varchar | 50 |  | √ | ' ' | 原文件类型,枚举: 1 :pdf 2 :图片 3 :影像文件 4 :ofd |
| 12 | frotation_angle | 旋转角度 | int4 | 32 |  | √ | 0 | 旋转角度 |
| 13 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 14 | fimage_url | 图片url | varchar | 300 |  | √ | ' ' | 图片url |
| 15 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | foriginal_state | 是否源文件 | varchar | 2 |  | √ | ' ' | 是否源文件,枚举: 0 :非源文件 1 :源文件 2 :底账图片 |
| 18 | fregion | 发票区域 | varchar | 35 |  | √ | ' ' | 发票区域 |
| 19 | fpdf_url | pdf url | varchar | 300 |  | √ | ' ' | pdf url |
| 20 | fofd_url | ofd_url | varchar | 300 |  | √ | ' ' | ofd_url |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_invoice_file_his |  | fid |
| 2 | idx_rim_invoice_file_his |  | fserial_no |
