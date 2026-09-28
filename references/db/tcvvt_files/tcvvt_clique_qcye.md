# 期初余额-tcvvt_clique_qcye

## 期初余额-主表 t_tcvvt_clique_qcye

- **表名称：** 期初余额-主表
- **表名：** t_tcvvt_clique_qcye

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fkm_dm | 科目代码(废弃) | varchar | 100 |  | √ | ' ' | 科目代码(废弃) |
| 6 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnd_dm | 年度代码 | varchar | 4 |  | √ | ' ' | 年度代码 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fkjqj | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :1 02 :2 03 :3 04 :4 05 :5 06 :6 07 :7 08 :8 09 :9 10 :10 11 :11 12 :12 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fqcjfye | 期初借方余额 | numeric | 25 | 4 | √ | 0 | 期初借方余额 |
| 13 | fyear | 年度代码 | timestamp | 0 |  |  | null | 年度代码 |
| 14 | fqcdfye | 期初贷方余额 | numeric | 25 | 4 | √ | 0 | 期初贷方余额 |
| 15 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :自动采集 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fkmdm | 科目代码 | int8 | 64 |  | √ | 0 | [科目 tcvvt_clique_account](../tcvvt_files/tcvvt_clique_account.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_clique_qcye_org |  | forgid |
| 2 | pk_tcvvt_clique_qcye |  | fid |
