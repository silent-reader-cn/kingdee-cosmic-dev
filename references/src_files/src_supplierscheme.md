# 供应商选择方案-src_supplierscheme

## 供应商选择方案-多语言表 t_src_supscheme_l

- **表名称：** 供应商选择方案-多语言表
- **表名：** t_src_supscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supscheme_l |  | fpkid |
| 2 | idx_src_supscheme_l_fid |  | fid |

---

## 供应商选择方案-主表 t_src_supscheme

- **表名称：** 供应商选择方案-主表
- **表名：** t_src_supscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 300 |  | √ | ' ' | 方案名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcondition_tag | 条件对象(后台字段)_详情 | text | 0 |  |  | null | 条件对象(后台字段)_详情 |
| 6 | fmaindata | 二开供应商主数据(一般不需要设置) | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fbasedataid | 待过滤的基础资料 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fpriority | 优先级 | int4 | 32 |  | √ | 0 | 优先级 |
| 10 | ffieldname | 正式供应商字段 | varchar | 50 |  | √ | ' ' | 正式供应商字段,枚举: |
| 11 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | ffieldid | 字段标识 | varchar | 30 |  | √ | ' ' | 字段标识 |
| 13 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmatchfield | 匹配度 | int4 | 32 |  | √ | 0 | 匹配度 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 可用状态 | bpchar | 1 |  | √ | ' ' | 可用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fcondition | 条件对象(后台字段) | varchar | 510 |  | √ | ' ' | 条件对象(后台字段) |
| 21 | fnumber | 方案编码 | varchar | 30 |  | √ | ' ' | 方案编码 |
| 22 | fissyspreset | 系统预置 | int8 | 64 |  | √ | '0' | 系统预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supscheme_fenable |  | fenable |
| 2 | idx_src_supscheme_fnumber |  | fnumber |
| 3 | pk_src_supscheme |  | fid |
| 4 | idx_src_supscheme_fstatus |  | fstatus |

---

## 插件分录-子表 t_src_supschemeentry

- **表名称：** 插件分录-子表
- **表名：** t_src_supschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fnote | 过滤插件说明 | varchar | 255 |  | √ | ' ' | 过滤插件说明 |
| 4 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 5 | fdisplayfields | 显示的字段 | varchar | 500 |  | √ | ' ' | 显示的字段,枚举: |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fpluginname | 过滤插件类名 | varchar | 100 |  | √ | ' ' | 过滤插件类名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_src_supschemeentry |  | fentryid |
| 2 | idx_src_supschemeentry_fid |  | fid |

---

## 招标方式-多选基础资料表 t_src_supschemebase

- **表名称：** 招标方式-多选基础资料表
- **表名：** t_src_supschemebase

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
| 1 | pk_src_supschemebase |  | fpkid |
| 2 | idx_src_supschemebase_fid |  | fid |
| 3 | idx_src_supschemebase_bid |  | fbasedataid |

---

## 参数分录-子表 t_src_supschemeparams

- **表名称：** 参数分录-子表
- **表名：** t_src_supschemeparams

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
| 1 | pk_src_supschemeparams |  | fentryid |
| 2 | idx_src_supschemeparams_fid |  | fid |

---

## 字段匹配分录-子表 t_src_supschemefields

- **表名称：** 字段匹配分录-子表
- **表名：** t_src_supschemefields

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
| 11 | fentryenable | 为空时不限制 | bpchar | 1 |  | √ | '0' | 为空时不限制 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_supschemefields_fid |  | fid |
| 2 | pk_src_supschemefields |  | fentryid |
