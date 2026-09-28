# 保证金余额-tnd_feesurplus

## 限定供应商用户-多选基础资料表 t_src_supplieruser

- **表名称：** 限定供应商用户-多选基础资料表
- **表名：** t_src_supplieruser

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [供应商用户 pur_supuser](../basedata_files/pur_supuser.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supplieruser_bid |  | fbasedataid |
| 2 | pk_src_supplieruser |  | fpkid |
| 3 | idx_src_supplieruser_fid |  | fid |

---

## 保证金余额-主表 t_src_feesurplus

- **表名称：** 保证金余额-主表
- **表名：** t_src_feesurplus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsumtransfer | 累计结余金额 | numeric | 23 | 10 | √ | 0 | 累计结余金额 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsourceid | 项目 | int8 | 64 |  | √ | 0 | [项目立项查询 src_demandno](../src_files/src_demandno.md) |
| 7 | fsumreturn | 累计退还金额 | numeric | 23 | 10 | √ | 0 | 累计退还金额 |
| 8 | fsumcarryover | 累计转履约金额 | numeric | 23 | 10 | √ | 0 | 累计转履约金额 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fsurplusamount | 当前余额 | numeric | 23 | 10 | √ | 0 | 当前余额 |
| 11 | fissurplus | 余额大于0 | bpchar | 1 |  | √ | '0' | 余额大于0 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsumreceipt | 累计收取金额 | numeric | 23 | 10 | √ | 0 | 累计收取金额 |
| 14 | fbillid | ID组合 | varchar | 100 |  | √ | ' ' | ID组合 |
| 15 | fsurplustype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: 1 :投标保证金 2 :履约保证金 3 :标书费 |
| 16 | ffeeitemid | 收费项 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 17 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fsumadjust | 累计调整金额 | numeric | 23 | 10 | √ | 0 | 累计调整金额 |
| 19 | fsumuse | 累计使用金额 | numeric | 23 | 10 | √ | 0 | 累计使用金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_feesurplus |  | fid |
| 2 | idx_src_feesurplus_bid |  | fbillid |
| 3 | idx_src_feesurplus_sid |  | fsourceid |
| 4 | idx_src_feesurplus_sup |  | fsupplierid |
