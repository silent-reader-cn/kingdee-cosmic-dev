# 全球税底稿左树-gtcp_draft_tab

## 全球税底稿左树-主表 t_gtcp_draft_tab

- **表名称：** 全球税底稿左树-主表
- **表名：** t_gtcp_draft_tab

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdraftid | 计提底稿id | int8 | 64 |  | √ | 0 | 计提底稿id |
| 3 | ftaxareagroup | 税收辖区 | int8 | 64 |  | √ | 0 | [税收辖区 bastax_taxareagroup](../basedata_files/bastax_taxareagroup.md) |
| 4 | ftab | 页签名称 | varchar | 200 |  | √ | ' ' | 页签名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_gtcp_draft_tab |  | fid |
| 2 | t_gtcp_draft_tab_fdraftid_idx |  | fdraftid |
