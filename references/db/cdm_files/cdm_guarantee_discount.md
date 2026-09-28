# 票据保贴处理-cdm_guarantee_discount

## 票据保贴处理-关联追踪表 t_cdm_guarantee_discount_tc

- **表名称：** 票据保贴处理-关联追踪表
- **表名：** t_cdm_guarantee_discount_tc

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
| 1 | pk_cdm_guarantee_discount_tc |  | fid |
| 2 | idx_cdm_guarantee_discount_tc_tbill |  | ftbillid |
| 3 | idx_cdm_guarantee_discount_tc_tid |  | ftid |

---

## 关联子实体-子表 t_cdm_guarantee_discount_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_guarantee_discount_lk

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
| 1 | idx_cdm_guarantee_discount_lk_fk |  | fid |
| 2 | pk_cdm_guarantee_discount_lk |  | fpkid |

---

## 单据体-子表 t_cdm_guarante_draftentry

- **表名称：** 单据体-子表
- **表名：** t_cdm_guarante_draftentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentryguarantortext | 保贴对象 | varchar | 100 |  | √ | ' ' | 保贴对象 |
| 3 | fentrybizdate | 保贴登记日期 | timestamp | 0 |  |  | null | 保贴登记日期 |
| 4 | fentrycreditlimitorg | 保贴授信机构 | varchar | 100 |  | √ | ' ' | 保贴授信机构 |
| 5 | fentryguaranttype | 保贴对象类型 | varchar | 30 |  | √ | ' ' | 保贴对象类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_user :职员 other :其他 |
| 6 | fentrycreditamount | 占用授信金额 | numeric | 19 | 6 | √ | 0 | 占用授信金额 |
| 7 | fentrycreditlimit | 占用授信 | varchar | 100 |  | √ | ' ' | 占用授信 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fguaranteeid | 保贴登记id | int8 | 64 |  | √ | 0 | 保贴登记id |
| 10 | fcreditamount | 占用授信金额 | numeric | 19 | 6 | √ | 0 | 占用授信金额 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fdraftbillid | 票据号码 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_guarantee_discount_fid |  | fid |
| 2 | pk_t_cdm_guarante_draftentry |  | fentryid |

---

## 票据保贴处理-反写记录表 t_cdm_guarantee_discount_wb

- **表名称：** 票据保贴处理-反写记录表
- **表名：** t_cdm_guarantee_discount_wb

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
| 1 | pk_cdm_guarantee_discount_wb |  | fentryid |
| 2 | idx_cdm_guarantee_discount_wb_fk |  | fid |

---

## 票据保贴处理-主表 t_cdm_guarantee_discount

- **表名称：** 票据保贴处理-主表
- **表名：** t_cdm_guarantee_discount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreditactualamount | 实际占用授信金额 | numeric | 19 | 6 | √ | 0 | 实际占用授信金额 |
| 3 | fcredittotalamount | 占用授信额度合计 | numeric | 19 | 6 | √ | 0 | 占用授信额度合计 |
| 4 | ftradetype | ftradetype | varchar | 30 |  | √ | ' ' |  |
| 5 | fdrafttypeid | 票据类型 | int8 | 64 |  | √ | 0 | [票据类型 cdm_billtype](../cdm_files/cdm_billtype.md) |
| 6 | famount | famount | numeric | 19 | 6 | √ | 0 |  |
| 7 | ftradebillno | ftradebillno | varchar | 80 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbiztype | 业务分类 | varchar | 30 |  | √ | ' ' | 业务分类,枚举: guarantee :保贴登记 unguarantee :解除保贴登记 accepterguarantee :承兑人保贴 unaccepterguarantee :解除承兑人保贴 |
| 10 | fcredittype | 授信类别 | int8 | 64 |  | √ | 0 | [授信类别 cfm_credittype](../creditm_files/cfm_credittype.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fdiscountorg | 贴现机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 13 | fcreditcurrency | 授信币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fguaranteetype | 保贴对象类型 | varchar | 30 |  | √ | ' ' | 保贴对象类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 bos_user :职员 other :其他 |
| 15 | fguarantorid | 保贴对象 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 16 | fguarantortext | 保贴对象 | varchar | 100 |  | √ | ' ' | 保贴对象 |
| 17 | fcount | 票据张数 | int4 | 32 |  | √ | 0 | 票据张数 |
| 18 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 19 | fsupportbankdraft | 支持保贴银票 | bpchar | 1 |  | √ | '0' | 支持保贴银票 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fdescription | fdescription | varchar | 600 |  | √ | ' ' |  |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fcreditlimitorg | 保贴授信机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | fbizdate | fbizdate | timestamp | 0 |  |  | null |  |
| 27 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 28 | frptype | 收付类型 | varchar | 30 |  | √ | ' ' | 收付类型,枚举: paybill :开票 receivebill :收票 |
| 29 | fguaranteebasetype | 保贴对象基础资料类型 | varchar | 50 |  | √ | ' ' | 保贴对象基础资料类型,枚举: bd_customer :客户 bd_supplier :供应商 bos_user :职员 bos_org :业务单元 |
| 30 | fcurrencyid | fcurrencyid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 33 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_guarantee_billno |  | fbillno |
| 2 | pk_t_cdm_guarantee_discount |  | fid |

---

## 关联子实体-子表 t_cdm_guarante_draftentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cdm_guarante_draftentry_lk

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
| 1 | pk_cdm_guarante_draftentry_lk |  | fpkid |
| 2 | idx_cdm_guarante_draftentry_lk_fk |  | fentryid |
