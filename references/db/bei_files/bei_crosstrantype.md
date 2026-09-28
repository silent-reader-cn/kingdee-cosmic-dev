# 银行交易类型-bei_crosstrantype

## 单据体-子表 t_bei_crosstrantype_entry

- **表名称：** 单据体-子表
- **表名：** t_bei_crosstrantype_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisnotnull | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 3 | ffieldname | 字段名称 | varchar | 80 |  | √ | ' ' | 字段名称 |
| 4 | fdefaultvalueid | 默认值主键 | int8 | 64 |  | √ | 0 | 默认值主键 |
| 5 | fissee | 可见 | bpchar | 1 |  | √ | '0' | 可见 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcomboxvalue | 枚举值 | varchar | 500 |  | √ | ' ' | 枚举值 |
| 8 | fislimitvalue | 限定有效值 | bpchar | 1 |  | √ | '0' | 限定有效值 |
| 9 | ffieldkey | 字段key | varchar | 80 |  | √ | ' ' | 字段key |
| 10 | fislimitlength | 控制长度 | bpchar | 1 |  | √ | '0' | 控制长度 |
| 11 | fvirtualvalue | 有效值 | varchar | 300 |  | √ | ' ' | 有效值 |
| 12 | ffieldtype | 字段类型 | varchar | 80 |  | √ | ' ' | 字段类型 |
| 13 | fmaxlength | 最大长度 | int8 | 64 |  | √ | 0 | 最大长度 |
| 14 | fbasedatatype | 基础资料类型 | varchar | 80 |  | √ | ' ' | 基础资料类型 |
| 15 | fdefaultvalue | 默认值 | varchar | 80 |  | √ | ' ' | 默认值 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_crosstrantype_entry |  | fid |
| 2 | t_bei_crosstrantype_entry_pkey |  | fentryid |

---

## 银行交易类型-主表 t_bei_crosstrantype

- **表名称：** 银行交易类型-主表
- **表名：** t_bei_crosstrantype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | freferencefee | 参考手续费 | int8 | 64 |  | √ | 0 | 参考手续费 |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcomment | 描述 | varchar | 750 |  | √ | ' ' | 描述 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fislimitsamebank | 限定同行交易 | bpchar | 1 |  | √ | '0' | 限定同行交易 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fispresetdata | 预设数据 | bpchar | 1 |  | √ | ' ' | 预设数据 |
| 12 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 13 | fbankcateid | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | ftimeliness | 时效类别 | varchar | 30 |  | √ | '0' | 时效类别,枚举: real :实时 near :准实时 work :工作时间 |
| 18 | fiscountry | 支持跨境交易/支持跨国家地区交易 | bpchar | 1 |  | √ | '0' | 支持跨境交易/支持跨国家地区交易 |
| 19 | fiscrosscurrency | 支持跨币种交易 | bpchar | 1 |  | √ | '0' | 支持跨币种交易 |
| 20 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fisdefault | 默认交易类型 | bpchar | 1 |  | √ | '0' | 默认交易类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_crosstrantype_pkey |  | fid |
| 2 | idx_t_bei_crosstrantype |  | fenable |

---

## 支持付款币种-多选基础资料表 t_bei_crosstrantype_cur

- **表名称：** 支持付款币种-多选基础资料表
- **表名：** t_bei_crosstrantype_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_crosstrantype_cur_pkey |  | fpkid |
| 2 | idx_bei_crosstrantype_cur |  | fid |

---

## 银行交易类型-多语言表 t_bei_crosstrantype_l

- **表名称：** 银行交易类型-多语言表
- **表名：** t_bei_crosstrantype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 描述 | varchar | 750 |  | √ | ' ' | 描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_crosstrantype_l_pkey |  | fpkid |
| 2 | idx_bei_crosstrantype_l |  | fid,fname |

---

## 支持收款方国家地区范围-多选基础资料表 t_bei_crosstrantype_cou

- **表名称：** 支持收款方国家地区范围-多选基础资料表
- **表名：** t_bei_crosstrantype_cou

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_crosstrantype_cou |  | fid |
| 2 | t_bei_crosstrantype_cou_pkey |  | fpkid |
