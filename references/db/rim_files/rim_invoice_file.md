# 发票文件-rim_invoice_file

## 发票文件-主表 t_rim_invoice_file

- **表名称：** 发票文件-主表
- **表名：** t_rim_invoice_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ficon_url | 图标url | varchar | 300 |  | √ | ' ' | 图标url |
| 3 | ffile_hash | 文件hash | varchar | 100 |  | √ | ' ' | 文件hash |
| 4 | ftenant_no | 租户编码 | varchar | 30 |  | √ | ' ' | 租户编码 |
| 5 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fsnapshot_url | 缩略图url | varchar | 300 |  | √ | ' ' | 缩略图url |
| 7 | foriginal_filename | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 8 | fpixel | 像素 | varchar | 20 |  | √ | ' ' | 像素 |
| 9 | foriginal_type | 原文件类型 | varchar | 50 |  | √ | ' ' | 原文件类型,枚举: 1 :pdf 2 :图片 3 :影像文件 4 :ofd |
| 10 | frotation_angle | 旋转角度 | int4 | 32 |  | √ | 0 | 旋转角度 |
| 11 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 12 | fimage_url | 图片url | varchar | 300 |  | √ | ' ' | 图片url |
| 13 | fcreate_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 14 | foriginal_state | 是否源文件 | varchar | 2 |  | √ | ' ' | 是否源文件,枚举: 0 :非源文件 1 :源文件 2 :底账图片 |
| 15 | fregion | 发票区域 | varchar | 35 |  | √ | ' ' | 发票区域 |
| 16 | fpdf_url | pdf url | varchar | 300 |  | √ | ' ' | pdf url |
| 17 | fofd_url | ofd_url | varchar | 300 |  | √ | ' ' | ofd_url |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_invoice_file |  | fid |
| 2 | idx_rim_invoice_file |  | fserial_no |
