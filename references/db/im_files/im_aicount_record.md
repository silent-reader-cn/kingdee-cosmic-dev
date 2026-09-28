# 盘点识别记录-im_aicount_record

## 盘点识别记录-主表 t_im_aicount_record

- **表名称：** 盘点识别记录-主表
- **表名：** t_im_aicount_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftraceid | traceid | varchar | 100 |  | √ | ' ' | traceid |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsessionid | sessionid | varchar | 100 |  | √ | ' ' | sessionid |
| 6 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 7 | fdatasource | 数据类型 | varchar | 50 |  | √ | ' ' | 数据类型 |
| 8 | fanalysetext | 解析文本 | varchar | 100 |  | √ | ' ' | 解析文本 |
| 9 | fanalysetext_tag | 解析文本_详情 | text | 0 |  |  | null | 解析文本_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_aicount_record_m0 |  | ftraceid,fsessionid,fbillid,fdatasource |
| 2 | pk_im_aicount_record |  | fid |
