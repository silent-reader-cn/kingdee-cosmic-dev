# 智能绩效设置版本记录-srm_autoevatpl_ver

## 智能绩效设置版本记录-主表 t_srm_autoevatplver

- **表名称：** 智能绩效设置版本记录-主表
- **表名：** t_srm_autoevatplver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftplid | 绩效评估模板id | varchar | 80 |  | √ | ' ' | 绩效评估模板id |
| 3 | fistypescorer | 按一级指标类型设置评委 | bpchar | 1 |  | √ | ' ' | 按一级指标类型设置评委 |
| 4 | fcategoryvalue | 品类字段匹配 | varchar | 60 |  | √ | ' ' | 品类字段匹配,枚举: |
| 5 | fbillobject | 取值单据 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 6 | fvernumber | 版本编号 | varchar | 80 |  | √ | ' ' | 版本编号 |
| 7 | fevamethod | 评估方式 | bpchar | 1 |  | √ | ' ' | 评估方式,枚举: A :供应商 B :物料+供应商 D :品类+供应商 |
| 8 | ffinishdateoffset | 天 | int8 | 64 |  | √ | 0 | 天 |
| 9 | fexpiringdate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 10 | forgid | 评估组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fop | 操作 | varchar | 30 |  | √ | ' ' | 操作,枚举: |
| 12 | fschemeid | 评估方案 | int8 | 64 |  | √ | 0 | 评估方案 srm_scheme |
| 13 | fnote | 模板备注 | varchar | 255 |  | √ | ' ' | 模板备注 |
| 14 | fconditiontext_tag | 通用过滤文本_详情 | text | 0 |  |  | null | 通用过滤文本_详情 |
| 15 | fexectime | 触发时间 | int8 | 64 |  | √ | 0 | 触发时间 |
| 16 | frepeatunit | 周期 | bpchar | 1 |  | √ | ' ' | 周期,枚举: 1 :年 2 :月 3 :日 4 :季度 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | ffiltertext | 过滤条件文本 | text | 0 |  |  | null | 过滤条件文本 |
| 19 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 21 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 23 | fpushtype | 下推类型 | varchar | 30 |  | √ | ' ' | 下推类型,枚举: srm_evaplan :评估计划 srm_evaplan_batch :绩效评估计划 |
| 24 | fevaorgvalue | 评估组织字段匹配 | varchar | 30 |  | √ | ' ' | 评估组织字段匹配,枚举: |
| 25 | fexecday | 触发日期 | varchar | 2 |  | √ | ' ' | 触发日期,枚举: 1 :1号 2 :2号 3 :3号 4 :4号 5 :5号 6 :6号 7 :7号 8 :8号 9 :9号 10 :10号 11 :11号 12 :12号 13 :13号 14 :14号 15 :15号 16 :16号 17 :17号 18 :18号 19 :19号 20 :20号 21 :21号 22 :22号 23 :23号 24 :24号 25 :25号 26 :26号 27 :27号 28 :28号 29 :29号 30 :30号 31 :31号 32 :最后一天 |
| 26 | feffectivedate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 27 | fconditiontext | 通用过滤文本 | text | 0 |  |  | null | 通用过滤文本 |
| 28 | fversion | 版本号 | varchar | 30 |  | √ | ' ' | 版本号 |
| 29 | ftimerange | 取值范围 | bpchar | 1 |  | √ | ' ' | 取值范围,枚举: 1 :指定时间范围 2 :依重复时间确定时间范围 3 :插件 |
| 30 | fmaterialvalue | 物料字段匹配 | varchar | 60 |  | √ | ' ' | 物料字段匹配,枚举: |
| 31 | fexecmonth | 触发月份 | varchar | 2 |  | √ | ' ' | 触发月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 32 | fsuppliervalue | 供应商字段匹配 | varchar | 30 |  | √ | ' ' | 供应商字段匹配,枚举: |
| 33 | fname | 模板名称 | varchar | 255 |  | √ | ' ' | 模板名称 |
| 34 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | frepeatnumber | 重复频率 | int8 | 64 |  | √ | 0 | 重复频率 |
| 36 | fgradeid | 分级方案 | int8 | 64 |  | √ | 0 | 分级方案 srm_grade |
| 37 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 38 | fevatypeid | 评估类型 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 39 | ffiltertext_tag | 过滤条件文本_详情 | text | 0 |  |  | null | 过滤条件文本_详情 |
| 40 | ftimevalue | 时间字段匹配 | varchar | 30 |  | √ | ' ' | 时间字段匹配,枚举: |
| 41 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 42 | fexectype | 触发方式 | bpchar | 1 |  | √ | ' ' | 触发方式,枚举: 1 :定期触发 2 :单据操作触发 |
| 43 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 44 | fautogetvalue | 按业务单据自动取值 | bpchar | 1 |  | √ | ' ' | 按业务单据自动取值 |
| 45 | fnumber | 模板编号 | varchar | 80 |  | √ | ' ' | 模板编号 |
| 46 | ffinishdatetype | 取值依据 | bpchar | 1 |  | √ | ' ' | 取值依据,枚举: 1 :模板触发日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoevatplver |  | fid |
| 2 | idx_srm_autoevatplver_fnumber |  | fnumber |

