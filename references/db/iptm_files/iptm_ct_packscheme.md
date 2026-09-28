# 打包方案-iptm_ct_packscheme

## 树形单据体-子表 t_iptm_ct_packschemecfg

- **表名称：** 树形单据体-子表
- **表名：** t_iptm_ct_packschemecfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmanualselectdata | 手工选择数据存储 | varchar | 255 |  | √ | ' ' | 手工选择数据存储 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmanualselectdata_tag | 手工选择数据存储_详情 | text | 0 |  |  | null | 手工选择数据存储_详情 |
| 5 | fexportfilters | 过滤条件存储 | varchar | 255 |  | √ | ' ' | 过滤条件存储 |
| 6 | ffilterterm | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 7 | fmunualsel | 手工选择 | varchar | 50 |  | √ | ' ' | 手工选择 |
| 8 | fdataselection | 数据选择方式 | varchar | 50 |  | √ | ' ' | 数据选择方式,枚举: A :过滤条件选择 B :手工选择 |
| 9 | fexportfilters_tag | 过滤条件存储_详情 | text | 0 |  |  | null | 过滤条件存储_详情 |
| 10 | fitem | 配置项名称 | int8 | 64 |  | √ | 0 | [传输对象 iptm_ct_configitems](../iptm_files/iptm_ct_configitems.md) |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fentryremark | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_ct_packschemecfg |  | fentryid |
| 2 | idx_packcfg |  | fid |

---

## 打包方案-多语言表 t_iptm_ct_packscheme_l

- **表名称：** 打包方案-多语言表
- **表名：** t_iptm_ct_packscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_ct_packscheme_l |  | fpkid |
| 2 | idx_packscheme_l |  | fid,flocaleid |

---

## 打包方案-主表 t_iptm_ct_packscheme

- **表名称：** 打包方案-主表
- **表名：** t_iptm_ct_packscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fremarks | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 11 | fispreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iptm_ct_packscheme |  | fid |
| 2 | idx_packscheme |  | fnumber |
