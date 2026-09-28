# 智能绩效设置-srm_autoevatpl

## 智能绩效设置-多语言表 t_srm_autoevatpl_l

- **表名称：** 智能绩效设置-多语言表
- **表名：** t_srm_autoevatpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_autoevatpl_l_idlocale |  | fid,flocaleid |
| 2 | pk_srm_autoevatpl_l |  | fpkid |

---

## 评委信息分录-子表 t_srm_autoscorerentry

- **表名称：** 评委信息分录-子表
- **表名：** t_srm_autoscorerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fevaindexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 2 | fscorernote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fevascorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fevascorerweight | 评委权重 | numeric | 23 | 10 | √ | 0 | 评委权重 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_srm_autoscorerentry |  | fdetailid |
| 2 | idx_srm_autoscorer_entryid |  | fentryid |

---

## 智能绩效设置-主表 t_srm_autoevatpl

- **表名称：** 智能绩效设置-主表
- **表名：** t_srm_autoevatpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fistypescorer | 按一级指标类型设置评委 | bpchar | 1 |  | √ | ' ' | 按一级指标类型设置评委 |
| 3 | fcategoryvalue | 品类字段匹配 | varchar | 60 |  | √ | ' ' | 品类字段匹配,枚举: |
| 4 | fbillobject | 取值单据 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fevamethod | 评估方式 | bpchar | 1 |  | √ | ' ' | 评估方式,枚举: A :供应商 B :物料+供应商 D :品类+供应商 |
| 6 | ffinishdateoffset | 天 | int8 | 64 |  | √ | 0 | 天 |
| 7 | fexpiringdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 8 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: |
| 10 | fschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |
| 11 | fnote | 模板备注 | varchar | 255 |  | √ | ' ' | 模板备注 |
| 12 | fconditiontext_tag | 通用过滤文本_详情 | text | 0 |  |  | null | 通用过滤文本_详情 |
| 13 | fexectime | 触发时间 | int8 | 64 |  | √ | 0 | 触发时间 |
| 14 | frepeatunit | 周期 | bpchar | 1 |  | √ | ' ' | 周期,枚举: 1 :年 2 :月 3 :日 4 :季度 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | ffiltertext | 过滤条件文本 | text | 0 |  |  | null | 过滤条件文本 |
| 17 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fpushtype | 下推类型 | varchar | 30 |  | √ | ' ' | 下推类型,枚举: srm_evaplan :评估计划 srm_evaplan_batch :绩效评估计划 |
| 22 | fevaorgvalue | 评估组织字段匹配 | varchar | 30 |  | √ | ' ' | 评估组织字段匹配,枚举: |
| 23 | fexecday | 触发日期 | varchar | 2 |  | √ | ' ' | 触发日期,枚举: 1 :1号 2 :2号 3 :3号 4 :4号 5 :5号 6 :6号 7 :7号 8 :8号 9 :9号 10 :10号 11 :11号 12 :12号 13 :13号 14 :14号 15 :15号 16 :16号 17 :17号 18 :18号 19 :19号 20 :20号 21 :21号 22 :22号 23 :23号 24 :24号 25 :25号 26 :26号 27 :27号 28 :28号 29 :29号 30 :30号 31 :31号 32 :最后一天 33 :倒数第二天 34 :倒数第三天 |
| 24 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 25 | fconditiontext | 通用过滤文本 | text | 0 |  |  | null | 通用过滤文本 |
| 26 | ftimerange | 取值范围 | bpchar | 1 |  | √ | ' ' | 取值范围,枚举: 1 :指定时间范围 2 :依重复时间确定时间范围 3 :插件 |
| 27 | fmaterialvalue | 物料字段匹配 | varchar | 60 |  | √ | ' ' | 物料字段匹配,枚举: |
| 28 | fexecmonth | 触发月份 | varchar | 2 |  | √ | ' ' | 触发月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 29 | fsuppliervalue | 供应商字段匹配 | varchar | 30 |  | √ | ' ' | 供应商字段匹配,枚举: |
| 30 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 31 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | frepeatnumber | 重复频率 | int8 | 64 |  | √ | 0 | 重复频率 |
| 33 | fgradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 34 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 35 | fevatypeid | 评估类型 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 36 | ffiltertext_tag | 过滤条件文本_详情 | text | 0 |  |  | null | 过滤条件文本_详情 |
| 37 | ftimevalue | 时间字段匹配 | varchar | 30 |  | √ | ' ' | 时间字段匹配,枚举: |
| 38 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 39 | fexectype | 触发方式 | bpchar | 1 |  | √ | ' ' | 触发方式,枚举: 1 :定期触发 2 :单据操作触发 |
| 40 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fautogetvalue | 按业务单据自动取值 | bpchar | 1 |  | √ | ' ' | 按业务单据自动取值 |
| 42 | fnumber | 模板编码 | varchar | 80 |  | √ | ' ' | 模板编码 |
| 43 | ffinishdatetype | 取值依据 | bpchar | 1 |  | √ | ' ' | 取值依据,枚举: 1 :模板触发日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoevatpl |  | fid |
| 2 | idx_srm_evatpl_feffdate |  | feffectivedate,fexpiringdate |
| 3 | idx_srm_autoevatpl_fnumber |  | fnumber |

---

## 供应商分录-子表 t_srm_evatplsupplierentry

- **表名称：** 供应商分录-子表
- **表名：** t_srm_evatplsupplierentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 5 | fsuppliernote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_evatplsupentry_fid |  | fid |
| 2 | pk_srm_evatplsupplierentry |  | fentryid |

---

## 评估对象分录-子表 t_srm_autoevasupentry

- **表名称：** 评估对象分录-子表
- **表名：** t_srm_autoevasupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevasupnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fevacategoryid | 评估品类 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 4 | fevamaterialid | 评估物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsuppliernote | fsuppliernote | varchar | 255 |  | √ | ' ' |  |
| 8 | fevagradeid | 分级方案 | int8 | 64 |  | √ | 0 | [分级方案 srm_grade](../srm_files/srm_grade.md) |
| 9 | fweightstrategy | 评委权重策略 | varchar | 30 |  | √ | ' ' | 评委权重策略,枚举: A :权重平均计算 B :自定义权重 |
| 10 | fevasupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 11 | fevaschemeid | 评估方案 | int8 | 64 |  | √ | 0 | [评估方案 srm_scheme](../srm_files/srm_scheme.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoevasupentry |  | fentryid |
| 2 | idx_srm_autoevasupentry_fid |  | fid |

---

## 关联子实体-子表 t_srm_autoevatpl_lk

- **表名称：** 关联子实体-子表
- **表名：** t_srm_autoevatpl_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoevatpl_lk |  | fpkid |
| 2 | idx_srm_autoevatpl_lk_fk |  | fid |

---

## 评委分录-子表 t_srm_evatplscorerentry

- **表名称：** 评委分录-子表
- **表名：** t_srm_evatplscorerentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 评委权重（%） | numeric | 23 | 10 | √ | 0 | 评委权重（%） |
| 3 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类 srm_indexclass](../srm_files/srm_indexclass.md) |
| 4 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fscorervaluetype | 评委取值类型 | varchar | 1 |  | √ | ' ' | 评委取值类型,枚举: 1 :指定具体人员 2 :从单据对象中取人员 |
| 7 | fscorervalue | 评委取值字段 | varchar | 30 |  | √ | ' ' | 评委取值字段,枚举: |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_evatplscorerentry |  | fentryid |
| 2 | idx_srm_evatplscoreentry_fid |  | fid |
