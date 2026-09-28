# 集成智能机器人-isc_smart_robot

## 集成智能机器人-主表 t_isc_smart_robot

- **表名称：** 集成智能机器人-主表
- **表名：** t_isc_smart_robot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | flabel | 标签 | varchar | 50 |  | √ | ' ' | 标签 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsuggest_model | 建议的AI实例 | varchar | 100 |  | √ | ' ' | 建议的AI实例 |
| 7 | fmodel_style | 模型风格 | varchar | 50 |  | √ | ' ' | 模型风格,枚举: CREATIVITY :创意 BALANCE :平衡 PRECISION :精准 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | flanguage_model | 绑定的AI实例 | varchar | 100 |  | √ | ' ' | 绑定的AI实例 |
| 10 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: T :提示语 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fscene | 适用场景 | varchar | 50 |  | √ | ' ' | 适用场景 |
| 13 | fprompt_tag | 提示词_详情 | text | 0 |  |  | null | 提示词_详情 |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |
| 16 | fdesc | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 17 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 18 | fprompt | 提示词 | varchar | 255 |  | √ | ' ' | 提示词 |
| 19 | fremembercount | 包含历史消息 | int4 | 32 |  | √ | 0 | 包含历史消息 |
| 20 | fcosmicversion | 适配苍穹版本 | varchar | 50 |  | √ | ' ' | 适配苍穹版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_t_isc_smart_robot_n |  | fnumber |
| 2 | pk_t_isc_smart_robot |  | fid |

---

## 单据体-子表 t_isc_smart_robot_v

- **表名称：** 单据体-子表
- **表名：** t_isc_smart_robot_v

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvar | 变量 | varchar | 20 |  | √ | ' ' | 变量 |
| 3 | fvartype | 字段类型 | varchar | 50 |  | √ | ' ' | 字段类型,枚举: String :文本 Integer :数字 DateTime :日期/时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvarname | 字段名称 | varchar | 20 |  | √ | ' ' | 字段名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_smart_robot_v |  | fentryid |
| 2 | index_smart_robot_v |  | fid |
