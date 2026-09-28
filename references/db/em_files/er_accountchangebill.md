# 收款信息变更单-er_accountchangebill

## 收款信息（变更后）-子表 t_er_changeentry

- **表名称：** 收款信息（变更后）-子表
- **表名：** t_er_changeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangerow | 源单行号 | varchar | 50 |  | √ | ' ' | 源单行号 |
| 3 | fchangeothercontactunit | 其他往来单位 | int8 | 64 |  | √ | 0 | [其他往来单位 cas_othercontactunit](../cas_files/cas_othercontactunit.md) |
| 4 | fchangepayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fchangesupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 7 | fchangepayertype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 cas_othercontactunit :其他往来单位 |
| 8 | fchangebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 9 | fchangecasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fchangebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 11 | fchangepayerbank | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 12 | fchangepayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 13 | fchangebillid | 源单id | varchar | 50 |  | √ | ' ' | 源单id |
| 14 | fchangepayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 15 | fchangecustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 16 | fchangeamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 17 | fchangeentryid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fchangepayeerid | 收款人（个人） | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 20 | fchangecurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_changeentry |  | fentryid |
| 2 | idx_er_changeentry_fid |  | fid |

---

## 收款信息（变更前）-子表 t_er_originalentry

- **表名称：** 收款信息（变更前）-子表
- **表名：** t_er_originalentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourceamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 3 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 4 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 5 | fothercontactunit | 其他往来单位 | int8 | 64 |  | √ | 0 | [其他往来单位 cas_othercontactunit](../cas_files/cas_othercontactunit.md) |
| 6 | fpayertype | 收款人类型 | varchar | 50 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 cas_othercontactunit :其他往来单位 |
| 7 | fsourceentryid | 源单分录id | varchar | 50 |  | √ | ' ' | 源单分录id |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fsourcecurrency | 源分录币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fpayerbank | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 12 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 13 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 14 | fpayeerid | 收款人（个人） | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 15 | fsourcebillid | 源单id | varchar | 50 |  | √ | 0 | 源单id |
| 16 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 17 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fsourcebillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 20 | fsourcerow | 源单行号 | varchar | 50 |  | √ | ' ' | 源单行号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_origin_fid |  | fid |
| 2 | pk_er_originalentry |  | fentryid |

---

## 收款信息变更单-多语言表 t_er_accountchangebill_l

- **表名称：** 收款信息变更单-多语言表
- **表名：** t_er_accountchangebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_acchangebill_l_id |  | fid,flocaleid |
| 2 | pk_er_accountchangebill_l |  | fpkid |

---

## 收款信息变更单-主表 t_er_accountchangebill

- **表名称：** 收款信息变更单-主表
- **表名：** t_er_accountchangebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 H :废弃 I :关闭 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |
| 11 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fchangedate | 变更日期 | timestamp | 0 |  |  | null | 变更日期 |
| 14 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 15 | fnextauditor | 下一步审核人 | varchar | 200 |  | √ | ' ' | 下一步审核人 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_accountchangebill |  | fid |
| 2 | idx_er_accchange_fbillno |  | fbillno |
| 3 | idx_er_accchange_fapplyerid |  | fapplierid,fmodifytime |

---

## 关联子实体-子表 t_er_originalentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_originalentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_originalentry_lk_fk |  | fentryid |
| 2 | pk_er_originalentry_lk |  | fpkid |

---

## 收款信息变更单-反写记录表 t_er_accountchangebill_wb

- **表名称：** 收款信息变更单-反写记录表
- **表名：** t_er_accountchangebill_wb

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
| 1 | idx_er_accountchangebill_wb_fk |  | fid |
| 2 | pk_er_accountchangebill_wb |  | fentryid |

---

## 收款信息变更单-关联追踪表 t_er_accountchangebill_tc

- **表名称：** 收款信息变更单-关联追踪表
- **表名：** t_er_accountchangebill_tc

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
| 1 | idx_er_accountchangebill_tc_tbill |  | ftbillid |
| 2 | pk_er_accountchangebill_tc |  | fid |
| 3 | idx_er_accountchangebill_tc_tid |  | ftid |
