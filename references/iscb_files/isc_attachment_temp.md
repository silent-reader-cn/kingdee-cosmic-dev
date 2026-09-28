# 附件信息临时表-isc_attachment_temp

## 附件信息临时表-主表 t_isc_attachment_temp

- **表名称：** 附件信息临时表-主表
- **表名：** t_isc_attachment_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemp_name | 临时文件名 | varchar | 255 |  | √ | ' ' | 临时文件名 |
| 3 | fname | 附件名称 | varchar | 255 |  | √ | ' ' | 附件名称 |
| 4 | fusr_def_create_time | 自定义附件创建时间 | timestamp | 0 |  |  | null | 自定义附件创建时间 |
| 5 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: W :待同步 S :同步完成 F :同步失败 |
| 6 | ftype | 附件类型 | varchar | 30 |  | √ | ' ' | 附件类型 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | furl | url | varchar | 500 |  | √ | ' ' | url |
| 9 | fbytes | 大小（字节数） | varchar | 50 |  | √ | ' ' | 大小（字节数） |
| 10 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fusr_def_creator | 自定义附件创建人 | varchar | 50 |  | √ | ' ' | 自定义附件创建人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_attachment_temp_pkey |  | fid |
| 2 | idx_isc_attach_temp_1 |  | fname |
