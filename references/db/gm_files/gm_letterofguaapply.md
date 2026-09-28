# 业务申请-gm_letterofguaapply

## 担保信息分录-子表 t_gm_guaranteeuse_info

- **表名称：** 担保信息分录-子表
- **表名：** t_gm_guaranteeuse_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcreditortext | fgcreditortext | varchar | 80 |  | √ | ' ' |  |
| 3 | fgcreditguarantee | 额度担保 | bpchar | 1 |  | √ | '0' | 额度担保 |
| 4 | fgsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fgcontractcurrency | 担保合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 8 | fgcreditorid | fgcreditorid | int8 | 64 |  | √ | 0 |  |
| 9 | fgcontractid | 担保/保证合同编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 10 | fgsrcbilltype | 来源单据 | varchar | 80 |  | √ | ' ' | 来源单据 |
| 11 | fgcurrencyid | fgcurrencyid | int8 | 64 |  | √ | 0 |  |
| 12 | fgstatus | 状态 | varchar | 80 |  | √ | ' ' | 状态,枚举: A :担保中 C :已解除 |
| 13 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 14 | fgratio | 担保比例(%) | numeric | 19 | 6 | √ | 0 | 担保比例(%) |
| 15 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fgcreditortype | fgcreditortype | varchar | 50 |  | √ | ' ' |  |
| 18 | fgcontractamount | 担保合同金额 | numeric | 19 | 6 | √ | 0 | 担保合同金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_info_efid |  | fid |
| 2 | pk_t_gm_guaranteeuse_info |  | fentryid |

---

## 业务申请-多语言表 t_gm_letterofguaapply_l

- **表名称：** 业务申请-多语言表
- **表名：** t_gm_letterofguaapply_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguaapply_l |  | fpkid |
| 2 | idx_gm_letterofguaap_l_fid |  | fid |

---

## 单据体-子表 t_gm_beneficiary_entry

- **表名称：** 单据体-子表
- **表名：** t_gm_beneficiary_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextbeneficiary | 被担保人 | varchar | 255 |  | √ | ' ' | 被担保人 |
| 3 | fbeneficiary | 被担保人id | int8 | 64 |  | √ | 0 | 被担保人id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbeneficiarytype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :公司 bos_user :职员 other :其他 bd_customer :客户 bd_supplier :供应商 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_beneficiary_entry |  | fentryid |
| 2 | idx_gm_beneficiaryentry |  | fid |

---

## 业务申请-主表 t_gm_letterofguaapply

- **表名称：** 业务申请-主表
- **表名：** t_gm_letterofguaapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: registering :登记中 registered :已登记 cancelled :已注销 |
| 4 | famount | 保函金额 | numeric | 19 | 6 | √ | 0 | 保函金额 |
| 5 | fapplyreissueorgid | 申请转开公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fguaranteeterm | 保函期限 | varchar | 50 |  | √ | ' ' | 保函期限 |
| 7 | festimatedtotalfee | 预计保函总费用 | numeric | 19 | 6 | √ | 0 | 预计保函总费用 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fguaranteetypeid | 保函类型 | int8 | 64 |  | √ | 0 | [保函类型 gm_guaranteetype](../gm_files/gm_guaranteetype.md) |
| 10 | fbeneficiarytype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :公司 bos_user :职员 other :其他 bd_customer :客户 bd_supplier :供应商 |
| 11 | fguaranteevarietyid | 保函品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 12 | fbiztype | 业务类型 | varchar | 80 |  | √ | ' ' | 业务类型,枚举: open :开函 change :改函 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fletterofguaranteeid | 开函登记单据编号 | int8 | 64 |  | √ | 0 | [开函登记 gm_letterofguarantee_f7](../gm_files/gm_letterofguarantee_f7.md) |
| 15 | fexpiredate | 开函到期日 | timestamp | 0 |  |  | null | 开函到期日 |
| 16 | freissuebankfeerate | 转开银行保函费率（%） | numeric | 19 | 6 | √ | 0 | 转开银行保函费率（%） |
| 17 | flocalreissuebankid | 当地转开行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 18 | fisrevokableinadv | 可提前撤销 | bpchar | 1 |  | √ | '0' | 可提前撤销 |
| 19 | fcomprehfeerate | 综合保函费率（%） | numeric | 19 | 6 | √ | 0 | 综合保函费率（%） |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fapplyorgid | 保函申请人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fbeneficiaryid | 被担保人id | int8 | 64 |  | √ | 0 | 被担保人id |
| 26 | fguaranteepurpose | 保函用途 | varchar | 255 |  | √ | ' ' | 保函用途 |
| 27 | fislettercreated | 已登记开函 | bpchar | 1 |  | √ | '0' | 已登记开函 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 30 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 31 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 32 | funfrozenfundbankid | 解活资金对应银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 33 | fisreissue | 转开 | bpchar | 1 |  | √ | '0' | 转开 |
| 34 | ftextbeneficiary | 被担保人 | varchar | 255 |  | √ | ' ' | 被担保人 |
| 35 | fstartdate | 开函起始日 | timestamp | 0 |  |  | null | 开函起始日 |
| 36 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 37 | fhasunfrozenfund | 有解活资金 | bpchar | 1 |  | √ | '0' | 有解活资金 |
| 38 | fcreditgratio | 授信比例 | numeric | 19 | 6 | √ | 0 | 授信比例 |
| 39 | fissuebankfeerate | 开立银行保函费率（%） | numeric | 19 | 6 | √ | 0 | 开立银行保函费率（%） |
| 40 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 other :其他 none :信用/无担保 |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fcreditlimitid | 预占授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 44 | ffinorginfoid | 金融机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 45 | ffeepaymentmethod | 保函费用支付方式 | varchar | 80 |  | √ | ' ' | 保函费用支付方式,枚举: ML :按月 QL :按季 HY :按半年 YL :按年 EO :到期一次性支付 IO :开具时一次性支付 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguaapply |  | fid |
| 2 | idx_gm_letterofguaap_orgbiz |  | forgid,fbizdate |
