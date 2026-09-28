# 质检信息记录-task_qualitymessagerecord

## 质检信息记录-主表 t_tk_qualitymessage

- **表名称：** 质检信息记录-主表
- **表名：** t_tk_qualitymessage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhandlemethod | 整改操作 | bpchar | 1 |  | √ | ' ' | 整改操作,枚举: 1 :整改完成 2 :申诉 |
| 3 | fpoint | 检查点 | int8 | 64 |  | √ | 0 | 检查点 |
| 4 | freviewmethod | 复核操作 | bpchar | 1 |  | √ | ' ' | 复核操作,枚举: 1 :整改通过 2 :申诉通过 3 :退回整改 |
| 5 | frebackcount | 打回次数 | int8 | 64 |  | √ | 0 | 打回次数 |
| 6 | fqualitycheck | 原质检任务id | int8 | 64 |  | √ | 0 | 原质检任务id |
| 7 | fischeckok | 是否合格 | bpchar | 1 |  | √ | '0' | 是否合格 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ssc_qualmsgtaskid |  | fqualitycheck |
| 2 | idx_ssc_qualmsgckpoint |  | fpoint |
| 3 | t_tk_qualitymessage_pkey |  | fid |

---

## 单据体-子表 t_tk_qualitymessageentry

- **表名称：** 单据体-子表
- **表名：** t_tk_qualitymessageentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 信息 | varchar | 1000 |  | √ | ' ' | 信息 |
| 3 | fusercheck | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisnewmessage | 是否是最新信息 | int8 | 64 |  | √ | 0 | 是否是最新信息 |
| 5 | fmessagetype | 信息类型 | bpchar | 1 |  | √ | ' ' | 信息类型,枚举: 0 :质检意见 1 :整改意见 2 :复核意见 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdatetime | 记录日期 | timestamp | 0 |  |  | null | 记录日期 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_qualitymessageentry_pkey |  | fentryid |
| 2 | idx_ssc_qualmsgentry |  | fid |
