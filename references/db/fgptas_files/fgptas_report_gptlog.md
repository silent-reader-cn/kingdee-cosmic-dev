# GPT提示调用日志-fgptas_report_gptlog

## GPT提示调用日志-主表 t_fgptas_report_gptlog

- **表名称：** GPT提示调用日志-主表
- **表名：** t_fgptas_report_gptlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 3 | fgpttaskid | GPTtaskid | varchar | 200 |  | √ | ' ' | GPTtaskid |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fgptinputjson | GPT接口输入 | varchar | 2000 |  | √ | ' ' | GPT接口输入 |
| 6 | fgptstatus | GPT接口状态 | int8 | 64 |  | √ | 0 | GPT接口状态 |
| 7 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fgptresultjson | GPT接口结果 | varchar | 2000 |  | √ | ' ' | GPT接口结果 |
| 9 | fdocid | 文档KEY | varchar | 100 |  | √ | ' ' | 文档KEY |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsequence | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 13 | fgptnumber | GPT编码 | varchar | 200 |  | √ | ' ' | GPT编码 |
| 14 | fwordid | 财务报告id | int8 | 64 |  | √ | 0 | 财务报告 fgptas_report |
| 15 | freportlog | 报告生成日志 | varchar | 255 |  | √ | ' ' | 报告生成日志 |
| 16 | freportlog_tag | 报告生成日志_详情 | text | 0 |  |  | null | 报告生成日志_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fgptas_gptlog_gptnumber |  | fgptnumber |
| 2 | pk_fgptas_report_gptlog |  | fid |
