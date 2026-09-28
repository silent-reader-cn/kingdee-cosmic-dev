# 分析框架-cbi_agent_analysis

## 分析框架-主表 t_cbi_agent_analysis

- **表名称：** 分析框架-主表
- **表名：** t_cbi_agent_analysis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | fstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :已启用 0 :已停用 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 7 | fpicturefield | 图片字段 | text | 0 |  |  | null | 图片字段 |
| 8 | fagentbaseid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 9 | fkeyword | 触发词 | varchar | 500 |  | √ | ' ' | 触发词 |
| 10 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_analysis |  | fid |

---

## 单据体-子表 t_cbi_agent_analysisentry

- **表名称：** 单据体-子表
- **表名：** t_cbi_agent_analysisentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatetype | 时间类型 | varchar | 50 |  | √ | ' ' | 时间类型 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 4 | foutformat_tag | 自定义内容_详情 | text | 0 |  |  | null | 自定义内容_详情 |
| 5 | ftitle | 章节标题 | varchar | 500 |  | √ | ' ' | 章节标题 |
| 6 | ftype | 章节类型 | varchar | 50 |  | √ | ' ' | 章节类型 |
| 7 | fdatevalue | 时间区间 | varchar | 50 |  | √ | ' ' | 时间区间 |
| 8 | foutformat | 自定义内容 | varchar | 255 |  | √ | ' ' | 自定义内容 |
| 9 | fprompt_tag | 总结思路_详情 | text | 0 |  |  | null | 总结思路_详情 |
| 10 | fcustomformat | 自定义输出格式 | varchar | 10 |  | √ | ' ' | 自定义输出格式 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fmeasure | 分析指标 | varchar | 2000 |  | √ | ' ' | 分析指标 |
| 13 | fdimension | 分析维度 | varchar | 1000 |  | √ | ' ' | 分析维度 |
| 14 | fprompt | 总结思路 | varchar | 255 |  | √ | ' ' | 总结思路 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_analysisentry |  | fentryid |
