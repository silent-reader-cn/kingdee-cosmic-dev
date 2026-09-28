# 点击详情-ipop_clickdetailinfo

## 点击详情-主表 t_ipop_clickdetailinfo

- **表名称：** 点击详情-主表
- **表名：** t_ipop_clickdetailinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foptime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 3 | fsync | 是否同步 | varchar | 1 |  | √ | '0' | 是否同步 |
| 4 | fsimplecode | 简码 | varchar | 50 |  | √ | ' ' | 简码 |
| 5 | foptype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 6 | furl | 跳转链接 | varchar | 2000 |  | √ | ' ' | 跳转链接 |
| 7 | fresname | 资源名称 | varchar | 50 |  | √ | ' ' | 资源名称 |
| 8 | fresnumber | 资源编码 | varchar | 50 |  | √ | ' ' | 资源编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_clickdetailinfo_sync |  | fsync |
| 2 | pk_ipop_clickdetailinfo |  | fid |
