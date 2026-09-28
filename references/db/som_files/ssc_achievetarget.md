# 绩效指标-ssc_achievetarget

## 绩效指标-主表 t_tk_achievetarget

- **表名称：** 绩效指标-主表
- **表名：** t_tk_achievetarget

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fruleexpression | 计算公式 | varchar | 1000 |  | √ | ' ' | 计算公式 |
| 4 | fuseorg | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fruleexpjson_tag | 计算公式json_详情 | text | 0 |  |  | null | 计算公式json_详情 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 4 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fenddate | 有效日期范围.结束 | timestamp | 0 |  |  | null | 有效日期范围.结束 |
| 12 | fachievedesc | 指标说明 | varchar | 255 |  | √ | ' ' | 指标说明 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | ftargettype | 指标类型 | bpchar | 1 |  | √ | ' ' | 指标类型,枚举: 0 :计算指标 1 :综合指标 |
| 18 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fparentid | 上级指标 | int8 | 64 |  | √ | 0 | [绩效指标 ssc_achievetarget](../som_files/ssc_achievetarget.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 24 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 25 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 26 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 27 | fstartdate | 有效日期范围.开始 | timestamp | 0 |  |  | null | 有效日期范围.开始 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 31 | fruleexpjson | 计算公式json | varchar | 255 |  | √ | ' ' | 计算公式json |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_achievetarget |  | fid |
| 2 | idx_tk_achieve_target_no |  | fnumber |
| 3 | idx_t_tk_achievetarget_createorg |  | fcreateorgid |
| 4 | idx_t_tk_achievetarget_master |  | fmasterid |

---

## 绩效指标-使用范围位图表 t_tk_achievetarget_m

- **表名称：** 绩效指标-使用范围位图表
- **表名：** t_tk_achievetarget_m

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
| 1 | pk_t_tk_achievetarget_m |  | forgid |

---

## 绩效指标-多语言表 t_tk_achievetarget_l

- **表名称：** 绩效指标-多语言表
- **表名：** t_tk_achievetarget_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fachievedesc | 指标说明 | varchar | 255 |  | √ | ' ' | 指标说明 |
| 4 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_achievetarget_l |  | fpkid |
| 2 | idx_tk_achieve_target_locale |  | fid,flocaleid |

---

## 绩效指标-使用范围表 t_tk_achievetarget_u

- **表名称：** 绩效指标-使用范围表
- **表名：** t_tk_achievetarget_u

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
| 1 | idx_t_tk_achievetarget_u_uo |  | fuseorgid |
| 2 | pk_t_tk_achievetarget_u |  | fdataid,fuseorgid |
