# 无代码分享表单记录-bos_nocode_share_record

## 无代码分享表单记录-主表 t_nocode_share_input

- **表名称：** 无代码分享表单记录-主表
- **表名：** t_nocode_share_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frecordid | 录入记录id | varchar | 50 |  |  | null | 录入记录id |
| 3 | fshareid | 分享id | varchar | 100 |  |  | null | 分享id |
| 4 | fip | 登录ip | varchar | 100 |  |  | null | 登录ip |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_nocode_share_input |  | fid |
| 2 | idx_share_id |  | fshareid |
