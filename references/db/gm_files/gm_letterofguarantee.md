# 开函登记-gm_letterofguarantee

## 关联子实体-子表 t_gm_letterofguarantee_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gm_letterofguarantee_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguarantee_lk |  | fpkid |
| 2 | idx_gm_letterofguarantee_lk_fk |  | fid |

---

## 开函登记-主表 t_gm_letterofguarantee

- **表名称：** 开函登记-主表
- **表名：** t_gm_letterofguarantee

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fgenreceiveletter | 生成收函单 | bpchar | 1 |  | √ | '0' | 生成收函单 |
| 4 | fapplyreissueorgid | 申请转开公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fguaranteeterm | 保函期限 | varchar | 50 |  | √ | ' ' | 保函期限 |
| 6 | festimatedtotalfee | 预计保函总费用 | numeric | 19 | 6 | √ | 0 | 预计保函总费用 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fguaranteetypeid | 保函类型 | int8 | 64 |  | √ | 0 | [保函类型 gm_guaranteetype](../gm_files/gm_guaranteetype.md) |
| 9 | fclaimdate | 索赔日期 | timestamp | 0 |  |  | null | 索赔日期 |
| 10 | flocalreissuebankid | 当地转开行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fsourcebilltype | 源单类型 | varchar | 80 |  | √ | ' ' | 源单类型,枚举: 开函申请 :gm_letterofguaapply |
| 13 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbeneficiaryid | 被担保人id | int8 | 64 |  | √ | 0 | 被担保人id |
| 15 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 16 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | funfrozenfundbankid | 解活资金对应银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 18 | fisreissue | 转开 | bpchar | 1 |  | √ | '0' | 转开 |
| 19 | ftextbeneficiary | 被担保人 | varchar | 255 |  | √ | ' ' | 被担保人 |
| 20 | fstartdate | 开函起始日 | timestamp | 0 |  |  | null | 开函起始日 |
| 21 | fcanceldate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 22 | fguaranteeno | 保函编号 | varchar | 255 |  | √ | ' ' | 保函编号 |
| 23 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 other :其他 none :信用/无担保 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | ffinorginfoid | 金融机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | ffeepaymentmethod | 保函费用支付方式 | varchar | 80 |  | √ | ' ' | 保函费用支付方式,枚举: ML :按月 QL :按季 HY :按半年 YL :按年 EO :到期一次性支付 IO :开具时一次性支付 |
| 27 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: registering :登记中 registered :已登记 cancelled :已注销 claimed :已索赔 changing :改函中 |
| 28 | fpayeebillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 29 | famount | 保函金额 | numeric | 19 | 6 | √ | 0 | 保函金额 |
| 30 | fcancelledtime | 注销操作日期 | timestamp | 0 |  |  | null | 注销操作日期 |
| 31 | fbeneficiarytype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :公司 bos_user :职员 other :其他 bd_customer :客户 bd_supplier :供应商 |
| 32 | fguaranteevarietyid | 保函品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fexpiredate | 开函到期日 | timestamp | 0 |  |  | null | 开函到期日 |
| 35 | freissuebankfeerate | 转开银行保函费率（%） | numeric | 19 | 6 | √ | 0 | 转开银行保函费率（%） |
| 36 | fapplybillno | 保函申请 | varchar | 80 |  | √ | ' ' | 保函申请 |
| 37 | fisrevokableinadv | 可提前撤销 | bpchar | 1 |  | √ | '0' | 可提前撤销 |
| 38 | fcomprehfeerate | 综合保函费率（%） | numeric | 19 | 6 | √ | 0 | 综合保函费率（%） |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fapplyorgid | 保函申请人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | fguaranteepurpose | 保函用途 | varchar | 255 |  | √ | ' ' | 保函用途 |
| 43 | fcontractamount | 合同金额 | numeric | 19 | 6 | √ | 0 | 合同金额 |
| 44 | fcontractno | 合同号 | varchar | 255 |  | √ | ' ' | 合同号 |
| 45 | fcancelledbyid | 注销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 47 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 48 | fhasunfrozenfund | 有解活资金 | bpchar | 1 |  | √ | '0' | 有解活资金 |
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

## 开函登记-反写记录表 t_gm_letterofguarantee_wb

- **表名称：** 开函登记-反写记录表
- **表名：** t_gm_letterofguarantee_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguarantee_wb |  | fentryid |
| 2 | idx_gm_letterofguarantee_wb_fk |  | fid |

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

## 开函登记-分表 t_gm_letterofguarantee_e

- **表名称：** 开函登记-分表
- **表名：** t_gm_letterofguarantee_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feassrcid | eas数据id | varchar | 50 |  | √ | ' ' | eas数据id |
| 3 | flockpayamt | 付款锁定金额 | numeric | 23 | 10 | √ | 0 | 付款锁定金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguarantee_e |  | fid |
| 2 | idx_gm_letterofgua_feassrcid |  | feassrcid |

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

---

## 开函登记-关联追踪表 t_gm_letterofguarantee_tc

- **表名称：** 开函登记-关联追踪表
- **表名：** t_gm_letterofguarantee_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gm_letterofguarantee_tc |  | fid |
| 2 | idx_gm_letterofguarantee_tc_tbill |  | ftbillid |
| 3 | idx_gm_letterofguarantee_tc_tid |  | ftid |
