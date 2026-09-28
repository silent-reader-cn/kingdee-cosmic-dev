# 项目方案配置-src_scheme2

## 专家考评类型-多选基础资料表 t_src_schemebiztype

- **表名称：** 专家考评类型-多选基础资料表
- **表名：** t_src_schemebiztype

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
| 1 | pk_src_schemebiztype |  | fpkid |
| 2 | idx_src_schemebiztype_fid |  | fid |

---

## 招标流程-多选基础资料表 t_src_schemesourceflow

- **表名称：** 招标流程-多选基础资料表
- **表名：** t_src_schemesourceflow

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
| 1 | pk_src_schemesourceflow |  | fpkid |
| 2 | idx_src_schemesourceflow_fid |  | fid |
| 3 | idx_src_schemesourceflow_bid |  | fbasedataid |

---

## 品类-多选基础资料表 t_src_schemecategory

- **表名称：** 品类-多选基础资料表
- **表名：** t_src_schemecategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemecategory_bid |  | fbasedataid |
| 2 | idx_src_schemecategory_fid |  | fid |
| 3 | pk_src_schemecategory |  | fpkid |

---

## 招标项目-多选基础资料表 t_src_schemeproject

- **表名称：** 招标项目-多选基础资料表
- **表名：** t_src_schemeproject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [招标项目F7 src_projectf7](../src_files/src_projectf7.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemeproject_bid |  | fbasedataid |
| 2 | pk_src_schemeproject |  | fpkid |
| 3 | idx_src_schemeproject_fid |  | fid |

---

## 项目方案配置-主表 t_src_scheme

- **表名称：** 项目方案配置-主表
- **表名：** t_src_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findexdimension | findexdimension | varchar | 255 |  |  | ' ' |  |
| 3 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 5 | fsourceid | 项目 | int8 | 64 |  | √ | 0 | [项目立项F7 src_demandnotwo](../src_files/src_demandnotwo.md) |
| 6 | fschemeid | 项目级方案的来源方案id | int8 | 64 |  | √ | 0 | 项目级方案的来源方案id |
| 7 | foffset | 评分异常偏差比例(%) | numeric | 19 | 6 | √ | 0 | 评分异常偏差比例(%) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fschemescore | 方案总分 | numeric | 23 | 10 | √ | 0 | 方案总分 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 22 | fprojectid | 项目级方案的寻源项目id | int8 | 64 |  | √ | 0 | 项目级方案的寻源项目id |
| 23 | fgradeid | 默认的考评分级方案 | int8 | 64 |  | √ | 0 | [考评分级方案 src_expertgrade](../src_files/src_expertgrade.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fexpertcount | 评委最低人数要求 | int4 | 32 |  | √ | 0 | 评委最低人数要求 |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fsumscore | 合格最低得分要求 | numeric | 23 | 10 | √ | 0 | 合格最低得分要求 |
| 28 | fschemetype | 方案类型 | bpchar | 1 |  | √ | '1' | 方案类型,枚举: 1 :招标评标方案 2 :资质审查方案 3 :供应商分析方案 4 :专家考评方案 |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 32 | fscoremethod | 评分方法 | bpchar | 1 |  | √ | '1' | 评分方法,枚举: 1 :百分制(每个指标按百分制评分，方案=100分) 2 :实际值(每个指标按实际值评分，方案=100分) 3 :最终值(每个指标按最终值评分，方案<=100分) |
| 33 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 35 | fuseorgid | 使用组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 37 | fisoffline | 是否线下评分方案 | bpchar | 1 |  | √ | '0' | 是否线下评分方案 |
| 38 | fisbizscore | 评委通过评标助手评商务分(线上评分) | bpchar | 1 |  | √ | '1' | 评委通过评标助手评商务分(线上评分) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scheme_fcreatetime |  | fcreatetime |
| 2 | idx_t_src_scheme_master |  | fmasterid |
| 3 | idx_src_scheme_findextypeid |  | findextypeid |
| 4 | pk_src_scheme |  | fid |
| 5 | idx_t_src_scheme_createorg |  | fcreateorgid |
| 6 | idx_src_scheme_fnumber |  | fnumber |
| 7 | idx_src_scheme_fsourceid |  | fsourceid |
| 8 | idx_src_scheme_fmasterid |  | fmasterid |

---

## 采购组-多选基础资料表 t_src_schemepurgroup

- **表名称：** 采购组-多选基础资料表
- **表名：** t_src_schemepurgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [业务组 pur_bizgroup](../pbd_files/pur_bizgroup.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemepurgroup_fid |  | fid |
| 2 | pk_src_schemepurgroup |  | fpkid |

---

## 指标分录-子表 t_src_schemeindex

- **表名称：** 指标分录-子表
- **表名：** t_src_schemeindex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisscoretask | 下达评标任务 | bpchar | 1 |  | √ | '1' | 下达评标任务 |
| 3 | findexdimension | 指标维度 | varchar | 255 |  | √ | ' ' | 指标维度 |
| 4 | fsrcentryid | fsrcentryid | int8 | 64 |  | √ | 0 |  |
| 5 | fhightvalue | 提醒值(>=) | numeric | 23 | 10 | √ | 0 | 提醒值(>=) |
| 6 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fisformula | 计算公式 | bpchar | 1 |  | √ | '0' | 计算公式 |
| 10 | fsrcindexlibid | fsrcindexlibid | int8 | 64 |  | √ | 0 |  |
| 11 | fisveto | 一票否决 | bpchar | 1 |  | √ | '0' | 一票否决,枚举: 1 :一级指标0分 2 :二级指标0分 3 :三级指标0分 4 :当前项目0分 9 :非否决项 |
| 12 | fsrcindexid | fsrcindexid | int8 | 64 |  | √ | 0 |  |
| 13 | fscoretype | 评分方式 | bpchar | 1 |  | √ | ' ' | 评分方式,枚举: 1 :手工评分 2 :自动评分 |
| 14 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 15 | fschemescore | 方案总分 | numeric | 23 | 10 | √ | 0 | 方案总分 |
| 16 | flowvalue | 提醒值(<=) | numeric | 23 | 10 | √ | 0 | 提醒值(<=) |
| 17 | fisopinion | 是否选择项 | bpchar | 1 |  | √ | '0' | 是否选择项 |
| 18 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 19 | fvaluebizobject | 关联的业务对象 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 20 | findex | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 21 | ffieldname | 关联的业务对象字段 | varchar | 50 |  | √ | ' ' | 关联的业务对象字段,枚举: |
| 22 | fproperty | 指标性质 | bpchar | 1 |  | √ | ' ' | 指标性质,枚举: 1 :定量指标 2 :定性指标 |
| 23 | fisfitted | 是否符合项 | bpchar | 1 |  | √ | '0' | 是否符合项 |
| 24 | fvaluetype | 指标值类型 | bpchar | 1 |  | √ | '0' | 指标值类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉列表 |
| 25 | findexlibid | 指标编码 | int8 | 64 |  | √ | 0 | [指标库 src_index](../src_files/src_index.md) |
| 26 | fsupplierid | fsupplierid | int8 | 64 |  | √ | 0 |  |
| 27 | fisthreshold | 是否门槛 | bpchar | 1 |  | √ | '0' | 是否门槛 |
| 28 | findextypeid | 指标类型 | int8 | 64 |  | √ | 0 | [指标类型 src_indexclass](../src_files/src_indexclass.md) |
| 29 | fitemtype | 指标可编辑性 | bpchar | 1 |  | √ | '1' | 指标可编辑性,枚举: 1 :采供双方均可编辑 2 :供应商可编辑，采购方可见不可编辑 3 :采购方可编辑，供应商可见不可编辑 4 :采购方可编辑，供应商不可见 |
| 30 | fscoremethod | 评分方法 | bpchar | 1 |  | √ | '1' | 评分方法,枚举: 1 :百分制(每个指标按百分制评分，方案=100分) 2 :实际值实际值(每个指标按实际值评分，方案=100分) 3 :最终值(每个指标按最终值评分，方案<100分) |
| 31 | fisdeduct | 扣分指标 | bpchar | 1 |  | √ | '0' | 扣分指标 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fscore | 标准分值(权重) | numeric | 19 | 6 | √ | 0 | 标准分值(权重) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_schemeindex_fsrcid |  | fsrcindexid |
| 2 | idx_src_schemeindex_findex |  | findex |
| 3 | idx_src_schemeindex_flibid |  | findexlibid |
| 4 | idx_src_schemeindex_fsrclibid |  | fsrcindexlibid |
| 5 | pk_src_schemeindex |  | fentryid |
| 6 | idx_src_schemeindex_fid |  | fid |
| 7 | idx_src_schemeindex_fsid |  | fsupplierid |

---

## 指标分录-多语言表 t_src_schemeindex_l

- **表名称：** 指标分录-多语言表
- **表名：** t_src_schemeindex_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | findexdimension | 指标维度 | varchar | 500 |  | √ | ' ' | 指标维度 |
| 2 | findex | 指标名称 | varchar | 500 |  | √ | ' ' | 指标名称 |
| 3 | findexrule | 评分标准 | varchar | 1020 |  | √ | ' ' | 评分标准 |
| 4 | fnote | 备注 | varchar | 500 |  | √ | ' ' | 备注 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_schemeindex_l |  | fpkid |
| 2 | idx_src_schemeindex_l_fid |  | fentryid,flocaleid |

---

## 寻源方式-多选基础资料表 t_src_schemesourcetype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_src_schemesourcetype

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
| 1 | pk_src_schemesourcetype |  | fpkid |
| 2 | idx_src_schemesourcetype_bid |  | fbasedataid |
| 3 | idx_src_schemesourcetype_fid |  | fid |

---

## 采购部门-多选基础资料表 t_src_schemepurdept

- **表名称：** 采购部门-多选基础资料表
- **表名：** t_src_schemepurdept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [采购部门 pds_purdepart](../pds_files/pds_purdepart.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_schemepurdept |  | fpkid |
| 2 | idx_src_schemepurdept_fid |  | fid |

---

## 参数分录-子表 t_src_schemeparams

- **表名称：** 参数分录-子表
- **表名：** t_src_schemeparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | [招标辅助资料 pds_extdata](../pds_files/pds_extdata.md) |
| 4 | fparamname | fparamname | varchar | 50 |  | √ | ' ' |  |
| 5 | fbasedatainfo | 参数说明 | varchar | 512 |  | √ | ' ' | 参数说明 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fismust | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 8 | fparamtype | fparamtype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_schemeparams |  | fentryid |
| 2 | idx_src_schemeparams_fid |  | fid |

---

## 项目方案配置-使用范围表 t_src_scheme_u

- **表名称：** 项目方案配置-使用范围表
- **表名：** t_src_scheme_u

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
| 1 | pk_t_src_scheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_src_scheme_u_uo |  | fuseorgid |

---

## 项目方案配置-多语言表 t_src_scheme_l

- **表名称：** 项目方案配置-多语言表
- **表名：** t_src_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 600 |  | √ | ' ' | 备注 |
| 3 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_scheme_l_fname |  | fname |
| 2 | pk_src_scheme_l |  | fpkid |

---

## 项目方案配置-使用范围位图表 t_src_scheme_m

- **表名称：** 项目方案配置-使用范围位图表
- **表名：** t_src_scheme_m

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
| 1 | pk_t_src_scheme_m |  | forgid |

---

## 采购组织-多选基础资料表 t_src_schemepurorg

- **表名称：** 采购组织-多选基础资料表
- **表名：** t_src_schemepurorg

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
| 1 | idx_src_schemepurorg_fid |  | fid |
| 2 | idx_src_schemepurorg_bid |  | fbasedataid |
| 3 | pk_src_schemepurorg |  | fpkid |

---

## 专家考评周期-多选基础资料表 t_src_schemeperiod

- **表名称：** 专家考评周期-多选基础资料表
- **表名：** t_src_schemeperiod

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
| 1 | idx_src_schemeperiod_fid |  | fid |
| 2 | pk_src_schemeperiod |  | fpkid |
