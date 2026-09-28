# 发票校验引擎-irew_engine

## 引擎规则依据单据体-子表 t_irew_engine_accord

- **表名称：** 引擎规则依据单据体-子表
- **表名：** t_irew_engine_accord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccording_file_path | 文件地址 | varchar | 200 |  | √ | ' ' | 文件地址 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | faccording_name | 政策法规名称/内部发文 | varchar | 200 |  | √ | ' ' | 政策法规名称/内部发文 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_engine_accord |  | fentryid |
| 2 | idx_irew_engine_accord_fk |  | fid |

---

## 发票数据校验规则单据体-子表 t_irew_engine_rule

- **表名称：** 发票数据校验规则单据体-子表
- **表名：** t_irew_engine_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalid_value | 值 | varchar | 200 |  | √ | ' ' | 值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | finvoice_type | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型 |
| 5 | fcondition | 条件 | varchar | 20 |  | √ | ' ' | 条件,枚举: = :等于 |
| 6 | finvoice_field | 发票字段 | varchar | 50 |  | √ | ' ' | 发票字段,枚举: |
| 7 | flogic | 逻辑 | varchar | 10 |  | √ | ' ' | 逻辑,枚举: && :并且 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_engine_rule |  | fentryid |
| 2 | idx_irew_engine_rule_fk |  | fid |

---

## 发票校验引擎-使用范围表 t_irew_engine_u

- **表名称：** 发票校验引擎-使用范围表
- **表名：** t_irew_engine_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | 0 |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_irew_engine_u |  | fdataid,fuseorgid |
| 2 | idx_t_irew_engine_u_uo |  | fuseorgid |

---

## 单据体-子表 t_irew_engine_queryconfig

- **表名称：** 单据体-子表
- **表名：** t_irew_engine_queryconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition_entity | 实体 | varchar | 50 |  | √ | ' ' | 实体,枚举: |
| 3 | fcondition_val | 值 | varchar | 500 |  | √ | ' ' | 值 |
| 4 | fcondition_logic | 逻辑 | varchar | 10 |  | √ | ' ' | 逻辑,枚举: and :并且 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fquery_condition | 条件 | varchar | 20 |  | √ | ' ' | [查询条件 irew_query_condition](../irew_files/irew_query_condition.md) |
| 7 | fcondition_val_hide | 隐藏值 | varchar | 1000 |  | √ | ' ' | 隐藏值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fentity_filed | 实体字段 | varchar | 150 |  | √ | ' ' | 实体字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_engine_queryconfig_fk |  | fid |
| 2 | pk_irew_engine_queryconfig |  | fentryid |

---

## 发票校验引擎-使用范围位图表 t_irew_engine_m

- **表名称：** 发票校验引擎-使用范围位图表
- **表名：** t_irew_engine_m

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
| 1 | pk_t_irew_engine_m |  | forgid |

---

## 发票校验引擎-多语言表 t_irew_engine_l

- **表名称：** 发票校验引擎-多语言表
- **表名：** t_irew_engine_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 校验引擎名称 | varchar | 50 |  | √ | ' ' | 校验引擎名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_engine_l |  | fpkid |
| 2 | idx_irew_engine_l_0 |  | fid,flocaleid |

---

## 展示字段单据体-子表 t_irew_engine_queryfield

- **表名称：** 展示字段单据体-子表
- **表名：** t_irew_engine_queryfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquery_entity | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 3 | fquery_field | 字段 | varchar | 150 |  | √ | ' ' | 字段 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fquery_field_name | 字段名 | varchar | 50 |  | √ | ' ' | 字段名 |
| 6 | fquery_entity_name | 实体名 | varchar | 50 |  | √ | ' ' | 实体名 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_engine_queryfield |  | fentryid |
| 2 | idx_irew_engine_queryfield_fk |  | fid |

---

## 发票校验引擎-主表 t_irew_engine

