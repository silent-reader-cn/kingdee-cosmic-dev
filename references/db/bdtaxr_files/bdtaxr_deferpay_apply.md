# 缓缴申请表-bdtaxr_deferpay_apply

## 缓缴申请表-主表 t_bdtaxr_deferpay_apply

- **表名称：** 缓缴申请表-主表
- **表名：** t_bdtaxr_deferpay_apply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperator | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | foperatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 4 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 5 | fapplyno | 申请编号 | varchar | 50 |  | √ | ' ' | 申请编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_deferpay_apply |  | fid |
| 2 | idx_bdtaxr_deferpay_apply |  | fsbbid |
