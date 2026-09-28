# 内部账户冻结&#x2f;解冻-ifm_accountfrozen

## 内部账户冻结&#x2f;解冻-多语言表 t_ifm_accountfrozen_l

- **表名称：** 内部账户冻结&#x2f;解冻-多语言表
- **表名：** t_ifm_accountfrozen_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffrozenreason | 冻结/解冻原因 | varchar | 255 |  | √ | ' ' | 冻结/解冻原因 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_accountfrozen_l |  | fpkid |
| 2 | idx_t_ifm_accountfrozen_l_fid |  | fid |

---

## 内部账户冻结&#x2f;解冻-主表 t_ifm_accountfrozen

- **表名称：** 内部账户冻结&#x2f;解冻-主表
- **表名：** t_ifm_accountfrozen

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautothawbillid | 自动解冻冻结单据ID | int8 | 64 |  | √ | 0 | 自动解冻冻结单据ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ffrozenstatus | 冻结状态 | varchar | 30 |  | √ | ' ' | 冻结状态,枚举: freezing :冻结中 frozen :已冻结 thawing :解冻中 thawed :已解冻 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | ffrozenenddate | 冻结结束日期 | timestamp | 0 |  |  | null | 冻结结束日期 |
| 12 | ftotalfrozenamount | 累计已冻结金额 | numeric | 23 | 10 | √ | 0 | 累计已冻结金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | ffrozentype | 冻结/解冻类型 | varchar | 30 |  | √ | ' ' | 冻结/解冻类型,枚举: account_frozen :账户冻结 account_thaw :账户解冻 amount_frozen :金额冻结 amount_thaw :金额解冻 |
| 15 | ffrozenreason | 冻结/解冻原因 | varchar | 255 |  | √ | ' ' | 冻结/解冻原因 |
| 16 | ffrozenamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 17 | fcapitalorgid | 资金组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | faccountid | 内部账户 | int8 | 64 |  | √ | 0 | 内部账户管理 ifm_inneracct |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ifm_accountfrozen_forgid |  | forgid |
| 2 | pk_t_ifm_accountfrozen |  | fid |
| 3 | idx_t_ifm_accountfrozen_faccountid |  | faccountid |
