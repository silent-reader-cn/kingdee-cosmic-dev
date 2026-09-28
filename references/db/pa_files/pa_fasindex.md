# 指标-pa_fasindex

## 指标-主表 t_pa_fasindex

- **表名称：** 指标-主表
- **表名：** t_pa_fasindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分组 | int8 | 64 |  | √ | 0 | [指标分组 pa_fasindexgroup](../pa_files/pa_fasindexgroup.md) |
| 3 | fdimensioncondition | 维度过滤条件 | varchar | 255 |  | √ | ' ' | 维度过滤条件 |
| 4 | fdimensioncondition_tag | 维度过滤条件_详情 | text | 0 |  |  | null | 维度过滤条件_详情 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodelid | 分析模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |
| 7 | findexformula | 计算公式 | varchar | 500 |  | √ | ' ' | 计算公式 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | faggmeasureid | 度量 | int8 | 64 |  | √ | 0 | [度量 pa_measure](../pa_files/pa_measure.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | funitbasedata | 单位基础资料类型 | varchar | 50 |  | √ | ' ' | 单位基础资料类型,枚举: bd_currency :币别 bd_measureunits :计量单位 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcategory | 指标类型 | bpchar | 1 |  | √ | '0' | 指标类型,枚举: 0 :基础指标 1 :复合指标 |
| 22 | fprecision | 计算精度 | int4 | 32 |  | √ | 20 | 计算精度 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | funitcategory | 单位类型 | varchar | 50 |  | √ | ' ' | 单位类型,枚举: 1 :金额类型 2 :数量类型 0 :数值类型 |
| 25 | funitid | 单位 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fdescription | 描述说明 | varchar | 255 |  | √ | ' ' | 描述说明 |
| 27 | faggregate | 聚合方式 | bpchar | 1 |  | √ | '0' | 聚合方式,枚举: 0 :求和 1 :计数 2 :平均 3 :最大 4 :最小 |
| 28 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 29 | findexformuladesc | 公式描述 | varchar | 500 |  | √ | ' ' | 公式描述 |
| 30 | fparent | fparent | int8 | 64 |  | √ | 0 |  |
| 31 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 33 | fsystemid | 分析体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 34 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_fasindex |  | fid |
| 2 | idx_t_pa_fasindex_master |  | fmasterid |
| 3 | idx_t_pa_fasindex_name |  | fname,fsystemid |
| 4 | idx_t_pa_fasindex_numer |  | fnumber,fsystemid |
| 5 | idx_t_pa_fasindex_createorg |  | fcreateorgid |

---

## 默认分组维度-多选基础资料表 t_pa_fasindex_defgroup

- **表名称：** 默认分组维度-多选基础资料表
- **表名：** t_pa_fasindex_defgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [维度 pa_dimension](../pa_files/pa_dimension.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_fasindex_formulaargs_fk |  | fid |
| 2 | pk_t_pa_fasindex_defgroup |  | fpkid |

---

## 公式参数-多选基础资料表 t_pa_fasindex_formulaargs

- **表名称：** 公式参数-多选基础资料表
- **表名：** t_pa_fasindex_formulaargs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [指标 pa_fasindex](../pa_files/pa_fasindex.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_fasindex_formulaargs |  | fpkid |
| 2 | idx_t_pa_fasindex_formulaargs |  | fid |

---

## 指标-多语言表 t_pa_fasindex_l

- **表名称：** 指标-多语言表
- **表名：** t_pa_fasindex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述说明 | varchar | 255 |  |  | ' ' | 描述说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_fasindex_l_0 |  | fid,flocaleid |
| 2 | pk_t_pa_fasindex_l |  | fpkid |

---

## 指标-使用范围表 t_pa_fasindex_u

- **表名称：** 指标-使用范围表
- **表名：** t_pa_fasindex_u

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
| 1 | pk_t_pa_fasindex_u |  | fdataid,fuseorgid |
| 2 | idx_t_pa_fasindex_u_uo |  | fuseorgid |
