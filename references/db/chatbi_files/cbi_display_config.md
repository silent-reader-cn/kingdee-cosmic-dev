# 展示配置-cbi_display_config

## 单据体-子表 t_cbi_recommend_queries

- **表名称：** 单据体-子表
- **表名：** t_cbi_recommend_queries

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | frecommendedqueries | 推荐问法 | varchar | 255 |  | √ | ' ' | 推荐问法 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_recommend_queries_fk |  | fid |
| 2 | pk_cbi_recommend_queries |  | fentryid |

---

## 展示配置-主表 t_cbi_display_config

- **表名称：** 展示配置-主表
- **表名：** t_cbi_display_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentbaseid | 基础资料 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 3 | ftextfield | 文本 | varchar | 50 |  | √ | ' ' | 文本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_agent_display_config_f |  | fagentbaseid |
| 2 | pk_cbi_display_config |  | fid |
