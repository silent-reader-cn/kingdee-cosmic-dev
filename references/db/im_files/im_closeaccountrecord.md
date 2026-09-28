# 关账记录-im_closeaccountrecord

## 关账记录-主表 t_im_closeacctrecord

- **表名称：** 关账记录-主表
- **表名：** t_im_closeacctrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fclosedate | 关账日期 | timestamp | 0 |  |  | null | 关账日期 |
| 4 | fisdelete | 是否删除 | bpchar | 1 |  | √ | ' ' | 是否删除 |
| 5 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_im_closred_foid |  | forgid |
| 2 | idx_im_closred_fwid |  | fwarehouseid |
| 3 | t_im_closeacctrecord_pkey |  | fid |
