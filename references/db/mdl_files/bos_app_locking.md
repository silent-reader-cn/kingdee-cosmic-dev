# 锁定页面管理-bos_app_locking

## 锁定页面管理-主表 t_meta_locking

- **表名称：** 锁定页面管理-主表
- **表名：** t_meta_locking

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcloudname | 所属云名称 | varchar | 100 |  |  | null | 所属云名称 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | faccounttype | 账号类型 | varchar | 50 |  | √ | ' ' | 账号类型 |
| 5 | fformnumber | 页面编码 | varchar | 50 |  | √ | ' ' | 页面编码 |
| 6 | funitid | 分组id | varchar | 50 |  |  | null | 分组id |
| 7 | fbizappname | 应用名称 | varchar | 100 |  |  | null | 应用名称 |
| 8 | fbizappnumber | 应用编码 | varchar | 50 |  |  | null | 应用编码 |
| 9 | fcloudnumber | 所属云编码 | varchar | 50 |  |  | null | 所属云编码 |
| 10 | funitname | 分组名称 | varchar | 100 |  |  | null | 分组名称 |
| 11 | faccount | 账号 | varchar | 255 |  | √ | ' ' | 账号 |
| 12 | fformname | 页面名称 | varchar | 200 |  | √ | ' ' | 页面名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_meta_locking |  | fid |
| 2 | idx_kdp_locking_number |  | fformnumber |
