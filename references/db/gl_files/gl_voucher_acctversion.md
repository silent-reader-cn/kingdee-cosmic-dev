# 科目版本化凭证记录-gl_voucher_acctversion

## 科目版本化凭证记录-主表 t_gl_voucheracctversion

- **表名称：** 科目版本化凭证记录-主表
- **表名：** t_gl_voucheracctversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucherid | 凭证ID | int8 | 64 |  | √ | 0 | 凭证ID |
| 3 | fafaccountid | 版本化后科目ID | int8 | 64 |  | √ | 0 | 版本化后科目ID |
| 4 | fversiondate | 版本化日期 | timestamp | 0 |  |  | null | 版本化日期 |
| 5 | fvoucherentryid | 凭证分录ID | int8 | 64 |  | √ | 0 | 凭证分录ID |
| 6 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbefasstvalue | 版本化前核算维度值 | int8 | 64 |  | √ | 0 | 版本化前核算维度值 |
| 9 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | freaccountid | 版本化前科目ID | int8 | 64 |  | √ | 0 | 版本化前科目ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_vchvsn_ve |  | fvoucherentryid |
| 2 | idx_gl_vchvsn_del |  | forgid,freaccountid,fversiondate |
| 3 | pk_t_gl_voucheracctversion |  | fid |
