# 下载记录（实体）-bdm_download_item

## 下载记录（实体）-主表 t_bdm_download_item

- **表名称：** 下载记录（实体）-主表
- **表名：** t_bdm_download_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间(yyyy-mm-dd) | varchar | 10 |  | √ | ' ' | 创建时间(yyyy-mm-dd) |
| 3 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | ffiletype | 文件类型 | varchar | 30 |  | √ | ' ' | 文件类型,枚举: excel :excel zip :zip |
| 5 | fdownloadnumber | 数量 | int8 | 64 |  | √ | 0 | 数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdm_download_item_id |  | fcreater |
| 2 | pk_bdm_download_item |  | fid |
