# 商务条款方案-src_bizscheme

## 寻源流程-多选基础资料表 t_src_bizschemesrcflow

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_src_bizschemesrcflow

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
| 1 | idx_src_bizschemesrcflow_fid |  | fid |
| 2 | pk_src_bizschemesrcflow |  | fpkid |
| 3 | idx_src_bizschemesrcflow_bid |  | fbasedataid |

---

## 条款分录-子表 t_src_bizschemeentry

- **表名称：** 条款分录-子表
- **表名：** t_src_bizschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizitemld | 商务条款编码 | int8 | 64 |  | √ | 0 | [寻源商务条款 src_bizitem](../src_files/src_bizitem.md) |
| 3 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 4 | fitemtype | 商务条款类型 | varchar | 50 |  | √ | ' ' | 商务条款类型 |
| 5 | fdemand | 采购方要求 | varchar | 510 |  | √ | ' ' | 采购方要求 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fdemandvalue | 采购方要求值 | varchar | 510 |  | √ | ' ' | 采购方要求值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | frequest | 商务条款名称 | varchar | 600 |  | √ | ' ' | 商务条款名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_bizschemeentry |  | fentryid |
| 2 | idx_src_bizschemeentry_fid |  | fid |

---

## 商务条款方案-主表 t_src_bizscheme

- **表名称：** 商务条款方案-主表
- **表名：** t_src_bizscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 描述 | varchar | 600 |  | √ | ' ' | 描述 |
| 3 | fisv_id | 开发商标识 | varchar | 50 |  | √ | ' ' | 开发商标识 |
| 4 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fplugin | fplugin | varchar | 100 |  | √ | ' ' |  |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bizscheme_fcreatetime |  | fcreatetime |
| 2 | idx_src_bizscheme_fmasterid |  | fmasterid |
| 3 | idx_src_bizscheme_fnumber |  | fnumber |
| 4 | pk_src_bizscheme |  | fid |

---

## 商务条款方案-多语言表 t_src_bizscheme_l

- **表名称：** 商务条款方案-多语言表
- **表名：** t_src_bizscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 描述 | varchar | 500 |  | √ | ' ' | 描述 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_bizscheme_l_fname |  | fname |
| 2 | pk_src_bizscheme_l |  | fpkid |
| 3 | idx_src_bizscheme_l_fid |  | fid |

---

## 寻源方式-多选基础资料表 t_src_bizschemesrctype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_src_bizschemesrctype

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
| 1 | idx_src_bizschemesrctype_bid |  | fbasedataid |
| 2 | idx_src_bizschemesrctype_fid |  | fid |
| 3 | pk_src_bizschemesrctype |  | fpkid |

---

## 条款分录-多语言表 t_src_bizschemeentry_l

- **表名称：** 条款分录-多语言表
- **表名：** t_src_bizschemeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 2 | fdemandvalue | fdemandvalue | varchar | 510 |  | √ | ' ' |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | floacleid | floacleid | varchar | 10 |  | √ | ' ' |  |
| 7 | frequest | 商务条款名称 | varchar | 500 |  | √ | ' ' | 商务条款名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_bizschemeentry_l |  | fpkid |
| 2 | idx_src_bizschemeentry_l_fid |  | fentryid,flocaleid |
