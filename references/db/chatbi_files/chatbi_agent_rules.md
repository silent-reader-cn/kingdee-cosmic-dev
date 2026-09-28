# 规则配置-chatbi_agent_rules

## 规则配置-主表 t_cbi_agent_rule

- **表名称：** 规则配置-主表
- **表名：** t_cbi_agent_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |
| 3 | frulelevel | 规则等级 | bpchar | 1 |  | √ | '1' | 规则等级,枚举: 0 :系统预置 1 :业务配置 2 :个人配置 |
| 4 | fruletype | 规则类型 | varchar | 20 |  | √ | ' ' | 规则类型,枚举: NV :虚拟指标1拖N NA :实际指标1拖N KCTopN :TOPN召回 KCBottomN :BottomN召回 KCRanking :KCRanking排行 KCUserDefinedFilter :自定义过滤条件 IfElse :IfElse条件规则 KCIsAchieveTarget :KCIsAchieveTarget达标 DefaultDim :维度缺省召回 RelateMetric :关联指标召回 CumulativeIndicator :累计指标规则处理 KCRankOfEntity :KCRankOfEntity排名 |
| 5 | fseq | 序号 | int4 | 32 |  | √ | 0 | 序号 |
| 6 | fmodifier | 最近更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fruledetail | 规则详情 | text | 0 |  |  | null | 规则详情 |
| 8 | fruledetail_tag | 规则详情_详情 | text | 0 |  |  | null | 规则详情_详情 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | fmodifydate | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 11 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fenable | 启用状态 | bpchar | 1 |  | √ | '1' | 启用状态 |
| 13 | frulename | 规则名称 | varchar | 200 |  | √ | ' ' | 规则名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_agent_rule_fagentid |  | fagentid |
| 2 | pk_cbi_agent_rule |  | fid |
