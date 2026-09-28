# 菜单简码-xkbos_simple_number

## 菜单简码-主表 t_xkbos_simple_num

- **表名称：** 菜单简码-主表
- **表名：** t_xkbos_simple_num

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 菜单名称 | varchar | 50 |  |  | null | 菜单名称 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fappid | 应用ID | varchar | 50 |  | √ | ' ' | 应用ID |
| 9 | fcloudname | 云名称 | varchar | 50 |  |  | null | 云名称 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsimplenumber | 菜单简码 | varchar | 50 |  | √ | ' ' | 菜单简码 |
| 12 | fcloudid | 云ID | varchar | 50 |  | √ | ' ' | 云ID |
| 13 | fappname | 应用名称 | varchar | 50 |  |  | null | 应用名称 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmenuid | 菜单ID | varchar | 50 |  | √ | ' ' | 菜单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_simple_num |  | fsimplenumber |
| 2 | pk_t_xkbos_simple_num |  | fid |
| 3 | idx_app_menu_id |  | fmenuid |
| 4 | idx_app_id |  | fappid |
