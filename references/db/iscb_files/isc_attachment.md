# 集成附件信息-isc_attachment

## 集成附件信息-主表 t_isc_attachment

- **表名称：** 集成附件信息-主表
- **表名：** t_isc_attachment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrc_cn | 源系统连接 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 3 | fsrc_att_create_time | 源附件创建时间 | timestamp | 0 |  |  | null | 源附件创建时间 |
| 4 | ffile_name | 附件文件名 | varchar | 255 |  | √ | ' ' | 附件文件名 |
| 5 | fsrc_oid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 6 | ffile_desc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fbytes | 字节数 | int8 | 64 |  | √ | 0 | 字节数 |
| 8 | f1 | 自定义字段1 | varchar | 255 |  | √ | ' ' | 自定义字段1 |
| 9 | f2 | 自定义字段2 | varchar | 255 |  | √ | ' ' | 自定义字段2 |
| 10 | ftar_attach | 目标附件ID | varchar | 50 |  | √ | ' ' | 目标附件ID |
| 11 | f3 | 目标附件创建人ID | varchar | 255 |  | √ | ' ' | 目标附件创建人ID |
| 12 | fcreated_time | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fsrc_table | 源单数据表 | varchar | 50 |  | √ | ' ' | 源单数据表 |
| 14 | ftar_cn | 目标系统连接 | int8 | 64 |  | √ | 0 | 连接器配置 isc_database_link |
| 15 | fstate | fstate | varchar | 30 |  | √ | ' ' |  |
| 16 | fupdated_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 17 | fsrc_att_creator | 源附件创建人ID | varchar | 100 |  | √ | ' ' | 源附件创建人ID |
| 18 | fsrc_att_creator_num | 源附件创建人编码 | varchar | 100 |  | √ | ' ' | 源附件创建人编码 |
| 19 | fsrc_number | 源单编码 | varchar | 100 |  | √ | ' ' | 源单编码 |
| 20 | ffile_type | 附件类型 | varchar | 50 |  | √ | ' ' | 附件类型 |
| 21 | fmd5_code | md5码 | varchar | 50 |  | √ | ' ' | md5码 |
| 22 | fsrc_attach | 源附件ID | varchar | 50 |  | √ | ' ' | 源附件ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_attachment_pkey |  | fid |
| 2 | idx_isc_attach_time |  | fupdated_time |
| 3 | idx_isc_attach |  | fsrc_oid,fsrc_attach,fsrc_cn,ftar_cn |
