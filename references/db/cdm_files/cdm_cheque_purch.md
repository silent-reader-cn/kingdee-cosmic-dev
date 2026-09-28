# 票据购置-cdm_cheque_purch

## 票据购置-多语言表 t_cdm_cheque_l

- **表名称：** 票据购置-多语言表
- **表名：** t_cdm_cheque_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 100 |  | √ | ' ' | pkid |
| 4 | finvalidmark | 作废原因 | varchar | 510 |  | √ | ' ' | 作废原因 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cdm_cheque_l_pkey |  | fpkid |
| 2 | idx_t_cdm_cheque_l_fid |  | fid |

---

## 票据购置-主表 t_cdm_cheque

- **表名称：** 票据购置-主表
- **表名：** t_cdm_cheque

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpurchdate | 购入日期 | timestamp | 0 |  |  | null | 购入日期 |
| 3 | ffilldate | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 4 | finvaliddate | 作废日期 | timestamp | 0 |  |  | null | 作废日期 |
| 5 | frelatebillnumber | 关联单据编号 | varchar | 100 |  | √ | ' ' | 关联单据编号 |
| 6 | fpurchase | 购置人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | famount | 张数 | int8 | 64 |  | √ | 0 | 张数 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | freplacechar | 通配符 | varchar | 10 |  | √ | ' ' | 通配符,枚举: * :* & :& @ :@ # :# |
| 11 | frelatebilltype | 关联单据类型 | varchar | 100 |  | √ | ' ' | 关联单据类型,枚举: cdm_payablebill :开票登记 |
| 12 | fcoderule | 编码规则 | varchar | 128 |  | √ | ' ' | 编码规则 |
| 13 | finvaliduser | 作废人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | frelateamount | 关联金额 | numeric | 19 | 6 | √ | 0.000000 | 关联金额 |
| 15 | finvalidmark | finvalidmark | varchar | 510 |  | √ | ' ' |  |
| 16 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 17 | fstartno | 起始流水号 | int8 | 64 |  | √ | 0 | 起始流水号 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fbatchno | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | frelatebillid | 关联单据ID | int8 | 64 |  | √ | 0 | 关联单据ID |
| 22 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fbank | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 24 | ffilluser | 填开人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | faccountbank | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 27 | cfbillstatus | 单据状态 | varchar | 10 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fchequestatus | 支票使用状态 | varchar | 30 |  | √ | ' ' | 支票使用状态,枚举: 0 :空白 1 :已领用 2 :已填开 3 :已作废 |
| 29 | fpurchorg | 购置组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 31 | fbilltype | fbilltype | varchar | 60 |  | √ | ' ' |  |
| 32 | fbilltypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cdm_cheque_purchorg |  | fpurchorg |
| 2 | idx_t_cdm_cheque_billno |  | fbillno |
| 3 | t_cdm_cheque_pkey |  | fid |
| 4 | idx_t_cdm_cheque_accountbank |  | faccountbank |
