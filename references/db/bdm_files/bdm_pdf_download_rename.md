# pdf文件下载命名-bdm_pdf_download_rename

## pdf文件下载命名-主表 t_bdm_pdf_download_rename

- **表名称：** pdf文件下载命名-主表
- **表名：** t_bdm_pdf_download_rename

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnowinvoicepdfname | 发票命名规则 | varchar | 150 |  | √ | ' ' | 发票命名规则 |
| 3 | fnowredinfopdfname | 红字信息表命名规则 | varchar | 150 |  | √ | ' ' | 红字信息表命名规则 |
| 4 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatedatefield | fcreatedatefield | timestamp | 0 |  |  | null |  |
| 6 | fredinfopdfseparator | 红字信息表命名分隔符 | varchar | 50 |  | √ | ' ' | 红字信息表命名分隔符 |
| 7 | fmodifierfield | fmodifierfield | int8 | 64 |  | √ | 0 |  |
| 8 | forg | 组织 | int8 | 64 |  | √ | 0 | [企业管理 bdm_org](../bdm_files/bdm_org.md) |
| 9 | fcreaterfield | fcreaterfield | int8 | 64 |  | √ | 0 |  |
| 10 | fmodifydatefield | fmodifydatefield | timestamp | 0 |  |  | null |  |
| 11 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 12 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 13 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | finvoicepdfseparator | 发票命名分隔符 | varchar | 50 |  | √ | ' ' | 发票命名分隔符 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_pdf_download_rename |  | forg |
| 2 | pk_bdm_pdf_download_rename |  | fid |