- **表名称：** 发票校验引擎-主表
- **表名：** t_irew_engine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexpense_term | 报销期限(天) | varchar | 10 |  | √ | ' ' | 报销期限(天),枚举: 30 :30天 60 :60天 90 :90天 120 :120天 180 :180天 240 :240天 300 :300天 365 :365天 |
| 3 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsource | 引擎来源 | varchar | 8 |  | √ | ' ' | 引擎来源,枚举: 1 :系统预设 2 :自定义 |
| 7 | fcheck_type | 发票校验业务类型 | varchar | 8 |  | √ | ' ' | 发票校验业务类型,枚举: 1 :销项发票信息 2 :进项发票信息 3 :销项发票与其他数据源 4 :进项发票与其他数据源 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcheckresult | 风险等级 | varchar | 30 |  | √ | ' ' | 风险等级,枚举: 0 :暂无风险 1 :低风险 2 :中风险 3 :高风险 4 :高危风险 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fremark | 校验描述 | varchar | 500 |  | √ | ' ' | 校验描述 |
| 17 | fname | 校验引擎名称 | varchar | 50 |  | √ | ' ' | 校验引擎名称 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fover_year | 是否允许跨年 | varchar | 10 |  | √ | ' ' | 是否允许跨年,枚举: 1 :是 0 :否 |
| 21 | fctrlstrategy | 控制策略 | varchar | 8 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fcustom_tips | 异常自定义提示语，在发生该异常时帮助客户更好业务处理 | varchar | 100 |  | √ | ' ' | 异常自定义提示语，在发生该异常时帮助客户更好业务处理 |
| 23 | fbasedatafield | 主实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 24 | fenable | 使用状态 | varchar | 4 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 校验引擎编码 | varchar | 30 |  | √ | ' ' | 校验引擎编码 |
| 26 | fcheck_according | 校验依据 | varchar | 50 |  | √ | ' ' | 校验依据,枚举: 1 :税法政策要求 2 :企业内部风控 |
| 27 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 28 | fclose_month | 第二年报销截止月份 | varchar | 10 |  | √ | ' ' | 第二年报销截止月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_engine_number |  | fnumber,fname |
| 2 | idx_t_irew_engine_createorg |  | fcreateorgid |
| 3 | idx_t_irew_engine_master |  | fmasterid |
| 4 | pk_irew_engine |  | fid |

---

## 关系单据体-子表 t_irew_engine_relation

- **表名称：** 关系单据体-子表
- **表名：** t_irew_engine_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frelation_condition | 条件 | varchar | 20 |  | √ | ' ' | 条件,枚举: = :等于 |
| 3 | fmain_entity_field | 实体A字段 | varchar | 150 |  | √ | ' ' | 实体A字段 |
| 4 | fsource_entity | 实体B | varchar | 50 |  | √ | ' ' | 实体B,枚举: |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fsource_entity_field | 实体B字段 | varchar | 150 |  | √ | ' ' | 实体B字段 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmain_entity | 实体A | varchar | 50 |  | √ | ' ' | 实体A,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_engine_relation_fk |  | fid |
| 2 | pk_irew_engine_relation |  | fentryid |

---

## 数据源单据体-子表 t_irew_engine_source

- **表名称：** 数据源单据体-子表
- **表名：** t_irew_engine_source

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsource_name | 数据来源 | varchar | 8 |  | √ | ' ' | 数据来源 |
| 3 | fsource_type | 类型 | varchar | 8 |  | √ | ' ' | 类型 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fsource_code | 数据来源编码 | varchar | 50 |  | √ | ' ' | 数据来源编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_engine_source_fk |  | fid |
| 2 | pk_irew_engine_source |  | fentryid |

---

## 其他数据源校验规则单据体-子表 t_irew_engine_sourcerule

- **表名称：** 其他数据源校验规则单据体-子表
- **表名：** t_irew_engine_sourcerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompare_type | 校验规则 | varchar | 10 |  | √ | ' ' | 校验规则,枚举: 1 :原值比较 2 :忽略大小写 3 :忽略全角半角括号 |
| 3 | ffinal_value | 固定值 | varchar | 36 |  | √ | ' ' | 固定值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | finvoice_type | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型 |
| 6 | fcondition | 条件 | varchar | 20 |  | √ | ' ' | [查询条件 irew_query_condition](../irew_files/irew_query_condition.md) |
| 7 | finvoice_field | 发票字段 | varchar | 150 |  | √ | ' ' | 发票字段 |
| 8 | fdata_source | 数据源 | varchar | 50 |  | √ | ' ' | 数据源,枚举: |
| 9 | flogic | 逻辑 | varchar | 10 |  | √ | ' ' | 逻辑,枚举: && :并且 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fdata_source_field | 数据源字段/固定值 | varchar | 150 |  | √ | ' ' | 数据源字段/固定值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_engine_sourcerule_fk |  | fid |
| 2 | pk_irew_engine_sourcerule |  | fentryid |
