# 核销扩展设置-ap_settle_ext_setting

## 核销记录扩展分录-子表 t_ap_record_extentry

- **表名称：** 核销记录扩展分录-子表
- **表名：** t_ap_record_extentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frecordbillkeyname | 单据属性名称 | varchar | 50 |  | √ | ' ' | 单据属性名称 |
| 3 | frecordsettlekey | 对应核销记录单据头属性名 | varchar | 50 |  | √ | ' ' | 对应核销记录单据头属性名 |
| 4 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 5 | frecordkeyplace | 单据标识所在位置 | varchar | 50 |  | √ | ' ' | 单据标识所在位置,枚举: head :单据头 entry :分录 |
| 6 | frecordbillkey | 单据属性标识 | varchar | 50 |  | √ | ' ' | 单据属性标识 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_record_extentry_pkey |  | fentryid |
| 2 | idx_ap_s_r_s_e_fid |  | fid |

---

## 核销记录生成核销单条件配置-多语言表 t_ap_settlebill_condition_l

- **表名称：** 核销记录生成核销单条件配置-多语言表
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

## 核销记录生成核销单条件配置-子表 t_ap_settlebill_condition

- **表名称：** 核销记录生成核销单条件配置-子表
- **表名：** t_ap_settlebill_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 4 | fcondition_tag | 生成核销单的条件设置_详情 | text | 0 |  |  | null | 生成核销单的条件设置_详情 |
| 5 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 recclearing :收款清理 recrefundclearing :收款退款清理 appaysettle :应付付款核销 liqsettle :应付清理 paytrans :应付转销 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 payclearing :付款清理 payrefundclearing :付款退款清理 |
| 6 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :创建 B :审核中 C :已审核 |
| 10 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 11 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
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

---

## 核销单生成条件-多选基础资料表 t_ap_settlebill_rules

- **表名称：** 核销单生成条件-多选基础资料表
- **表名：** t_ap_settlebill_rules

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [核销记录生成核销单条件 ap_settle_ext_condition](../ap_files/ap_settle_ext_condition.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_settlebillrules_bid |  | fbasedataid |
| 2 | idx_ap_settlebillrules_entryid |  | fentryid |
| 3 | pk_t_ap_settlebill_rules |  | fpkid |

---

## 核销扩展设置-多语言表 t_ap_settle_ext_l

- **表名称：** 核销扩展设置-多语言表
- **表名：** t_ap_settle_ext_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settle_ext_l_pkey |  | fpkid |
| 2 | idx_ap_settle_ext_fid |  | fid,flocaleid |

---

## 核销记录生成核销单规则-子表 t_ap_settlebill_rule

- **表名称：** 核销记录生成核销单规则-子表
- **表名：** t_ap_settlebill_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlerelation | 核销关系 | varchar | 30 |  | √ | ' ' | 核销关系,枚举: recsettle :应收收款核销 arself :应收红蓝对冲 artransfer :应收转销 arapsettle :应收冲应付 arwriteoff :应收红蓝冲销 baddebtloss :坏账损失 baddebtrecovery :坏账收回 recpaysettle :收款冲退款 arpaysettle :应收退款核销 arliqsettle :应收清理 recclearing :收款清理 recrefundclearing :收款退款清理 recself :收款红蓝对冲 appaysettle :应付付款核销 liqsettle :应付清理 paytrans :应付转销 payself :付款红蓝对冲 apself :应付红蓝对冲 aparsettle :应付冲应收 apwriteoff :应付红蓝冲销 payrecsettle :付款冲退款 aprecsettle :应付退款核销 transwar :转出质保金 payclearing :付款清理 payrefundclearing :付款退款清理 |
| 3 | fadjustcondition | 汇兑损益生成核销单 | bpchar | 1 |  | √ | '1' | 汇兑损益生成核销单 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fconditionid | 核销单生成条件 | int8 | 64 |  | √ | 0 | [核销记录生成核销单条件 ap_settle_ext_condition](../ap_files/ap_settle_ext_condition.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_settlebill_rule |  | fentryid |
| 2 | idx_ap_settlebillrule_fid |  | fid |

---

## 列表分录-子表 t_ap_settle_extentrylist

- **表名称：** 列表分录-子表
- **表名：** t_ap_settle_extentrylist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fsettlebillkeyname | 手工核销对应属性列名称 | varchar | 50 |  | √ | ' ' | 手工核销对应属性列名称 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fbillkeyplace | 单据标识所在位置 | varchar | 50 |  | √ | 'head' | 单据标识所在位置,枚举: head :单据头 entry :分录 detailentry :物料行分录 planentry :计划行分录 |
| 6 | fbillkey | 单据属性标识 | varchar | 50 |  | √ | ' ' | 单据属性标识 |
| 7 | fbillkeyname | 单据属性名称 | varchar | 50 |  | √ | ' ' | 单据属性名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_s_s_e_el_fid |  | fid |
| 2 | t_ap_settle_extentrylist_pkey |  | fentryid |

---

## 过滤分录-子表 t_ap_settle_extentry

- **表名称：** 过滤分录-子表
- **表名：** t_ap_settle_extentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fmatchfieldkey | 匹配属性标识 | varchar | 255 |  | √ | ' ' | 匹配属性标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffieldkeyname | 单据属性名称 | varchar | 50 |  | √ | ' ' | 单据属性名称 |
| 7 | ffieldkey | 单据属性标识 | varchar | 50 |  | √ | ' ' | 单据属性标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settle_extentry_pkey |  | fentryid |
| 2 | idx_ap_s_e_e_fid |  | fid |

---

## 核销扩展设置-主表 t_ap_settle_ext

- **表名称：** 核销扩展设置-主表
- **表名：** t_ap_settle_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frunconditionvalue | 过滤条件配置 | varchar | 255 |  | √ | ' ' | 过滤条件配置 |
| 5 | frunconditionvalue_tag | 过滤条件配置_详情 | text | 0 |  |  | null | 过滤条件配置_详情 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settle_ext_pkey |  | fid |
| 2 | idx_ap_settle_ext_fnumber |  | fnumber |
