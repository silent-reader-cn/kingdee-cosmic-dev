# 预缴申报台账单据-tcvat_project_account

## 单据体-子表 t_tcvat_account_entry

- **表名称：** 单据体-子表
- **表名：** t_tcvat_account_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprepayrate | 预征率 | varchar | 50 |  | √ | ' ' | 预征率 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fprepaybase | 预缴基数 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴基数 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ftaxtype | 预缴税种 | varchar | 50 |  | √ | ' ' | 预缴税种 |
| 7 | fprepayamount | 预缴税额 | numeric | 23 | 10 | √ | 0.0000000000 | 预缴税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvat_account_entry_fk |  | fid |
| 2 | pk_tcvat_account_entry |  | fentryid |

---

## 预缴申报台账单据-主表 t_tcvat_project_account

- **表名称：** 预缴申报台账单据-主表
- **表名：** t_tcvat_project_account

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | faddress | 项目详细地址 | varchar | 100 |  | √ | ' ' | 项目详细地址 |
| 4 | fprojectid | 项目id | int8 | 64 |  | √ | 0 | 项目id |
| 5 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | flevytype | 征收方式 | varchar | 30 |  | √ | ' ' | 征收方式,枚举: normal :一般计税 simple :简易计税 |
| 8 | fsalesamount | 销售额 | numeric | 23 | 10 | √ | 0.0000000000 | 销售额 |
| 9 | fprojectzone | 项目所在地 | varchar | 50 |  | √ | ' ' | 项目所在地 |
| 10 | fdeductionamount | 扣除金额 | numeric | 23 | 10 | √ | 0.0000000000 | 扣除金额 |
| 11 | flicensecode | 建筑工程施工许可证编号 | varchar | 50 |  | √ | ' ' | 建筑工程施工许可证编号 |
| 12 | fenddate | 期止 | timestamp | 0 |  |  | null | 期止 |
| 13 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态 |
| 14 | fdeclareserialno | 申报编码 | varchar | 50 |  | √ | ' ' | 申报编码 |
| 15 | fstartdate | 期起 | timestamp | 0 |  |  | null | 期起 |
| 16 | fprepaytype | 预缴类型 | varchar | 30 |  | √ | ' ' | 预缴类型,枚举: VAT_YJXMLX_001 :异地建筑服务 VAT_YJXMLX_002 :建筑服务预收款 VAT_YJXMLX_003 :房地产项目预售 VAT_YJXMLX_004 :不动产转让 VAT_YJXMLX_005 :异地不动产出租 |
| 17 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 18 | ftaxoffice | 主管税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 19 | fapplicationno | 预缴申请单编号 | varchar | 50 |  | √ | ' ' | 预缴申请单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_project_account |  | fid |
| 2 | idx_tcvat_project_account |  | forgid,fstartdate,fserialno,fenddate |
