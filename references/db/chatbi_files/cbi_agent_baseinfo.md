# 智能体基本信息-cbi_agent_baseinfo

## 兜底配置-子表 t_cbi_fallback_response

- **表名称：** 兜底配置-子表
- **表名：** t_cbi_fallback_response

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 3 | fquestiontype | 问题类型 | varchar | 50 |  | √ | ' ' | 问题类型,枚举: notExistMeasure :查在途指标（查数超范围） persona :人设 simpleChat :闲聊 |
| 4 | ffixedfallback | 固定回复文案/Prompt配置 | varchar | 500 |  | √ | ' ' | 固定回复文案/Prompt配置 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ffallbacktype | 回复方式 | varchar | 50 |  | √ | ' ' | 回复方式,枚举: modelProcessing :模型处理 fixedReply :固定回复 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fqueryfield | 查询词 | varchar | 255 |  | √ | ' ' | 查询词 |
| 10 | ffallbackalias | 口语化别名 | varchar | 500 |  | √ | ' ' | 口语化别名 |
| 11 | ffallbackstatus | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_fallback_response |  | fentryid |
| 2 | idx_cbi_fallback_response_fk |  | fid |

---

## 智能体基本信息-主表 t_cbi_agent_baseinfo

- **表名称：** 智能体基本信息-主表
- **表名：** t_cbi_agent_baseinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffallbackresponse | 智能体人设 | varchar | 1000 |  |  | ' ' | 智能体人设 |
| 3 | fdialogprompttext | 对话框提示文本 | varchar | 200 |  |  | ' ' | 对话框提示文本 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 7 | fagentbaseid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 8 | fagentpersona | 智能体人设 | varchar | 1000 |  |  | ' ' | 智能体人设 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_baseinfo |  | fid |
