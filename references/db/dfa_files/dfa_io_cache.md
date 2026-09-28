# IO缓存-dfa_io_cache

## IO缓存-主表 t_dfa_io_cache

- **表名称：** IO缓存-主表
- **表名：** t_dfa_io_cache

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fupdate_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fhits | 命中次数 | int8 | 64 |  | √ | 0 | 命中次数 |
| 5 | fio_contextid | IO上下文ID | varchar | 50 |  | √ | ' ' | IO上下文ID |
| 6 | fio_type | IO类型 | varchar | 50 |  | √ | ' ' | IO类型,枚举: agent_io :agent_io action_io :action_io res_resp_io :res_resp_io |
| 7 | fcache_version | 缓存版本号 | varchar | 50 |  | √ | ' ' | 缓存版本号 |
| 8 | fio_status | fio_status | varchar | 50 |  | √ | ' ' |  |
| 9 | fscenario_condition | 场景条件json | varchar | 255 |  | √ | ' ' | 场景条件json |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fenable | 是否可用 | bpchar | 1 |  |  | '1' | 是否可用 |
| 12 | fsource_input | 原始输入 | varchar | 250 |  | √ | ' ' | 原始输入 |
| 13 | flang | 语言类型 | varchar | 50 |  | √ | ' ' | 语言类型,枚举: zh-CN :中文简体 zh-TW :中文繁体 en-US :英文 ms-MY :马来语 vi-VN :越南语 th-TH :泰语 id-ID :印尼语 ar-001 :阿拉伯语 |
| 14 | fscenario_condition_tag | 场景条件json_详情 | text | 0 |  |  | null | 场景条件json_详情 |
| 15 | fio_key | io_key | varchar | 50 |  | √ | ' ' | io_key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_io_cache |  | fio_key |
| 2 | pk_dfa_io_cache |  | fid |
