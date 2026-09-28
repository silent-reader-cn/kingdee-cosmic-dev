# 分支进项税额加计抵减模板-tcvat_fz_income_add_temp

## 分支进项税额加计抵减模板-主表 t_tcvat_fz_adddeduct

- **表名称：** 分支进项税额加计抵减模板-主表
- **表名：** t_tcvat_fz_adddeduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fenddate | fenddate | timestamp | 0 |  |  | null |  |
| 3 | fstartdate | fstartdate | timestamp | 0 |  |  | null |  |
| 4 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fcurrentdecrease | 本期调减额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期调减额 |
| 6 | fservicetype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 7 | frowno | 序号 | varchar | 50 |  | √ | ' ' | 序号 |
| 8 | fcurrentamount | 本期发生额 | numeric | 23 | 10 | √ | 0.0000000000 | 本期发生额 |
| 9 | fdifftype | 差额扣除类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tcvat_bizdef_entity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_fz_adddeduct |  | fid |
| 2 | idx_tcvat_fz_adddeduct |  | forgid,fstartdate,fenddate |
