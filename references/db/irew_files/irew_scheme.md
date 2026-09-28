# 发票预警方案-irew_scheme

## 发票预警方案-多语言表 t_irew_scheme_l

- **表名称：** 发票预警方案-多语言表
- **表名：** t_irew_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_scheme_l |  | fpkid |
| 2 | idx_irew_scheme_l_0 |  | fid,flocaleid |

---

## 发票预警方案-使用范围位图表 t_irew_scheme_m

- **表名称：** 发票预警方案-使用范围位图表
- **表名：** t_irew_scheme_m

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
| 1 | pk_t_irew_scheme_m |  | forgid |

---

## 校验单据类型-多选基础资料表 t_irew_scheme_exptype

- **表名称：** 校验单据类型-多选基础资料表
- **表名：** t_irew_scheme_exptype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 手动添加单据类型 rim_expense_type |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_scheme_exptype_fk |  | fid |
| 2 | pk_irew_scheme_exptype |  | fpkid |

---

## 发票预警方案-使用范围表 t_irew_scheme_u

- **表名称：** 发票预警方案-使用范围表
- **表名：** t_irew_scheme_u

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
| 1 | idx_t_irew_scheme_u_uo |  | fuseorgid |
| 2 | pk_t_irew_scheme_u |  | fdataid,fuseorgid |

---

## 查询条件分录-子表 t_irew_scheme_condition

- **表名称：** 查询条件分录-子表
- **表名：** t_irew_scheme_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition_val | 值 | varchar | 200 |  | √ | ' ' | 值 |
| 3 | fcondition_key | 实体字段 | varchar | 150 |  | √ | ' ' | 实体字段 |
| 4 | fcondition_logic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑,枚举: and :并且 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fcondition | 条件 | int8 | 64 |  | √ | 0 | 查询条件 irew_query_condition |
| 7 | fcondition_val_hide | 隐藏值 | varchar | 200 |  | √ | ' ' | 隐藏值 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_irew_scheme_condition |  | fentryid |
| 2 | idx_irew_scheme_condition_fk |  | fid |

---

## 方案适用组织-多选基础资料表 t_irew_scheme_useorg

- **表名称：** 方案适用组织-多选基础资料表
- **表名：** t_irew_scheme_useorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_scheme_useorg |  | fpkid |
| 2 | idx_irew_scheme_useorg_fk |  | fid |

---

## 引擎清单-子表 t_irew_scheme_engine

- **表名称：** 引擎清单-子表
- **表名：** t_irew_scheme_engine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcheklevel | 校验等级 | varchar | 10 |  | √ | ' ' | 校验等级,枚举: 0 :高（严格管控） 1 :中（中度警示） 2 :低（轻度提示） |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fengine | 引擎编号 | int8 | 64 |  | √ | 0 | 发票校验引擎 irew_engine |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_scheme_engine |  | fentryid |
| 2 | idx_irew_scheme_engine_fk |  | fid |

---

## 发票预警方案-主表 t_irew_scheme

- **表名称：** 发票预警方案-主表
- **表名：** t_irew_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ffrequency | 审计频率 | varchar | 10 |  | √ | ' ' | 审计频率,枚举: 1 :每周 2 :每月 3 :每季度 4 :每半年 5 :每年 6 :自定义（天） |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fchecktype | 应用业务环节 | varchar | 10 |  | √ | ' ' | 应用业务环节,枚举: 1 :销项发票开具 2 :进项发票采集 3 :销项全票池审计 4 :进项全票池审计 |
| 12 | fstatus | 数据状态 | varchar | 8 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fstartdate | 审计开始执行时间 | timestamp | 0 |  |  | null | 审计开始执行时间 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | ffrequency_day | 审计频次（天） | int8 | 64 |  | √ | 0 | 审计频次（天） |
| 18 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 8 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fdaterange | 审计时间范围 | varchar | 50 |  | √ | ' ' | 审计时间范围,枚举: 1 :最近一周 2 :最近一月 3 :最近三月 4 :最近半年 5 :最近一年 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | flastexcutetime | 上次执行时间 | timestamp | 0 |  |  | null | 上次执行时间 |
| 23 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_scheme |  | fnumber,fname |
| 2 | idx_t_irew_scheme_createorg |  | fcreateorgid |
| 3 | pk_irew_scheme |  | fid |
| 4 | idx_t_irew_scheme_master |  | fmasterid |
