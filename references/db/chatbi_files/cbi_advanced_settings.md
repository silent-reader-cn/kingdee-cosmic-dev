# 高级配置-cbi_advanced_settings

## 高级配置-主表 t_cbi_advanced_settings

- **表名称：** 高级配置-主表
- **表名：** t_cbi_advanced_settings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimensionnumber | 文本 | varchar | 255 |  | √ | ' ' | 文本 |
| 3 | fsmartdatainterpret | 数据解读内容 | varchar | 2000 |  | √ | ' ' | 数据解读内容 |
| 4 | fforecastingepoch | 整数 | int4 | 32 |  | √ | 0 | 整数 |
| 5 | fischeckdimension | 复选框3 | bpchar | 1 |  | √ | '0' | 复选框3 |
| 6 | fisusepredictive | 复选框 | bpchar | 1 |  | √ | '0' | 复选框 |
| 7 | falertforecasting | 复选框 | bpchar | 1 |  | √ | '0' | 复选框 |
| 8 | fundimension | 多选下拉列表1 | varchar | 2000 |  | √ | ' ' | 多选下拉列表1,枚举: |
| 9 | fradiogroupfield | 单选按钮组 | varchar | 255 |  | √ | ' ' | 单选按钮组,枚举: 1 :Prophet 模型 2 :ARIMA 模型 |
| 10 | fdatamodelid | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 11 | fdimensionvalue | 维度值 ≤ | bpchar | 1 |  | √ | '0' | 维度值 ≤ |
| 12 | fundimensionvalue | 排除部分维度 | bpchar | 1 |  | √ | '0' | 排除部分维度 |
| 13 | fisdatainterpret | 复选框 | bpchar | 1 |  | √ | '0' | 复选框 |
| 14 | fdatainterpretideastext | 数据解读内容 | varchar | 2000 |  | √ | ' ' | 数据解读内容 |
| 15 | fagentbaseid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 16 | feffindicators | 多选下拉列表 | varchar | 2000 |  | √ | ' ' | 多选下拉列表,枚举: |
| 17 | flargeeffindicators | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 18 | fepochunit | 预测周期单位 | varchar | 10 |  | √ | ' ' | 预测周期单位,枚举: DAY :天 MONTH :月 YEAR :年 |
| 19 | flargeeffindicators_tag | 指标名称_详情 | text | 0 |  |  | null | 指标名称_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_advanced_settings_fk |  | fagentbaseid |
| 2 | pk_cbi_advanced_settings |  | fid |

---

## 树形单据体-子表 t_cbi_question_rewriting

- **表名称：** 树形单据体-子表
- **表名：** t_cbi_question_rewriting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frewritingenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 3 | frewritingphrase | 替换词 | varchar | 40 |  | √ | ' ' | 替换词 |
| 4 | fquestionphrase | 查询词 | varchar | 40 |  | √ | ' ' | 查询词 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_question_rewriting_fk |  | fid |
| 2 | pk_cbi_question_rewriting |  | fentryid |

---

## 单据体-子表 t_cbi_datamodel_prompt

- **表名称：** 单据体-子表
- **表名：** t_cbi_datamodel_prompt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffirstlevel | 一级分类 | varchar | 50 |  | √ | ' ' | 一级分类,枚举: NL2SQL :NL2DSL |
| 3 | fsecondlevel | 二级分类 | varchar | 50 |  | √ | ' ' | 二级分类 |
| 4 | fprompt_tag | Prompt_详情 | text | 0 |  |  | null | Prompt_详情 |
| 5 | favailable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillnofield | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fprompt | Prompt | varchar | 1000 |  | √ | ' ' | Prompt |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datamodel_prompt |  | fentryid |
| 2 | idx_cbi_datamodel_prompt_fk |  | fid |
