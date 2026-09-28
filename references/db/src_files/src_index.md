# 指标库-src_index

## 采购组-多选基础资料表 t_src_indexpurgroup

- **表名称：** 采购组-多选基础资料表
- **表名：** t_src_indexpurgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购业务组(封存) bd_pmoperatorgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_indexpurgroup |  | fpkid |
| 2 | idx_src_indexpurgroup_bid |  | fbasedataid |
| 3 | idx_src_indexpurgroup_fid |  | fid |

---

## 指标库-多语言表 t_src_index_l

- **表名称：** 指标库-多语言表
- **表名：** t_src_index_l

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
| 1 | pk_src_index_l |  | fpkid |
| 2 | idx_src_index_l_id |  | fid,flocaleid |

---

## 指标库-主表 t_src_index

- **表名称：** 指标库-主表
- **表名：** t_src_index

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | findexdimension | 指标维度 | varchar | 255 |  | √ | ' ' | 指标维度 |
| 3 | ffiltertype | 数据获取方式 | bpchar | 1 |  | √ | '1' | 数据获取方式,枚举: 1 :通过关键字段直接获取 2 :组件，且通过父单据关联获取 3 :通过过滤插件获取 4 :通过扩展过滤方案获取 |
| 4 | fextplugin | 扩展过滤插件 | varchar | 255 |  | √ | ' ' | 扩展过滤插件 |
| 5 | findexrule | 评分标准 | varchar | 255 |  | √ | ' ' | 评分标准 |
| 6 | fvaluefield | 取值字段 | varchar | 50 |  | √ | ' ' | 取值字段,枚举: |
| 7 | fpentitykey | 父单据实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | findexclassid | 指标分类 | int8 | 64 |  | √ | 0 | 指标类型 src_indexclass |
| 13 | fcondition | 条件对象(后台字段) | varchar | 255 |  | √ | ' ' | 条件对象(后台字段) |
| 14 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 15 | fremark | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fthreshold | 门槛值 | numeric | 19 | 6 | √ | 0 | 门槛值 |
| 18 | fname | 名称 | varchar | 300 |  | √ | ' ' | 名称 |
| 19 | fkeyfield | 来源业务对象匹配的关键字段 | varchar | 50 |  | √ | ' ' | 来源业务对象匹配的关键字段,枚举: |
| 20 | fcondition_tag | 条件对象(后台字段)_详情 | text | 0 |  |  | null | 条件对象(后台字段)_详情 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fbizobject | 业务对象 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 23 | fproperty | 指标性质 | varchar | 30 |  | √ | ' ' | 指标性质,枚举: 1 :定量指标 2 :定性指标 |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fisfitted | 是否符合项 | bpchar | 1 |  | √ | '0' | 是否符合项 |
| 26 | fpkeyfield | 父单据匹配的关键字段 | varchar | 50 |  | √ | ' ' | 父单据匹配的关键字段,枚举: |
| 27 | fvaluetype | 指标值类型 | bpchar | 1 |  | √ | ' ' | 指标值类型,枚举: 0 :文本 1 :整数 2 :长整数 3 :小数 4 :日期 5 :长日期 6 :时间 7 :布尔类型 8 :基础资料 9 :下拉列表 A :多选下拉列表 |
| 28 | fdatefield | 日期过滤字段 | varchar | 100 |  | √ | ' ' | 日期过滤字段,枚举: |
| 29 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 30 | fisthreshold | 是否门槛 | bpchar | 1 |  | √ | '0' | 是否门槛 |
| 31 | fenable | 可用状态 | varchar | 30 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 33 | fextfilterid | 扩展过滤方案 | int8 | 64 |  | √ | 0 | 扩展过滤 pds_extfilter |
| 34 | forderby | 记录排序字段 | varchar | 100 |  | √ | ' ' | 记录排序字段,枚举: |
| 35 | fpluginname | 自动计算评分插件 | varchar | 100 |  | √ | ' ' | 自动计算评分插件 |
| 36 | fscore | fscore | numeric | 19 | 6 | √ | 0 |  |
| 37 | fmaxscore | 指标最高分值 | numeric | 23 | 10 | √ | 0 | 指标最高分值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_index_fnumber |  | fnumber |
| 2 | pk_src_index |  | fid |

---

## 评分规则分录-子表 t_src_indexentry

- **表名称：** 评分规则分录-子表
- **表名：** t_src_indexentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvaluefrom | 定量值从(大于等于) | numeric | 19 | 6 | √ | 0 | 定量值从(大于等于) |
| 3 | fvalueto | 定量值至(小于) | numeric | 19 | 6 | √ | 0 | 定量值至(小于) |
| 4 | fitemmaxscore | 最高得分(≤) | numeric | 23 | 10 | √ | 0 | 最高得分(≤) |
| 5 | fitem | 评分规则描述 | varchar | 1020 |  | √ | ' ' | 评分规则描述 |
| 6 | fitemvalue | 定性值 | varchar | 100 |  | √ | ' ' | 定性值 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 9 | fitemscore | 得分 | numeric | 19 | 6 | √ | 0 | 得分 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fitemminscore | 最低得分(≥) | numeric | 23 | 10 | √ | 0 | 最低得分(≥) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexentry_id |  | fid |
| 2 | pk_src_indexentry |  | fentryid |

---

## 采购部门-多选基础资料表 t_src_indexpurdept

- **表名称：** 采购部门-多选基础资料表
- **表名：** t_src_indexpurdept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 采购部门 pds_purdepart |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexpurdept_bid |  | fbasedataid |
| 2 | pk_src_indexpurdept |  | fpkid |
| 3 | idx_src_indexpurdept_fid |  | fid |

---

## 品类-多选基础资料表 t_src_indexcategory

- **表名称：** 品类-多选基础资料表
- **表名：** t_src_indexcategory

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexcategory_bid |  | fbasedataid |
| 2 | pk_src_indexcategory |  | fpkid |
| 3 | idx_src_indexcategory_fid |  | fid |

---

## 供应商得分分录-子表 t_src_indexsupentry

- **表名称：** 供应商得分分录-子表
- **表名：** t_src_indexsupentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuppliertype | 供应商类别 | varchar | 30 |  | √ | ' ' | 供应商类别,枚举: src_supplier :注册供应商 src_supplier_inner :内部供应商(员工) src_supplier_tmp :临时供应商 bd_supplier :供应商 |
| 3 | fsuppliername | 供应商名称 | varchar | 50 |  | √ | ' ' | 供应商名称 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fscore | 实际得分(百分制) | numeric | 23 | 10 | √ | 0 | 实际得分(百分制) |
| 7 | fsupplierid | 供应商编码 | int8 | 64 |  | √ | 0 | 注册供应商 src_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_indexsupentry_fid |  | fsupplierid |
| 2 | idx_src_entry_fscore |  | fscore |
| 3 | pk_src_indexsupentry |  | fentryid |
