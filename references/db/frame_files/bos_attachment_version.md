# 附件版本维护-bos_attachment_version

## 附件版本维护-主表 t_bd_attach_version

- **表名称：** 附件版本维护-主表
- **表名：** t_bd_attach_version

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fattachid | 附件id | varchar | 50 |  | √ | ' ' | 附件id |
| 3 | fedittype | 文件编辑类型 | varchar | 10 |  | √ | ' ' | 文件编辑类型 |
| 4 | fversion | 当前版本 | int4 | 32 |  | √ | 0 | 当前版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_attach_version_attachid |  | fattachid |
| 2 | pk_t_bd_attach_version |  | fid |
