# DAP内部参数（非开发勿动）-ai_dapconfig_snp

## DAP内部参数（非开发勿动）-主表 t_ai_dapconfig_snp

- **表名称：** DAP内部参数（非开发勿动）-主表
- **表名：** t_ai_dapconfig_snp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenlogger | DAP生成凭证内部日志 | bpchar | 1 |  | √ | ' ' | DAP生成凭证内部日志 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 5 | fallorgopen | 全组织参数（打开则上面组织账簿无效） | bpchar | 1 |  | √ | ' ' | 全组织参数（打开则上面组织账簿无效） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ai_dapconfig_snp |  | fid |
| 2 | idx_ai_dapconfig_snp_org |  | forgid |
