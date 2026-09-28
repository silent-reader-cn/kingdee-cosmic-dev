# 资金池核销记录-occba_verifyrecord

## 上账单据核销明细-子表 t_occba_vr_inentity

- **表名称：** 上账单据核销明细-子表
- **表名：** t_occba_vr_inentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finamount | 上账金额 | numeric | 23 | 10 | √ | 0 | 上账金额 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fverifyuseamount | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 4 | finsourceentryseq | 上账单据分录序号 | int4 | 32 |  | √ | 0 | 上账单据分录序号 |
| 5 | finsourceentryid | 上账单据分录ID | int8 | 64 |  | √ | 0 | 上账单据分录ID |
| 6 | fintime | 上账时间 | timestamp | 0 |  |  | null | 上账时间 |
| 7 | finitemid | 费用商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |
| 8 | finrecordid | 上账流水ID | int8 | 64 |  | √ | 0 | 上账流水ID |
| 9 | fexpensetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [营销费用类型 ocdbd_expensetype](../ocmem_files/ocdbd_expensetype.md) |
| 10 | finsourcebillid | 上账单据ID | int8 | 64 |  | √ | 0 | 上账单据ID |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 12 | finsourceentry | 上账来源单据分录 | varchar | 80 |  | √ | ' ' | 上账来源单据分录 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 14 | finsoucebill | 上账单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 15 | finsourcebillno | 上账单据编码 | varchar | 80 |  | √ | ' ' | 上账单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_vr_inentity |  | fdetailid |
| 2 | idx_occba_vr_inentity_eid |  | fentryid |

---

## 单据使用记录-子表 t_occba_vr_useentity

- **表名称：** 单据使用记录-子表
- **表名：** t_occba_vr_useentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcebillentryid | 关联订单明细行 | int8 | 64 |  | √ | 0 | 关联订单明细行 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fuseamount | 使用金额 | numeric | 23 | 10 | √ | 0 | 使用金额 |
| 5 | fverifyamount | 本次核销金额 | numeric | 23 | 10 | √ | 0 | 本次核销金额 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fitemid | 订单商品编码 | int8 | 64 |  | √ | 0 | [商品信息 ocdbd_iteminfo](../ocdbd_files/ocdbd_iteminfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_vr_useentity_fid |  | fid |
| 2 | pk_occba_vr_useentity |  | fentryid |

---

## 资金池核销记录-主表 t_occba_verifyrecord

- **表名称：** 资金池核销记录-主表
- **表名：** t_occba_verifyrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 核销状态 | bpchar | 1 |  | √ | 'A' | 核销状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftotalamount | 使用金额 | numeric | 23 | 10 | √ | 0 | 使用金额 |
| 6 | fsourceentryid | 关联来源单据分录id | int8 | 64 |  | √ | 0 | 关联来源单据分录id |
| 7 | fsettorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsourceentryseq | 来源单据分录序号 | int4 | 32 |  | √ | 0 | 来源单据分录序号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | faccounttypeid | 使用账户类型 | int8 | 64 |  | √ | 0 | [资金账户 ocdbd_incentiveaccount](../occba_files/ocdbd_incentiveaccount.md) |
| 13 | fsourcebillid | 关联来源单据id | int8 | 64 |  | √ | 0 | 关联来源单据id |
| 14 | fchannelid | 使用渠道 | int8 | 64 |  | √ | 0 | [渠道 ocdbd_channel](../ocdbd_files/ocdbd_channel.md) |
| 15 | fbillentity | 使用单对象 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fsourcebillno | 使用单编码 | varchar | 80 |  | √ | ' ' | 使用单编码 |
| 17 | ftotalveramount | 核销总金额 | numeric | 23 | 10 | √ | 0 | 核销总金额 |
| 18 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fverifydate | 核销日期 | timestamp | 0 |  |  | null | 核销日期 |
| 22 | fsourceentry | 来源单据分录标识 | varchar | 80 |  | √ | ' ' | 来源单据分录标识 |
| 23 | frebateaccountid | 使用资金池 | int8 | 64 |  | √ | 0 | [资金池余额 ocdbd_rebateaccount](../occba_files/ocdbd_rebateaccount.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occba_verifyrecord |  | fid |
| 2 | idx_occba_verifyrecord_no |  | fbillno |

---

## 关联子实体-子表 t_occba_vr_useentity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occba_vr_useentity_lk

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
| 1 | idx_occba_vr_useentity_lk_fk |  | fentryid |
| 2 | pk_occba_vr_useentity_lk |  | fpkid |

---

## 资金池核销记录-关联追踪表 t_occba_verifyrecord_tc

- **表名称：** 资金池核销记录-关联追踪表
- **表名：** t_occba_verifyrecord_tc

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
| 1 | pk_occba_verifyrecord_tc |  | fid |
| 2 | idx_occba_verifyrecord_tc_tid |  | ftid |
| 3 | idx_occba_verifyrecord_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_occba_verifyrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occba_verifyrecord_lk

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
| 1 | pk_occba_verifyrecord_lk |  | fpkid |
| 2 | idx_occba_verifyrecord_lk_fk |  | fid |

---

## 资金池核销记录-反写记录表 t_occba_verifyrecord_wb

- **表名称：** 资金池核销记录-反写记录表
- **表名：** t_occba_verifyrecord_wb

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
| 1 | idx_occba_verifyrecord_wb_fk |  | fid |
| 2 | pk_occba_verifyrecord_wb |  | fentryid |

---

## 关联子实体-子表 t_occba_vr_inentity_lk

- **表名称：** 关联子实体-子表
- **表名：** t_occba_vr_inentity_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occba_vr_inentity_lk_fk |  | fdetailid |
| 2 | pk_occba_vr_inentity_lk |  | fpkid |
