# 风险检查项-rsa_riskitem

## 其他统计维度-多选基础资料表 t_rsa_otherdimension

- **表名称：** 其他统计维度-多选基础资料表
- **表名：** t_rsa_otherdimension

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
| 1 | idx_rsa_otherdimension |  | fid |
| 2 | pk_t_rsa_otherdimension |  | fpkid |

---

## 默认统计维度-多选基础资料表 t_rsa_defaultdimension

- **表名称：** 默认统计维度-多选基础资料表
- **表名：** t_rsa_defaultdimension

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
| 1 | idx_rsa_defaultdimension |  | fid |
| 2 | pk_t_rsa_defaultdimension |  | fpkid |

---

## 风险触发条件-子表 t_rsa_riskitementry

- **表名称：** 风险触发条件-子表
- **表名：** t_rsa_riskitementry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finfluence | 影响说明 | varchar | 255 |  | √ | ' ' | 影响说明 |
| 3 | fstart | 指标起始值 | varchar | 30 |  | √ | ' ' | 指标起始值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flevelid | 风险等级 | int8 | 64 |  | √ | 0 | [风险等级 rsa_risklevel](../rsa_files/rsa_risklevel.md) |
| 6 | fend | 指标终止值 | varchar | 30 |  | √ | ' ' | 指标终止值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_rsa_riskitementry |  | fentryid |
| 2 | idx_rsa_riskitementry |  | fid |

---

## 风险检查项-主表 t_rsa_riskitem

- **表名称：** 风险检查项-主表
- **表名：** t_rsa_riskitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fgroupid | 风险类别 | int8 | 64 |  | √ | 0 | [风险类别 rsa_riskgroup](../rsa_files/rsa_riskgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdescript | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | fmodelid | 指标来源体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 10 | fvaluetype | 指标值类型 | bpchar | 2 |  | √ | '00' | 指标值类型,枚举: 00 :原值 01 :同比增长率 02 :同比增长额 03 :环比增长率 04 :环比增长额 |
| 11 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 14 | ffasindexid | 指标 | int8 | 64 |  | √ | 0 | [指标 pa_fasindex](../pa_files/pa_fasindex.md) |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | fnumericalunit | 指标数值单位 | bpchar | 1 |  | √ | '0' | 指标数值单位,枚举: 0 :无 1 :千 2 :万 3 :亿 4 :百分比 5 :千分比 |
| 19 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 23 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rsa_riskitem_search |  | fnumber |
| 2 | idx_t_rsa_riskitem_createorg |  | fcreateorgid |
| 3 | idx_t_rsa_riskitem_master |  | fmasterid |
| 4 | pk_t_rsa_riskitem |  | fid |

---

## 风险检查项-使用范围表 t_rsa_riskitem_u

- **表名称：** 风险检查项-使用范围表
- **表名：** t_rsa_riskitem_u

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
| 1 | pk_t_rsa_riskitem_u |  | fdataid,fuseorgid |
| 2 | idx_t_rsa_riskitem_u_uo |  | fuseorgid |

---

## 风险检查项-多语言表 t_rsa_riskitem_l

- **表名称：** 风险检查项-多语言表
- **表名：** t_rsa_riskitem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rsa_riskitem_l |  | fid,flocaleid |
| 2 | pk_t_rsa_riskitem_l |  | fpkid |
