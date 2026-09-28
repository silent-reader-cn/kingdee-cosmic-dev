# 卡片容器-bos_nocode_cardcontainer

## 卡片容器-主表 t_nocode_cardcontainer

- **表名称：** 卡片容器-主表
- **表名：** t_nocode_cardcontainer

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fw | 宽度 | int8 | 64 |  | √ | 0 | 宽度 |
| 3 | fpageid | 页面id | int8 | 64 |  | √ | 0 | 页面id |
| 4 | fx | x轴 | int8 | 64 |  | √ | 0 | x轴 |
| 5 | fh | 高度 | int8 | 64 |  | √ | 0 | 高度 |
| 6 | fy | y轴 | int8 | 64 |  | √ | 0 | y轴 |
| 7 | ftype | 类型 | int8 | 64 |  | √ | 0 | 类型 |
| 8 | fcardid | 卡片ID | int8 | 64 |  | √ | 0 | 卡片ID |
| 9 | fschemaid | 视图ID | int8 | 64 |  | √ | 0 | 视图ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_cardcontainer |  | fid |
| 2 | idx_nc_ccon_schemaid |  | fschemaid |
