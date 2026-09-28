# 打印pdf附件设置-pds_print_pdf_set

## 打印pdf附件设置-主表 t_pds_print_pdf_set

- **表名称：** 打印pdf附件设置-主表
- **表名：** t_pds_print_pdf_set

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 主单据标识 | varchar | 50 |  | √ | ' ' | 主单据标识 |
| 3 | fcompkey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 4 | fentryattach | 分录附件 | varchar | 50 |  | √ | ' ' | 分录附件 |
| 5 | fbillattach | 单据附件 | varchar | 50 |  | √ | ' ' | 单据附件 |
| 6 | ftemplate | 打印模板 | varchar | 50 |  | √ | ' ' | 打印元数据 bos_print_meta |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pds_print_pdf_set |  | fid |
| 2 | idx_pds_print_pdf_set_en |  | fentityname |
| 3 | idx_pds_print_pdf_set_ck |  | fcompkey |
