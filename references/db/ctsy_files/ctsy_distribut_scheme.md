# 主数据分发方案-ctsy_distribut_scheme

## 主数据分发方案-主表 t_ctsy_distributscheme

- **表名称：** 主数据分发方案-主表
- **表名：** t_ctsy_distributscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 分发对象 | int8 | 64 |  | √ | 0 | [主数据域管理 ctsy_domain](../ctsy_files/ctsy_domain.md) |
| 5 | fmanualswitch | 人工启动 | bpchar | 1 |  | √ | '1' | 人工启动 |
| 6 | feventswitch | 事件启动 | bpchar | 1 |  | √ | '1' | 事件启动 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fjob_mutex | 后台任务锁 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 9 | fbatch_size | 目标单批量大小 | int8 | 64 |  | √ | 0 | 目标单批量大小 |
| 10 | fvalidatedtime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 11 | fiscdataid | 数据集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | finterval | 执行频率 | varchar | 30 |  | √ | ' ' | 执行频率,枚举: 1 :执行频率 - 1次/小时 2 :执行频率 - 2次/小时 3 :执行频率 - 3次/小时 5 :执行频率 - 5次/小时 10 :执行频率 - 10次/小时 20 :执行频率 - 20次/小时 30 :执行频率 - 30次/小时 60 :执行频率 - 60次/小时 d :每天 d1 :每天凌晨一点 w :每周 0 :自定义 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fthread_ubound | 最大线程数 | int8 | 64 |  | √ | 0 | 最大线程数 |
| 18 | fscheduleswitch | 开启定时任务 | bpchar | 1 |  | √ | '0' | 开启定时任务 |
| 19 | fschedule | 触发间隔 | varchar | 30 |  | √ | ' ' | 触发间隔 |
| 20 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | ftraceall | 保存全部日志 | bpchar | 1 |  | √ | '0' | 保存全部日志 |
| 22 | fnumber | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 23 | fevents | 触发事件 | varchar | 1000 |  | √ | ' ' | 触发事件,枚举: |
| 24 | fexpiredtime | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctsy_distributscheme |  | fid |
| 2 | idx_t_ctsy_distributscheme_num |  | fnumber |

---

## 主数据分发方案-多语言表 t_ctsy_distributscheme_l

- **表名称：** 主数据分发方案-多语言表
- **表名：** t_ctsy_distributscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ctsy_distributscheme_l_fid |  | fid,flocaleid |
| 2 | pk_t_ctsy_distributscheme_l |  | fpkid |

---

## 过滤条件-子表 t_ctsy_distschemefilters

- **表名称：** 过滤条件-子表
- **表名：** t_ctsy_distschemefilters

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 3 | flink | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :并且 OR :或者 |
| 4 | fleftbracket | 左括号 | varchar | 30 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |
| 5 | frightbracket | 右括号 | varchar | 30 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 6 | ffiltercolumn | 条件字段 | varchar | 150 |  | √ | ' ' | 条件字段 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | ffilterlabel | 字段描述 | varchar | 150 |  | √ | ' ' | 字段描述 |
| 10 | fvaluefixed | 固定比较值 | varchar | 255 |  | √ | ' ' | 固定比较值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctsy_distschemefilters |  | fentryid |
| 2 | idx_ctsy_distschemefilters_fid |  | fid |

---

## 目标租户-多选基础资料表 t_ctsy_distschemetenants

- **表名称：** 目标租户-多选基础资料表
- **表名：** t_ctsy_distschemetenants

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [租户配置 ctsy_tenant](../ctsy_files/ctsy_tenant.md) |
| 3 | fisctriggerid | fisctriggerid | int8 | 64 |  | √ | 0 |  |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctsy_distschemetenants |  | fpkid |
| 2 | idx_ctsy_distschemetenants_fid |  | fid |
