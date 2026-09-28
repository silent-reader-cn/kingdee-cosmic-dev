# 核销记录生成核销单条件-ap_settle_ext_condition

## 核销记录生成核销单条件-多语言表 t_ap_settlebill_condition_l

- **表名称：** 核销记录生成核销单条件-多语言表
- **表名：** t_ap_settlebill_condition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_settlebillcon_l_entryid |  | fentryid |
| 2 | pk_t_ap_settlebill_condition_l |  | fpkid |

---

## 核销记录生成核销单条件-主表 t_ap_settlebill_condition

- **表名称：** 核销记录生成核销单条件-主表
- **表名：** t_ap_settlebill_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcondition_tag | 生成核销单的条件设置_详情 | text | 0 |  |  | null | 生成核销单的条件设置_详情 |
| 5 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 recclearing :收款清理 recrefundclearing :收款退款清理 appaysettle :应付付款核销 liqsettle :应付清理 paytrans :应付转销 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 appaidsettle :采购期初预付 payclearing :付款清理 payrefundclearing :付款退款清理 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fcondition | 生成核销单的条件设置 | varchar | 255 |  | √ | ' ' | 生成核销单的条件设置 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_settlebill_condition |  | fentryid |
| 2 | idx_settlebillcon_masterid |  | fmasterid |
| 3 | idx_settlebillcon_number |  | fnumber |
| 4 | idx_settlebillcon_id |  | fid |
