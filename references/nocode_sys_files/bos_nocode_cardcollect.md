# 卡片收藏-bos_nocode_cardcollect

## 卡片收藏-主表 t_nocode_cardcollect

- **表名称：** 卡片收藏-主表
- **表名：** t_nocode_cardcollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcardid | 卡片id | int8 | 64 |  | √ | 0 | 卡片id |
| 3 | fuserid | 用户id | int8 | 64 |  | √ | 0 | 用户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_nocode_cardcollect |  | fid |
| 2 | idx_nc_cardc_userid |  | fuserid |
