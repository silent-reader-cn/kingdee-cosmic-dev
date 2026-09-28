# 扩展过滤-pds_extfilter

## 插件分录-子表 t_pds_extfilterentry

- **表名称：** 插件分录-子表
- **表名：** t_pds_extfilterentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fnote | 过滤插件说明 | varchar | 255 |  | √ | ' ' | 过滤插件说明 |
| 4 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fpluginname | 过滤插件类名 | varchar | 100 |  | √ | ' ' | 过滤插件类名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_extfilterentry |  | fentryid |
| 2 | idx_pds_extfilterentry_fid |  | fid |

---

## 扩展过滤-多语言表 t_pds_extfilter_l

- **表名称：** 扩展过滤-多语言表
- **表名：** t_pds_extfilter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_extfilter_l |  | fpkid |
| 2 | idx_pds_extfilter_l |  | fid |

---

## 字段分录-子表 t_pds_extfilterfields

- **表名称：** 字段分录-子表
- **表名：** t_pds_extfilterfields

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称,枚举: |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | ffieldid | 字段标识 | varchar | 50 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extfilterfields_fid |  | fid |
| 2 | pk_pds_extfilterfields |  | fentryid |

---

## 扩展过滤-主表 t_pds_extfilter

- **表名称：** 扩展过滤-主表
- **表名：** t_pds_extfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 扩展过滤分组 pds_extfiltergroup |
| 3 | fismodifynode | 允许修改节点 | bpchar | 1 |  | √ | '0' | 允许修改节点 |
| 4 | fearlywarn | 预警频度 | varchar | 255 |  | √ | ' ' | 预警频度 |
| 5 | ffilterfield | 返回业务对象的哪个字段值 | varchar | 50 |  | √ | ' ' | 返回业务对象的哪个字段值,枚举: |
| 6 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcondition | 条件对象(后台字段) | varchar | 510 |  | √ | ' ' | 条件对象(后台字段) |
| 13 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | ' ' | 系统预置 |
| 14 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcondition_tag | 条件对象(后台字段)_详情 | text | 0 |  |  | null | 条件对象(后台字段)_详情 |
| 18 | fbasedataid | 待过滤的业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 22 | fbizobjectid | 值字段的业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 23 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 25 | forderby | 排序方式 | varchar | 50 |  | √ | ' ' | 排序方式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extfilter_enable |  | fenable |
| 2 | idx_pds_extfilter_status |  | fstatus |
| 3 | pk_pds_extfilter |  | fid |
| 4 | idx_pds_extfilter_fnumber |  | fnumber |
| 5 | idx_pds_extfilter_fbid |  | fbasedataid |

---

## 字段匹配分录-子表 t_pds_extfiltermatchfield

- **表名称：** 字段匹配分录-子表
- **表名：** t_pds_extfiltermatchfield

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchtype | 匹配方式 | varchar | 50 |  | √ | ' ' | 匹配方式,枚举: = :基础资料/多选基础资料/整数/ID/下拉列表 等于 ( = ) > :大于 ( > ） = :大于等于 ( >= ) :不等于 ( <> ) like :多选下拉列表/字符串 相似 ( like ) not like :多选下拉列表/字符串 不相似 ( not like ) in :在...之中 ( in ) (值为集合) not in :不在...之中 ( not in ) (值为集合) is null :为空 ( is null ) is not null :不为空 ( is not null ) match :匹配 ( match ) 全文检索 ftlike :ftlike(全文检索) exists :存在 ( exists ) 子查询 not exists :不存在 ( not exists ) 子查询 |
| 3 | fqueryfieldtype | 查询字段类型 | varchar | 50 |  | √ | ' ' | 查询字段类型 |
| 4 | ffieldtype | 字段名称 | varchar | 50 |  | √ | ' ' | 字段名称 |
| 5 | fvaluefield | 值字段 | varchar | 50 |  | √ | ' ' | 值字段,枚举: |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fvaluefieldtype | 值字段类型 | varchar | 50 |  | √ | ' ' | 值字段类型 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fqueryfield | 查询字段 | varchar | 50 |  | √ | ' ' | 查询字段,枚举: |
| 10 | ffieldnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fentryenable | 为空时不限制 | bpchar | 1 |  | √ | '1' | 为空时不限制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extfiltermatchfield_id |  | fid |
| 2 | pk_pds_extfiltermatchfield |  | fentryid |

---

## 参数分录-子表 t_pds_extparams

- **表名称：** 参数分录-子表
- **表名：** t_pds_extparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparamvalue | 默认值 | varchar | 512 |  | √ | ' ' | 默认值 |
| 3 | fparameterid | 参数编码 | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
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
| 1 | pk_pds_extparams |  | fentryid |
| 2 | idx_pds_extparams_fid |  | fid |

---

## 寻源流程-多选基础资料表 t_pds_extfilter_srcflow

- **表名称：** 寻源流程-多选基础资料表
- **表名：** t_pds_extfilter_srcflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 流程配置 pds_flowconfig |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extfilter_srcflow_fid |  | fid |
| 2 | pk_pds_extfilter_srcflow |  | fpkid |
| 3 | idx_pds_extfilter_srcflow_bid |  | fbasedataid |

---

## 寻源方式-多选基础资料表 t_pds_extfilter_srctype

- **表名称：** 寻源方式-多选基础资料表
- **表名：** t_pds_extfilter_srctype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 招标辅助资料 pds_extdata |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pds_extfilter_srctype_bid |  | fbasedataid |
| 2 | idx_pds_extfilter_srctype_fid |  | fid |
| 3 | pk_pds_extfilter_srctype |  | fpkid |
