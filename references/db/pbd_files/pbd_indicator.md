# 风险指标-pbd_indicator

## 风险指标-主表 t_pbd_indicator

- **表名称：** 风险指标-主表
- **表名：** t_pbd_indicator

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 pbd_indicator_group](../pbd_files/pbd_indicator_group.md) |
| 3 | forderbys | 排序 | varchar | 255 |  | √ | ' ' | 排序 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ffiltercondition_tag | 参与计算的数据范围_详情 | text | 0 |  |  | null | 参与计算的数据范围_详情 |
| 6 | forderbys_tag | 排序_详情 | varchar | 1000 |  | √ | ' ' | 排序_详情 |
| 7 | findicatortype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 1 :基础指标 2 :复合指标 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | ffiltercondition | 参与计算的数据范围 | varchar | 255 |  | √ | ' ' | 参与计算的数据范围 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | foutput | 结果输出 | bpchar | 1 |  | √ | ' ' | 结果输出,枚举: 1 :计算结果 2 :统计结果 |
| 22 | fcalformula | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 23 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fbizobjectid | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 25 | fcalformula_tag | 计算公式_详情 | text | 0 |  |  | null | 计算公式_详情 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 28 | fcalmethod | 计算方式 | bpchar | 1 |  | √ | '1' | 计算方式,枚举: 1 :公式 2 :插件 |
| 29 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 30 | fpluginname | 插件 | varchar | 255 |  | √ | ' ' | 插件 |
| 31 | fmaxreturndata | 查询最大返回数量 | int4 | 32 |  | √ | 0 | 查询最大返回数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_indicator |  | fid |
| 2 | idx_t_pbd_indicator_createorg |  | fcreateorgid |
| 3 | idx_pbd_ind_fgroupid |  | fgroupid |
| 4 | idx_pbd_ind_fnumber |  | fnumber |
| 5 | idx_t_pbd_indicator_master |  | fmasterid |

---

## 维度分录-子表 t_pbd_indicator_dims

- **表名称：** 维度分录-子表
- **表名：** t_pbd_indicator_dims

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimfilters_tag | 条件设置_详情 | text | 0 |  |  | null | 条件设置_详情 |
| 3 | ftimedim | 时间维度 | bpchar | 1 |  | √ | ' ' | 时间维度,枚举: 1 :年 2 :季度 3 :月 4 :周 5 :日 |
| 4 | findicatordimid | 维度 | int8 | 64 |  | √ | 0 | [分析维度 pbd_dim](../pbd_files/pbd_dim.md) |
| 5 | fdimfilters | 条件设置 | varchar | 1000 |  | √ | ' ' | 条件设置 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pbd_indicator_dims |  | fentryid |
| 2 | idx_pbd_ind_dims_fid |  | fid |

---

## 单据体-子表 t_pbd_indicator_entry

- **表名称：** 单据体-子表
- **表名：** t_pbd_indicator_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fsubindicatorid | 子指标 | int8 | 64 |  | √ | 0 | [风险指标 pbd_indicator](../pbd_files/pbd_indicator.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_ind_entry_fid |  | fid |
| 2 | pk_pbd_indicator_entry |  | fentryid |

---

## 风险指标-多语言表 t_pbd_indicator_l

- **表名称：** 风险指标-多语言表
- **表名：** t_pbd_indicator_l

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
| 1 | idx_pbd_ind_l_fid |  | fid,flocaleid |
| 2 | pk_pbd_indicator_l |  | fpkid |

---

## 风险指标-使用范围表 t_pbd_indicator_u

- **表名称：** 风险指标-使用范围表
- **表名：** t_pbd_indicator_u

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
| 1 | idx_t_pbd_indicator_u_uo |  | fuseorgid |
| 2 | pk_t_pbd_indicator_u |  | fdataid,fuseorgid |
