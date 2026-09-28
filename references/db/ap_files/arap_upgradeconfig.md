# 数据升级任务配置-arap_upgradeconfig

## 数据升级任务配置-主表 t_arap_upgradeconfig

- **表名称：** 数据升级任务配置-主表
- **表名：** t_arap_upgradeconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatestarttime | 数据升级开始日期 | timestamp | 0 |  |  | null | 数据升级开始日期 |
| 3 | ftraceid | traceid | varchar | 30 |  | √ | ' ' | traceid |
| 4 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fexecutestatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 0 :待升级 1 :升级中 2 :升级完成 3 :升级失败 |
| 7 | fintervaldays | 间隔时间(天) | int4 | 32 |  | √ | 0 | 间隔时间(天) |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fdateendtime | 数据升级截止日期 | timestamp | 0 |  |  | null | 数据升级截止日期 |
| 10 | fplugin | 升级插件 | varchar | 100 |  | √ | ' ' | 升级插件 |
| 11 | fbizobj | 升级对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fisdefault | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 14 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_arap_upgradeplugin |  | fplugin |
| 2 | pk_t_arap_upgradeconfig |  | fid |
| 3 | idx_arap_upgradetime |  | fcreatetime |

---

## 单据体-子表 t_arap_upgradeentry

- **表名称：** 单据体-子表
- **表名：** t_arap_upgradeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftraceid | traceid | varchar | 30 |  | √ | ' ' | traceid |
| 3 | fexceptioninfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fexecutestatus | 执行状态 | varchar | 30 |  | √ | ' ' | 执行状态,枚举: 0 :待升级 1 :升级中 2 :升级完成 3 :升级失败 |
| 6 | ftaskenddate | 任务结束时间 | timestamp | 0 |  |  | null | 任务结束时间 |
| 7 | fexceptioninfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 8 | fexecutetimes | 已执行次数 | int4 | 32 |  | √ | 0 | 已执行次数 |
| 9 | fdatastartdate | 数据开始日期 | timestamp | 0 |  |  | null | 数据开始日期 |
| 10 | fisupgradeplugin | 是否升级插件执行 | bpchar | 1 |  | √ | '0' | 是否升级插件执行 |
| 11 | fdataenddate | 数据截止日期 | timestamp | 0 |  |  | null | 数据截止日期 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ftaskstartdate | 任务开始时间 | timestamp | 0 |  |  | null | 任务开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arap_upgradeentry |  | fentryid |
| 2 | idx_arap_upgradentry |  | fid |
