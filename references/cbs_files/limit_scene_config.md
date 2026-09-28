# 限流场景配置-limit_scene_config

## 限流场景配置-多语言表 t_cbs_limit_scene_l

- **表名称：** 限流场景配置-多语言表
- **表名：** t_cbs_limit_scene_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 场景名 | varchar | 100 |  | √ | ' ' | 场景名 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_limit_scene_l |  | fpkid |
| 2 | idx_cbs_limit_scene_l_0 |  | fid,flocaleid |

---

## 限流场景配置-主表 t_cbs_limit_scene

- **表名称：** 限流场景配置-主表
- **表名：** t_cbs_limit_scene

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 场景名 | varchar | 500 |  | √ | ' ' | 场景名 |
| 3 | fcounter_type | fcounter_type | bpchar | 1 |  | √ | ' ' |  |
| 4 | fcreated | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmax_count | 最大次数 | int8 | 64 |  |  | 0 | 最大次数 |
| 6 | flimit_time | 熔断时长 | int8 | 64 |  |  | 0 | 熔断时长 |
| 7 | fdescription | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 8 | fupdated | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 9 | fwindow_time_unit | 窗口时间单位 | bpchar | 1 |  |  | ' ' | 窗口时间单位,枚举: 0 :秒 1 :分 2 :时 |
| 10 | flimit_time_unit | 熔断时长单位 | bpchar | 1 |  |  | ' ' | 熔断时长单位,枚举: 0 :秒 1 :分 2 :时 |
| 11 | ftype | 限流类型 | bpchar | 1 |  | √ | '0' | 限流类型,枚举: 0 :本地配置 1 :许可 |
| 12 | fmax_size | 最大大小 | int8 | 64 |  |  | 0 | 最大大小 |
| 13 | fwarn_threshold | 告警阈值 | int8 | 64 |  |  | 80 | 告警阈值 |
| 14 | frange | 限流范围 | bpchar | 1 |  | √ | ' ' | 限流范围,枚举: 0 :线程 1 :集群 2 :节点 |
| 15 | fexclude_package | 排除目录 | varchar | 1000 |  |  | ' ' | 排除目录 |
| 16 | finclude_package | 包含目录 | varchar | 1000 |  |  | ' ' | 包含目录 |
| 17 | fis_async | 是否异步 | bpchar | 1 |  | √ | '0' | 是否异步 |
| 18 | flimit_enable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 19 | falgorithm | 限流算法 | bpchar | 1 |  | √ | ' ' | 限流算法,枚举: 0 :计数器 1 :固定窗口 2 :滑动窗口 |
| 20 | fwarn_enable | 是否启用告警 | bpchar | 1 |  | √ | '0' | 是否启用告警 |
| 21 | fcode | 场景编码 | varchar | 100 |  | √ | ' ' | 场景编码 |
| 22 | fwindow_time | 窗口时间 | int8 | 64 |  |  | 0 | 窗口时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_limit_scene |  | fid |
| 2 | idx_cbs_limit_scene_fcode |  | fcode |
