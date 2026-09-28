# ID生成器-消费号-bos_cr_signer_record

## ID生成器-消费号-主表 t_signer_record

- **表名称：** ID生成器-消费号-主表
- **表名：** t_signer_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fkey | 关键字 | varchar | 512 |  | √ | ' ' | 关键字 |
| 3 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 4 | fentryid | fentryid | varchar | 36 |  | √ | ' ' |  |
| 5 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |
| 6 | fconsumeseq | 消费号 | int8 | 64 |  | √ | 0 | 消费号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_signer_record |  | fentryid |
| 2 | idx_signer_record_fk |  | fid |
