# 关联关系删除记录-link_deleted_record

## 关联关系删除记录-主表 t_botp_linkdeleted_record

- **表名称：** 关联关系删除记录-主表
- **表名：** t_botp_linkdeleted_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fusername | 用户名 | varchar | 200 |  | √ | ' ' | 用户名 |
| 3 | fsourcenumber | 源单标识 | varchar | 80 |  | √ | ' ' | 源单标识 |
| 4 | fdeldata_tag | 删除数据_详情 | text | 0 |  |  | null | 删除数据_详情 |
| 5 | fcreatetime | 删除时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 删除时间 |
| 6 | fsourcefid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 7 | ftargetnumber | 目标单标识 | varchar | 80 |  | √ | ' ' | 目标单标识 |
| 8 | flinktype | 关联关系类型 | varchar | 255 |  | √ | ' ' | 关联关系类型 |
| 9 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 10 | ftargetfid | 目标单ID | varchar | 50 |  | √ | ' ' | 目标单ID |
| 11 | fdeldata | 删除数据 | varchar | 255 |  | √ | ' ' | 删除数据 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_botp_linkdeleted_record |  | fid |
| 2 | idx_botp_linkdeleted_record |  | ftargetnumber,ftargetfid,fsourcenumber,fsourcefid |
