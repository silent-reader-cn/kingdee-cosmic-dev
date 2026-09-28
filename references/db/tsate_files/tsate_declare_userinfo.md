# 用户同步信息-tsate_declare_userinfo

## 用户同步信息-主表 t_tsate_declare_yhinfo

- **表名称：** 用户同步信息-主表
- **表名：** t_tsate_declare_yhinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuserid | 云合同步用户id | varchar | 50 |  | √ | ' ' | 云合同步用户id |
| 3 | fnumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tsate_declare_yhinfo |  | fnumber |
| 2 | pk_tsate_declare_yhinfo |  | fid |