---

## 智能绩效设置版本记录-多语言表 t_srm_autoevatplver_l

- **表名称：** 智能绩效设置版本记录-多语言表
- **表名：** t_srm_autoevatplver_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 100 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_autoevatplver_l_idloc |  | fid,flocaleid |
| 2 | pk_srm_autoevatplver_l |  | fpkid |

---

## 关联子实体-子表 t_srm_autoevatplver_lk

- **表名称：** 关联子实体-子表
- **表名：** t_srm_autoevatplver_lk

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
| 1 | idx_srm_autoevatplver_lk_fk |  | fid |
| 2 | pk_srm_autoevatplver_lk |  | fpkid |

---

## 评委分录-子表 t_srm_evatplscorever

- **表名称：** 评委分录-子表
- **表名：** t_srm_evatplscorever

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fweight | 评委权重（%） | numeric | 23 | 10 | √ | 0 | 评委权重（%） |
| 3 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | 指标分类 srm_indexclass |
| 4 | fscorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 1 | pk_srm_evatplscorever |  | fentryid |
| 2 | idx_srm_evatplscorerver_id |  | fid |

---

## 评估对象分录-子表 t_srm_autoevasupentryver

- **表名称：** 评估对象分录-子表
- **表名：** t_srm_autoevasupentryver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fevasupnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fevacategoryid | 评估品类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 4 | fevamaterialid | 评估物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsuppliernote | fsuppliernote | varchar | 255 |  | √ | ' ' |  |
| 8 | fevagradeid | 分级方案 | int8 | 64 |  | √ | 0 | 分级方案 srm_grade |
| 9 | fweightstrategy | 评委权重策略 | varchar | 30 |  | √ | ' ' | 评委权重策略,枚举: A :权重平均计算 B :自定义权重 |
| 10 | fevasupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 11 | fevaschemeid | 评估方案 | int8 | 64 |  | √ | 0 | 评估方案 srm_scheme |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoevasupentryver |  | fentryid |
| 2 | idx_srm_autoevasupentryver_fid |  | fid |

---

## 供应商分录-子表 t_srm_evatplsupplierver

- **表名称：** 供应商分录-子表
- **表名：** t_srm_evatplsupplierver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 5 | fsuppliernote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_evatplsupver_id |  | fid |
| 2 | pk_srm_evatplsupplierver |  | fentryid |

---

## 评委信息分录-子表 t_srm_autoscorerentryver

- **表名称：** 评委信息分录-子表
- **表名：** t_srm_autoscorerentryver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fevaindexclassid | 指标分类 | int8 | 64 |  | √ | 0 | 指标分类 srm_indexclass |
| 2 | fscorernote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fevascorerid | 评委 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fevascorerweight | 评委权重 | numeric | 23 | 10 | √ | 0 | 评委权重 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_srm_autoscorerentryver |  | fdetailid |
| 2 | idx_srm_autoscorerver_enid |  | fentryid |
