# 开函登记-gm_letterofguarantee_f7

## 开函登记-主表 t_gm_letterofguarantee

- **表名称：** 开函登记-主表
- **表名：** t_gm_letterofguarantee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fgenreceiveletter | fgenreceiveletter | bpchar | 1 |  | √ | '0' |  |
| 4 | fapplyreissueorgid | 申请转开公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fguaranteeterm | 保函期限 | varchar | 50 |  | √ | ' ' | 保函期限 |
| 6 | festimatedtotalfee | 预计保函总费用 | numeric | 19 | 6 | √ | 0 | 预计保函总费用 |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fguaranteetypeid | 保函类型 | int8 | 64 |  | √ | 0 | [保函类型 gm_guaranteetype](../gm_files/gm_guaranteetype.md) |
| 9 | fclaimdate | 索赔日期 | timestamp | 0 |  |  | null | 索赔日期 |
| 10 | flocalreissuebankid | 当地转开行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fsourcebilltype | fsourcebilltype | varchar | 80 |  | √ | ' ' |  |
| 13 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbeneficiaryid | fbeneficiaryid | int8 | 64 |  | √ | 0 |  |
| 15 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 16 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | funfrozenfundbankid | funfrozenfundbankid | int8 | 64 |  | √ | 0 |  |
| 18 | fisreissue | 银行转开 | bpchar | 1 |  | √ | '0' | 银行转开 |
| 19 | ftextbeneficiary | 保函受益人 | varchar | 255 |  | √ | ' ' | 保函受益人 |
| 20 | fstartdate | 开函起始日 | timestamp | 0 |  |  | null | 开函起始日 |
| 21 | fcanceldate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 22 | fguaranteeno | 保函编号 | varchar | 255 |  | √ | ' ' | 保函编号 |
| 23 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 other :其他 none :信用/无担保 |
| 24 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 25 | ffinorginfoid | 金融机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | ffeepaymentmethod | 保函费用支付方式 | varchar | 80 |  | √ | ' ' | 保函费用支付方式,枚举: ML :按月 QL :按季 HY :按半年 YL :按年 EO :到期一次性支付 IO :开具时一次性支付 |
| 27 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: registering :登记中 registered :已登记 cancelled :已注销 claimed :已索赔 changing :改函中 |
| 28 | fpayeebillno | fpayeebillno | varchar | 80 |  | √ | ' ' |  |
| 29 | famount | 保函金额 | numeric | 19 | 6 | √ | 0 | 保函金额 |
| 30 | fcancelledtime | fcancelledtime | timestamp | 0 |  |  | null |  |
| 31 | fbeneficiarytype | 受益人类型 | varchar | 80 |  | √ | ' ' | 受益人类型,枚举: bos_org :公司 bos_user :职员 other :其他 bd_customer :客户 bd_supplier :供应商 |
| 32 | fguaranteevarietyid | 保函品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 33 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 34 | fexpiredate | 开函到期日 | timestamp | 0 |  |  | null | 开函到期日 |
| 35 | freissuebankfeerate | 转开银行保函费率（%） | numeric | 19 | 6 | √ | 0 | 转开银行保函费率（%） |
| 36 | fapplybillno | fapplybillno | varchar | 80 |  | √ | ' ' |  |
| 37 | fisrevokableinadv | fisrevokableinadv | bpchar | 1 |  | √ | '0' |  |
| 38 | fcomprehfeerate | 综合保函费率（%） | numeric | 19 | 6 | √ | 0 | 综合保函费率（%） |
| 39 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 40 | fapplyorgid | 保函申请人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 42 | fguaranteepurpose | 保函用途 | varchar | 255 |  | √ | ' ' | 保函用途 |
| 43 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 44 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 45 | fcancelledbyid | fcancelledbyid | int8 | 64 |  | √ | 0 |  |
| 46 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 47 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 48 | fhasunfrozenfund | fhasunfrozenfund | bpchar | 1 |  | √ | '0' |  |
| 49 | fissuebankfeerate | 开立银行保函费率（%） | numeric | 19 | 6 | √ | 0 | 开立银行保函费率（%） |
| 50 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 51 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguarantee |  | fid |
| 2 | idx_gm_letterofguaran_orgbiz |  | forgid,fbizdate |

---

## 单据体-子表 t_gm_beneficiary_entry

- **表名称：** 单据体-子表
- **表名：** t_gm_beneficiary_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftextbeneficiary | 保函受益人 | varchar | 255 |  | √ | ' ' | 保函受益人 |
| 3 | fbeneficiary | 受益人id | int8 | 64 |  | √ | 0 | 受益人id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fbeneficiarytype | 受益人类型 | varchar | 80 |  | √ | ' ' | 受益人类型,枚举: bos_org :公司 bos_user :职员 other :其他 bd_customer :客户 bd_supplier :供应商 |

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

## 开函登记-多语言表 t_gm_letterofguarantee_l

- **表名称：** 开函登记-多语言表
- **表名：** t_gm_letterofguarantee_l

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
| 1 | idx_gm_letterof_guaran_l_fid |  | fid |
| 2 | pk_gm_letterofguarantee_l |  | fpkid |
