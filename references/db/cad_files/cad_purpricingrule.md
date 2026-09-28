# 采购取价规则-cad_purpricingrule

## 单据类型-多选基础资料表 t_cad_price_billtypeorder

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_cad_price_billtypeorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_price_billtypeorder |  | fpkid |
| 2 | idx_cad_price_billtypeorder |  | fid |

---

## 采购组织-多选基础资料表 t_cad_price_purorgcon

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_cad_price_purorgcon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_price_purorgcon |  | fpkid |
| 2 | idx_cad_price_purorgcon |  | fid |

---

## 采购取价规则-主表 t_cad_purpricingrule

- **表名称：** 采购取价规则-主表
- **表名：** t_cad_purpricingrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpricingqtyorder | 取量字段 | varchar | 30 |  | √ | ' ' | 取量字段,枚举: baseqty :基本数量 |
| 3 | fpricingdayorder | 取价天数 | int4 | 32 |  | √ | 0 | 取价天数 |
| 4 | fiswithcomporder | 考虑关联公司 | bpchar | 1 |  | √ | ' ' | 考虑关联公司 |
| 5 | fiswithcompcon | 考虑关联公司 | bpchar | 1 |  | √ | ' ' | 考虑关联公司 |
| 6 | flevelorder | 优先级 | varchar | 30 |  | √ | ' ' | 优先级,枚举: one :1级 two :2级 |
| 7 | forgconid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | flevelcon | 优先级 | varchar | 30 |  | √ | ' ' | 优先级,枚举: one :1级 two :2级 |
| 10 | fcosttypeid | 成本类型 | int8 | 64 |  | √ | 0 | [标准成本方案 cad_costtype](../basedata_files/cad_costtype.md) |
| 11 | ftypeconid | 合同类型 | int8 | 64 |  | √ | 0 | [合同类型 conm_type](../conm_files/conm_type.md) |
| 12 | fispricingcon | 参与取价 | bpchar | 1 |  | √ | ' ' | 参与取价 |
| 13 | fpricingvalueorder | 取价字段 | varchar | 30 |  | √ | ' ' | 取价字段,枚举: amount :金额 |
| 14 | fpricingvaluecon | 取价字段 | varchar | 30 |  | √ | ' ' | 取价字段,枚举: price :单价 |
| 15 | fispricingorder | 参与取价 | bpchar | 1 |  | √ | ' ' | 参与取价 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_purpricingrule |  | fcosttypeid |
| 2 | pk_t_cad_purpricingrule |  | fid |

---

## 采购组织-多选基础资料表 t_cad_price_purorgorder

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_cad_price_purorgorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_price_purorgorder |  | fpkid |
| 2 | idx_cad_price_purorgorder |  | fid |

---

## 单据类型-多选基础资料表 t_cad_price_billtypecon

- **表名称：** 单据类型-多选基础资料表
- **表名：** t_cad_price_billtypecon

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cad_price_billtypecon |  | fid,fbasedataid |
| 2 | pk_t_cad_price_billtypecon |  | fpkid |
