# PLM单据轻扩展-plm_plmsm_bizextmeta

## PLM单据轻扩展-主表 t_plm_plmsm_bizextmeta

- **表名称：** PLM单据轻扩展-主表
- **表名：** t_plm_plmsm_bizextmeta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpdextmetadataid | 扩展模型单据 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 3 | fkey | 源对象键值 | varchar | 50 |  | √ | ' ' | 源对象键值 |
| 4 | fcfgextmetadataid | 配置模型单据 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_plmsm_bizextmeta_key |  | fkey |
| 2 | pk_t_plm_plmsm_bizextmeta |  | fid |
