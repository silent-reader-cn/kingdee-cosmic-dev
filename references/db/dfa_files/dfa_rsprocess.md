# 推理过程-dfa_rsprocess

## 推理过程-主表 t_dfa_rsprocess

- **表名称：** 推理过程-主表
- **表名：** t_dfa_rsprocess

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fagentname | agent名称 | varchar | 100 |  | √ | ' ' | agent名称 |
| 3 | fcreator | fcreator | int8 | 64 |  | √ | 0 |  |
| 4 | fthinkcontent | 推理过程数据 | varchar | 255 |  | √ | ' ' | 推理过程数据 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | farragngeagentid | 自主编排agentid | int8 | 64 |  | √ | 0 | 自主编排agentid |
| 8 | fmodifier | fmodifier | int8 | 64 |  | √ | 0 |  |
| 9 | fthinkcontent_tag | 推理过程数据_详情 | text | 0 |  |  | null | 推理过程数据_详情 |
| 10 | frunid | 执行ID | varchar | 50 |  | √ | ' ' | 执行ID |
| 11 | fbizid | 业务ID | int8 | 64 |  | √ | 0 | 业务ID |
| 12 | fchatsessionid | 会话ID | varchar | 50 |  | √ | ' ' | 会话ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_rsbizid |  | fbizid |
| 2 | pk_dfa_rsprocess |  | fid |
