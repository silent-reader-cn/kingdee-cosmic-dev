# 模板版本-conm_tempfileentry

## 模板版本-主表 t_conm_attachentry

- **表名称：** 模板版本-主表
- **表名：** t_conm_attachentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fenablestatus | 启用状态 | varchar | 5 |  | √ | ' ' | 启用状态 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | ftemplatenum | 编号 | varchar | 80 |  | √ | ' ' | 编号 |
| 5 | ffilename | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | ffilemodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fversion | 版本号 | varchar | 80 |  | √ | ' ' | 版本号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_conm_attachentry |  | fentryid |
| 2 | idx_conm_attachentry_fid |  | fid |
