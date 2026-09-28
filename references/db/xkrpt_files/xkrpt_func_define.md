# 自定义函数-xkrpt_func_define

## 取数设置-子表 t_xkrpt_func_value_para

- **表名称：** 取数设置-子表
- **表名：** t_xkrpt_func_value_para

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetresultfieldvalue | 对应来源字段值 | varchar | 100 |  | √ | ' ' | 对应来源字段值 |
| 3 | fsummarytype | 汇总类型 | varchar | 50 |  | √ | ' ' | 汇总类型,枚举: sum :SUM count :COUNT max :MAX min :MIN top :TOP 1 average :AVERAGE |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fitemdatatype | 项目数据类型 | int8 | 64 |  | √ | 0 | [项目数据类型 xkbd_rptitemdatatype](../fibd_files/xkbd_rptitemdatatype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_func_value_para_fid |  | fid |
| 2 | pk_xkrpt_func_value_para |  | fentryid |

---

## 自定义函数-多语言表 t_xkrpt_func_define_l

- **表名称：** 自定义函数-多语言表
- **表名：** t_xkrpt_func_define_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 函数名称 | varchar | 100 |  | √ | ' ' | 函数名称 |
| 3 | fdefaultfiltername | 前置条件 | varchar | 100 |  | √ | ' ' | 前置条件 |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkrpt_func_define_l |  | fpkid |
| 2 | idx_xkrpt_func_define_l_fid |  | fid,flocaleid |

---

## 自定义函数-主表 t_xkrpt_func_define

- **表名称：** 自定义函数-主表
- **表名：** t_xkrpt_func_define

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 函数名称 | varchar | 100 |  | √ | ' ' | 函数名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fdefaultfilter | 前置条件值 | varchar | 2000 |  | √ | ' ' | 前置条件值 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fvaluetype | 取值来源类型 | varchar | 50 |  | √ | ' ' | 取值来源类型,枚举: BaseFormModel :基础资料 BillFormModel :单据与基础资料 ReportFormModel :查询报表 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fdefaultfiltername | 前置条件 | varchar | 100 |  | √ | ' ' | 前置条件 |
| 12 | fsyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 函数编码 | varchar | 50 |  | √ | ' ' | 函数编码 |
| 15 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 16 | fforbiddate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 17 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fvaluedatatype | 取数来源 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_func_define_number |  | fnumber |
| 2 | pk_xkrpt_func_define |  | fid |

---

## 取数参数-子表 t_xkrpt_func_condition

- **表名称：** 取数参数-子表
- **表名：** t_xkrpt_func_condition

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | 比较符 | varchar | 50 |  | √ | ' ' | 比较符,枚举: equals :等于 large_than :大于 large_equals :大于等于 less_than :小于 less_equals :小于等于 not_equals :不等于 between :范围 in :列表 like :包含 not_like :不包含 |
| 3 | fmustinput | 必录 | bpchar | 1 |  | √ | '0' | 必录 |
| 4 | ftargetfieldvalue | 来源字段值 | varchar | 100 |  | √ | ' ' | 来源字段值 |
| 5 | fparadesc | 参数说明 | varchar | 255 |  | √ | ' ' | 参数说明 |
| 6 | fpara | 参数 | int8 | 64 |  | √ | 0 | [取数参数管理 xkrpt_func_paradefine](../xkrpt_files/xkrpt_func_paradefine.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fparamap | 报表属性与参数传递关系 | varchar | 100 |  | √ | ' ' | 报表属性与参数传递关系 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_func_condition_fid |  | fid |
| 2 | pk_xkrpt_func_condition |  | fentryid |

---

## 取数参数-多语言表 t_xkrpt_func_condition_l

- **表名称：** 取数参数-多语言表
- **表名：** t_xkrpt_func_condition_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparadesc | 参数说明 | varchar | 50 |  | √ | ' ' | 参数说明 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkrpt_func_cd_l_entryid |  | fentryid |
| 2 | pk_xkrpt_func_condition_l |  | fpkid |
