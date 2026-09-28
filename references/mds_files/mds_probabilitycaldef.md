# 用量概率计算方案定义-mds_probabilitycaldef

## 用量概率计算方案定义-多语言表 t_mds_probabilitycaldef_l

- **表名称：** 用量概率计算方案定义-多语言表
- **表名：** t_mds_probabilitycaldef_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probabilidef_l_fid |  | fid,flocaleid |
| 2 | pk_mds_probabilitycaldef_l |  | fpkid |

---

## 用量概率计算方案定义-使用范围位图表 t_mds_probabilitycaldef_m

- **表名称：** 用量概率计算方案定义-使用范围位图表
- **表名：** t_mds_probabilitycaldef_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mds_probabilitycaldef_m |  | forgid |

---

## 用量概率计算方案定义-使用范围表 t_mds_probabilitycaldef_u

- **表名称：** 用量概率计算方案定义-使用范围表
- **表名：** t_mds_probabilitycaldef_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_probabilitycaldef_u_uo |  | fuseorgid |
| 2 | pk_t_mds_probabilitycaldef_u |  | fdataid,fuseorgid |

---

## 用量概率计算方案定义-主表 t_mds_probabilitycaldef

- **表名称：** 用量概率计算方案定义-主表
- **表名：** t_mds_probabilitycaldef

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fhistorydata | 历史数据 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsampledata | 样本数据 | int8 | 64 |  | √ | 0 | 取数方案定义 mds_datafetchset |
| 16 | fsamplehistoryfilter | 样本历史过滤字段对照 | varchar | 2000 |  | √ | ' ' | 样本历史过滤字段对照 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | falgorithmdef | 用量概率算法 | int8 | 64 |  | √ | 0 | 用量概率算法定义 mds_algorithmdef |
| 19 | fmaterialchange | 物料转换 | bpchar | 1 |  | √ | '0' | 物料转换 |
| 20 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 24 | fsamplehistoryfilterval | 样本历史过滤字段对照(后台) | text | 0 |  |  | null | 样本历史过滤字段对照(后台) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mds_probabilitycaldef_createorg |  | fcreateorgid |
| 2 | pk_mds_probabilitycaldef |  | fid |
| 3 | idx_mds_probabilidef_no |  | fnumber |
| 4 | idx_t_mds_probabilitycaldef_master |  | fmasterid |

---

## 结果单据体-子表 t_mds_probabilityrp

- **表名称：** 结果单据体-子表
- **表名：** t_mds_probabilityrp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | frpselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 5 | frpselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probabilityrp_id |  | fid |
| 2 | pk_mds_probabilityrp |  | fentryid |

---

## 样本单据体-子表 t_mds_probabilitysp

- **表名称：** 样本单据体-子表
- **表名：** t_mds_probabilitysp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fspselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |
| 3 | fspselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 4 | fspselectdimension | 数据选择维度 | varchar | 255 |  | √ | ' ' | 数据选择维度 |
| 5 | fspselectdimensionval | 选择维度(后台) | varchar | 255 |  | √ | ' ' | 选择维度(后台) |
| 6 | fspsort | 排序 | varchar | 2000 |  | √ | ' ' | 排序 |
| 7 | fspsortval | 排序值(后台) | text | 0 |  |  | null | 排序值(后台) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fspselectall | 全选 | bpchar | 1 |  | √ | '0' | 全选 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fspdataselectnum | 数据选择条数 | int8 | 64 |  | √ | 0 | 数据选择条数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mds_probabilitysp |  | fentryid |
| 2 | idx_mds_probabilitysp_id |  | fid |

---

## 历史单据体-子表 t_mds_probabilityhp

- **表名称：** 历史单据体-子表
- **表名：** t_mds_probabilityhp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhpsortval | 排序值(后台) | text | 0 |  |  | null | 排序值(后台) |
| 3 | fhpdataselectnum | 数据选择条数 | int8 | 64 |  | √ | 0 | 数据选择条数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fhpselectdimension | 数据选择维度 | varchar | 255 |  | √ | ' ' | 数据选择维度 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fhpselectall | 全选 | bpchar | 1 |  | √ | '0' | 全选 |
| 8 | fhpselectdimensionval | 选择维度(后台) | varchar | 255 |  | √ | ' ' | 选择维度(后台) |
| 9 | fhpselectfilter | 选择条件 | varchar | 2000 |  | √ | ' ' | 选择条件 |
| 10 | fhpselectfilterval | 选择条件值(后台) | text | 0 |  |  | null | 选择条件值(后台) |
| 11 | fhpsort | 排序 | varchar | 2000 |  | √ | ' ' | 排序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mds_probabilityhp_id |  | fid |
| 2 | pk_mds_probabilityhp |  | fentryid |
