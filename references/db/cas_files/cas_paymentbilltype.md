# 付款用途-cas_paymentbilltype

## 付款用途-主表 t_cas_paymentbilltype

- **表名称：** 付款用途-主表
- **表名：** t_cas_paymentbilltype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | ffundflowitem | 默认资金用途 | int8 | 64 |  | √ | 0 | [资金用途 cas_fundflowitem](../cas_files/cas_fundflowitem.md) |
| 5 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fispartpayment | 参与应付核销 | bpchar | 1 |  | √ | '0' | 参与应付核销 |
| 8 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 9 | fispartreceivable | 参与应收核销 | bpchar | 1 |  | √ | '0' | 参与应收核销 |
| 10 | fispreset | 是否预设(弃用) | bpchar | 1 |  | √ | '0' | 是否预设(弃用) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fbiztype | 付款业务类型 | varchar | 30 |  | √ | ' ' | 付款业务类型,枚举: 201 :采购付款 202 :预付款 203 :退销售回款 204 :退预收款 205 :代付款 206 :退代收款 210 :个人借款 211 :费用报销 212 :资金上划 997 :工资支付 999 :其他 214 :同名转账 215 :现金存取 216 :资金下拨 217 :跨主体调拨 FK1001_SYS :其他预付 FK1004_SYS :退其他预收 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fisreturnbg | 返还预算 | bpchar | 1 |  | √ | '0' | 返还预算 |
| 17 | fissystem | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fenable | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :禁用 1 :启用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_pbt_fnumber |  | fnumber |
| 2 | t_cas_paymentbilltype_pkey |  | fid |

---

## 付款用途-多语言表 t_cas_paymentbilltype_l

- **表名称：** 付款用途-多语言表
- **表名：** t_cas_paymentbilltype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 300 |  |  | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_paymentbilltype_l_pkey |  | fpkid |
| 2 | idx_cas_pbtl_flocaleid |  | flocaleid |
| 3 | idx_cas_pbtl_fname |  | fname |
| 4 | idx_cas_pbtl_fpid |  | fid,flocaleid |

---

## 单据业务类型-多选基础资料表 t_cas_paymentbilltype_bt

- **表名称：** 单据业务类型-多选基础资料表
- **表名：** t_cas_paymentbilltype_bt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cas_paymentbilltype_bt |  | fpkid |
| 2 | idx_cas_paymentbilltype_bt |  | fid |
