# 每日资源提醒记录-ipop_dailyreswarnrecord

## 单据体-子表 t_ipop_dailyresuseentry

- **表名称：** 单据体-子表
- **表名：** t_ipop_dailyresuseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fresusejson_tag | 资源用量信息_详情 | text | 0 |  |  | null | 资源用量信息_详情 |
| 3 | fresusejson | 资源用量信息 | varchar | 255 |  | √ | ' ' | 资源用量信息 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fresnumber | 资源编码 | varchar | 50 |  | √ | ' ' | 资源编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_dailyresuseentry |  | fid |
| 2 | pk_t_ipop_dailyresuseentry |  | fentryid |

---

## 每日资源提醒记录-主表 t_ipop_dailyreswarnrecord

- **表名称：** 每日资源提醒记录-主表
- **表名：** t_ipop_dailyreswarnrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwarndate | 提醒日期 | timestamp | 0 |  |  | null | 提醒日期 |
| 3 | fhasnotifyresjson | 已提醒资源 | varchar | 2000 |  | √ | ' ' | 已提醒资源 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ipop_dailyreswarnrecord |  | fid |
| 2 | idx_ipop_dailyreswarnrecord |  | fwarndate |
