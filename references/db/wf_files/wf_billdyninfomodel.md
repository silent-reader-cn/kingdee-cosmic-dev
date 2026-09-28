# 单据动态信息模型-wf_billdyninfomodel

## 单据动态信息模型-主表 t_wf_billdyninfo

- **表名称：** 单据动态信息模型-主表
- **表名：** t_wf_billdyninfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人ID | int8 | 64 |  | √ | 0 | 修改人ID |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fformkey | PC页面formkey | varchar | 50 |  | √ | ' ' | PC页面formkey |
| 5 | fcreatorid | 创建人id | int8 | 64 |  | √ | 0 | 创建人id |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fsubject | 单据主题 | text | 0 |  |  | null | 单据主题 |
| 8 | foperationwhensave | 单据保存时调用的操作 | varchar | 36 |  | √ | ' ' | 单据保存时调用的操作 |
| 9 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 10 | factivityid | 当前节点id | varchar | 255 |  | √ | ' ' | 当前节点id |
| 11 | ffieldmodified | 单据字段是否可修改 | bpchar | 1 |  | √ | '0' | 单据字段是否可修改 |
| 12 | fmobileformkey | 移动页面formkey | varchar | 50 |  | √ | ' ' | 移动页面formkey |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_billdyninfo_pkey |  | fid |
| 2 | idx_wf_billdyninfo_pdef |  | fprocdefid |
