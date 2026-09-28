# 数据资产明细-fa_data_asset_detail

## 数据资产明细-多语言表 t_fa_data_detail_l

- **表名称：** 数据资产明细-多语言表
- **表名：** t_fa_data_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fentryname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_data_detail_l |  | fpkid |
| 2 | idx_fa_data_detail_l_lid |  | fentryid,flocaleid |

---

## 数据资产明细-主表 t_fa_data_detail

- **表名称：** 数据资产明细-主表
- **表名：** t_fa_data_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 数据资产id | int8 | 64 |  | √ | 0 | 数据资产id |
| 2 | finvaliddate | 失效时间 | timestamp | 0 |  |  | null | 失效时间 |
| 3 | feffectuatedate | 生效时间 | timestamp | 0 |  |  | null | 生效时间 |
| 4 | fstatus | 状态 | varchar | 10 |  | √ | ' ' | 状态,枚举: 1 :生效 2 :失效 |
| 5 | fentrymodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fentryscale | 数据规模 | numeric | 23 | 10 | √ | 0 | 数据规模 |
| 7 | fentrysupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finvalidtype | finvalidtype | bpchar | 1 |  | √ | '1' |  |
| 11 | fdetailsbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 12 | fentryunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fa_data_detail |  | fentryid |
| 2 | idx_fa_data_detail_id |  | fid |
