# 配送模式-ocdbd_distributionmode

## 配送模式-主表 t_ocdbd_distributionmode

- **表名称：** 配送模式-主表
- **表名：** t_ocdbd_distributionmode

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 0 :配送 1 :自提 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 6 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | '1' | 系统预设 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ocdbd_distributionmode |  | fid |
| 2 | idx_ocdbd_distributionmode_num |  | fnumber |
