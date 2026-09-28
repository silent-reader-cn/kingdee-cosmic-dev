# 凭证分录-tcvvt_voucher

## 凭证分录-主表 t_tcvvt_voucher

- **表名称：** 凭证分录-主表
- **表名：** t_tcvvt_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpzh | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 4 | fwbjfje | 外币借方金额 | numeric | 23 | 4 |  | null | 外币借方金额 |
| 5 | fwbdfje | 外币贷方金额 | numeric | 23 | 4 |  | null | 外币贷方金额 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcn | 出纳 | varchar | 200 |  | √ | ' ' | 出纳 |
| 8 | fkjqjxllb | fkjqjxllb | varchar | 50 |  | √ | ' ' |  |
| 9 | fkjqj | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间,枚举: 01 :1 02 :2 03 :3 04 :4 05 :5 06 :6 07 :7 08 :8 09 :9 10 :10 11 :11 12 :12 |
| 10 | fjfje | 借方金额 | numeric | 23 | 4 |  | null | 借方金额 |
| 11 | fzdr | 制单人 | varchar | 200 |  | √ | ' ' | 制单人 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fjzr | 记账人 | varchar | 200 |  | √ | ' ' | 记账人 |
| 14 | fflh | 分录号 | int8 | 64 |  | √ | 0 | 分录号 |
| 15 | fwbbz | 外币币种 | varchar | 100 |  | √ | ' ' | 外币币种 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fkmdm | 科目代码 | int8 | 64 |  | √ | 0 | [科目 tcvvt_clique_account](../tcvvt_files/tcvvt_clique_account.md) |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fflzy | 分录摘要 | varchar | 2000 |  | √ | ' ' | 分录摘要 |
| 22 | ffjs | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 23 | fshr | 审核人 | varchar | 200 |  | √ | ' ' | 审核人 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdfje | 贷方金额 | numeric | 23 | 4 |  | null | 贷方金额 |
| 26 | fnddm | 年度代码 | varchar | 4 |  | √ | ' ' | 年度代码 |
| 27 | fyear | 年度代码 | timestamp | 0 |  |  | null | 年度代码 |
| 28 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 0 :手工新增 1 :自动采集 |
| 29 | fpzz | 凭证字（类型） | varchar | 50 |  | √ | ' ' | 凭证字（类型） |
| 30 | fpzrq | 凭证日期 | timestamp | 0 |  |  | null | 凭证日期 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_voucher_fkmdm |  | fkmdm |
| 2 | idx_tcvvt_voucher_fpzh |  | fpzh |
| 3 | idx_tcvvt_voucher_fpzrq |  | fpzrq |
| 4 | idx_tcvvt_voucher_fbizkey |  | forgid,fnddm,fkjqj |
| 5 | pk_tcvvt_voucher |  | fid |
