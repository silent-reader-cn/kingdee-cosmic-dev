# 议价管控方案-src_negscheme

## 议价管控方案-主表 t_src_negscheme

- **表名称：** 议价管控方案-主表
- **表名：** t_src_negscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 方案描述 | varchar | 255 |  | √ | ' ' | 方案描述 |
| 3 | ftaxamount | 含税金额 (≥) | numeric | 23 | 10 | √ | 0 | 含税金额 (≥) |
| 4 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 5 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 10 | famount | 未税金额 (≥) | numeric | 23 | 10 | √ | 0 | 未税金额 (≥) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fenable | 可用状态 | bpchar | 1 |  | √ | '1' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 18 | fcount | 议价次数 | int4 | 32 |  | √ | 0 | 议价次数 |
| 19 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 20 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 21 | fnegotiatetype | 议价方式 | varchar | 30 |  | √ | ' ' | 议价方式,枚举: 1 :不允许议价 2 :允许议价的次数 3 :不限制议价次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_negscheme |  | fid |
| 2 | idx_src_negscheme_num |  | fnumber |

---

## 寻源流程-多选基础资料表 t_src_negscheme_srcflow

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_src_negscheme_srcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [流程配置 pds_flowconfig](../pds_files/pds_flowconfig.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_negscheme_srcflow |  | fid |
| 2 | pk_src_negscheme_srcflow |  | fpkid |
| 3 | idx_src_negscheme_srcflow_bid |  | fbasedataid |

---

## 业务节点-多选基础资料表 t_src_negscheme_biznode

- **表名称：** 业务节点-多选基础资料表
- **表名：** t_src_negscheme_biznode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务节点 pds_biznode](../pds_files/pds_biznode.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_negscheme_biznode |  | fid |
| 2 | pk_src_negscheme_biznode |  | fpkid |
| 3 | idx_src_negscheme_biznode_bid |  | fbasedataid |

---

## 寻源方式-多选基础资料表 t_src_negscheme_srctype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_src_negscheme_srctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_negscheme_srctype |  | fpkid |
| 2 | idx_src_negscheme_srctype |  | fid |
| 3 | idx_src_negscheme_srctype_bid |  | fbasedataid |

---

## 议价管控方案-多语言表 t_src_negscheme_l

- **表名称：** 议价管控方案-多语言表
- **表名：** t_src_negscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_negscheme_l |  | fpkid |
| 2 | idx_src_negscheme_l_fid |  | fid,flocaleid |
