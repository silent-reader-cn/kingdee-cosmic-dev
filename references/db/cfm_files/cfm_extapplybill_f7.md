# 展期申请-cfm_extapplybill_f7

## 展期申请-主表 t_cfm_extendapplybill

- **表名称：** 展期申请-主表
- **表名：** t_cfm_extendapplybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freferrateid | freferrateid | int8 | 64 |  | √ | 0 |  |
| 3 | frateadjustcycle | frateadjustcycle | int8 | 64 |  | √ | 0 |  |
| 4 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | frenewalinterestrate | frenewalinterestrate | numeric | 23 | 10 | √ | 0 |  |
| 6 | fnotrepayamount | fnotrepayamount | numeric | 23 | 10 | √ | 0 |  |
| 7 | famount | 借款金额 | numeric | 23 | 10 | √ | 0 | 借款金额 |
| 8 | frateadjustcycletype | frateadjustcycletype | varchar | 50 |  | √ | ' ' |  |
| 9 | frenewalexpiredate | frenewalexpiredate | timestamp | 0 |  |  | null |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fdrawamount | fdrawamount | numeric | 23 | 10 | √ | 0 |  |
| 14 | fbusinessstatus | fbusinessstatus | varchar | 50 |  | √ | ' ' |  |
| 15 | fratefloatpoint | fratefloatpoint | numeric | 16 | 6 | √ | 0 |  |
| 16 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 17 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fprevrenewalexpiredate | fprevrenewalexpiredate | timestamp | 0 |  |  | null |  |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fapplydate | fapplydate | timestamp | 0 |  |  | null |  |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fproductfactoryid | fproductfactoryid | int8 | 64 |  | √ | 0 |  |
| 24 | floancontractbillid | 合同单据编号 | int8 | 64 |  | √ | 0 | [借款合同 cfm_loancontractbill_f7](../cfm_files/cfm_loancontractbill_f7.md) |
| 25 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 26 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 27 | fisadjustinterestrate | fisadjustinterestrate | bpchar | 1 |  | √ | '0' |  |
| 28 | frateadjuststyle | frateadjuststyle | varchar | 50 |  | √ | ' ' |  |
| 29 | floantype | floantype | varchar | 50 |  | √ | ' ' |  |
| 30 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 31 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 32 | fcurrencyid | 借款币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 33 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 34 | fratesign | fratesign | varchar | 50 |  | √ | ' ' |  |
| 35 | fprotocolno | fprotocolno | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_extendapplybill |  | fbillno,fbillstatus |
| 2 | pk_cfm_extendapplybill |  | fid |

---

## 展期申请-多语言表 t_cfm_extendapplybill_l

- **表名称：** 展期申请-多语言表
- **表名：** t_cfm_extendapplybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_extendapplybill_l |  | fpkid |
| 2 | idx_cfm_extendapplybill_l |  | fid |
