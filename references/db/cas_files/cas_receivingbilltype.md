# 收款用途-cas_receivingbilltype

## 收款用途-多语言表 t_cas_receivingbilltype_l

- **表名称：** 收款用途-多语言表
- **表名：** t_cas_receivingbilltype_l

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
| 1 | t_cas_receivingbilltype_l_pkey |  | fpkid |
| 2 | idx_cas_rbtl_fpid |  | fid,flocaleid |

---

## 收款用途-主表 t_cas_receivingbilltype

- **表名称：** 收款用途-主表
- **表名：** t_cas_receivingbilltype

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
| 13 | fbiztype | 收款业务类型 | varchar | 30 |  | √ | ' ' | 收款业务类型,枚举: 100 :销售回款 101 :预收款 102 :退采购付款 103 :退预付款 104 :代收款 105 :退代付款 106 :资金下拨 107 :虚拟收款 108 :结算中心收款 999 :其他 SK1001_SYS :其他预收 SK1002_SYS :退其他预付 |
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
| 1 | idx_cas_rbt_fnumber |  | fnumber |
| 2 | t_cas_receivingbilltype_pkey |  | fid |

---

## 单据业务类型-多选基础资料表 t_cas_receivingbilltyp_bt

- **表名称：** 单据业务类型-多选基础资料表
- **表名：** t_cas_receivingbilltyp_bt

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
| 1 | idx_cas_receivingbilltyp_bt |  | fid |
| 2 | pk_cas_receivingbilltyp_bt |  | fpkid |
