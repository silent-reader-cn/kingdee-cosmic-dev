# 应收关账记录-ar_closerecord

## 应收关账记录-主表 t_ar_closerecord

- **表名称：** 应收关账记录-主表
- **表名：** t_ar_closerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedate | 关账日期 | timestamp | 0 |  |  | null | 关账日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_closerecord_pkey |  | fid |
| 2 | idx_ar_record_orgdate |  | forgid,fclosedate |
