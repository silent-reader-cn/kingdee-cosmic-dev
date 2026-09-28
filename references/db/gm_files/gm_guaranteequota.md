# 担保额度-gm_guaranteequota

## 担保额度-主表 t_gm_guaranteequota

- **表名称：** 担保额度-主表
- **表名：** t_gm_guaranteequota

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 担保人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftotalamount | 总额度 | numeric | 23 | 10 | √ | 0 | 总额度 |
| 4 | fdisabledate | 关闭日期 | timestamp | 0 |  |  | null | 关闭日期 |
| 5 | favailablequota | 可用额度 | numeric | 23 | 10 | √ | 0 | 可用额度 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fenablerid | 打开人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 13 | fname | 额度名称 | varchar | 255 |  | √ | ' ' | 额度名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fbegindate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 18 | fguaranteeorgid | 担保人ID | int8 | 64 |  | √ | 0 | 担保人ID |
| 19 | fenabledate | 打开日期 | timestamp | 0 |  |  | null | 打开日期 |
| 20 | fadvancequota | 预占额度 | numeric | 23 | 10 | √ | 0 | 预占额度 |
| 21 | fdisablerid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | fusedquota | 已用额度 | numeric | 23 | 10 | √ | 0 | 已用额度 |
| 24 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 25 | fquotaproperty | 额度性质 | varchar | 80 |  | √ | ' ' | 额度性质,枚举: cycle :循环 no_cycle :非循环 |
| 26 | fenable | 使用状态 | varchar | 80 |  | √ | '1' | 使用状态,枚举: 0 :已关闭 1 :可用 |
| 27 | fnumber | 担保额度单号 | varchar | 80 |  | √ | ' ' | 担保额度单号 |
| 28 | fctrllimit | 控制对象 | varchar | 80 |  | √ | ' ' | 控制对象,枚举: guaranteeorg :担保人 guaranteedorg :被担保人 |
| 29 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteequota |  | fnumber |
| 2 | pk_t_gm_guaranteequota |  | fid |

---

## 被担保人分录-子表 t_gm_reguaquota_entry

- **表名称：** 被担保人分录-子表
- **表名：** t_gm_reguaquota_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 3 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 4 | flimitamount | 限定额度 | numeric | 23 | 10 | √ | 0 | 限定额度 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_reguaquota_entry |  | fid |
| 2 | pk_t_gm_reguaquota_entry |  | fentryid |

---

## 担保额度-多语言表 t_gm_guaranteequota_l

- **表名称：** 担保额度-多语言表
- **表名：** t_gm_guaranteequota_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 额度名称 | varchar | 255 |  | √ | ' ' | 额度名称 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteequota_l |  | fid,flocaleid |
| 2 | pk_t_gm_guaranteequota_l |  | fpkid |
