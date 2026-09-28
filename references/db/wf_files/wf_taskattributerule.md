# 任务中心属性规则-wf_taskattributerule

## 任务中心属性规则-主表 t_wf_taskattributerule

- **表名称：** 任务中心属性规则-主表
- **表名：** t_wf_taskattributerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftype | 类型 | varchar | 100 |  |  | ' ' | 类型 |
| 5 | fconditionalruleid | 条件id | int8 | 64 |  | √ | 0 | 条件id |
| 6 | fexpression | 表达式 | varchar | 2000 |  | √ | ' ' | 表达式 |
| 7 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 8 | fautoexenexttask | 自动处理下一条任务 | bpchar | 1 |  | √ | '0' | 自动处理下一条任务 |
| 9 | factivitstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: enable :启用 disable :禁用 |
| 10 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |
| 11 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_taskattributerule_pkey |  | fid |
| 2 | idx_wf_taskattrrule_userid |  | fuserid |
| 3 | idx_wf_taskattrrule_number |  | fnumber |

---

## 任务中心属性规则-多语言表 t_wf_taskattributerule_l

- **表名称：** 任务中心属性规则-多语言表
- **表名：** t_wf_taskattributerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 230 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_taskattributerule_l |  | fid,flocaleid |
| 2 | t_wf_taskattributerule_l_pkey |  | fpkid |

---

## 单据体-子表 t_wf_taskoperationmeta

- **表名称：** 单据体-子表
- **表名：** t_wf_taskoperationmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperationkey | 操作标识 | varchar | 100 |  | √ | ' ' | 操作标识 |
| 3 | foperateparams | 操作参数 | text | 0 |  |  | null | 操作参数 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_taskoperationmeta_pkey |  | fentryid |
| 2 | idx_wf_taskopermeta_id |  | fid |
