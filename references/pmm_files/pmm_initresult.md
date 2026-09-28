# 电商初始化结果-pmm_initresult

## 单据体-子表 t_mal_initressultentry

- **表名称：** 单据体-子表
- **表名：** t_mal_initressultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubtime | 耗时（毫秒） | int8 | 64 |  | √ | 0 | 耗时（毫秒） |
| 3 | fdetail | 执行详情 | varchar | 2000 |  | √ | ' ' | 执行详情 |
| 4 | fsubtaskid | 任务明细 | int8 | 64 |  | √ | 0 | 电商初始化任务 pmm_inittask |
| 5 | fsubstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fsubstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_initressultentry_fid |  | fid |
| 2 | pk_t_mal_initressultentry |  | fentryid |

---

## 电商初始化结果-主表 t_mal_initresult

- **表名称：** 电商初始化结果-主表
- **表名：** t_mal_initresult

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | femalauthid | 电商授权 | int8 | 64 |  | √ | 0 | 电商授权 pmm_ecadmit |
| 3 | ftime | 耗时（秒） | int8 | 64 |  | √ | 0 | 耗时（秒） |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fcontext | 运行上下文 | text | 0 |  |  | null | 运行上下文 |
| 7 | fprogress | 进度（%） | int8 | 64 |  | √ | 0 | 进度（%） |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fcontext_tag | 运行上下文_详情 | text | 0 |  |  | null | 运行上下文_详情 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: 1 :未执行 2 :执行中 3 :失败 4 :成功 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | ftaskid | 初始化任务 | int8 | 64 |  | √ | 0 | 电商初始化配置 pmm_initconfig |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_initresult |  | fid |
| 2 | idx_mal_initresult_emalauthid |  | ftaskid,femalauthid |
