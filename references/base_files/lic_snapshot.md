# 许可快照管理-lic_snapshot

## 许可快照管理-主表 t_lic_snapshot

- **表名称：** 许可快照管理-主表
- **表名：** t_lic_snapshot

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatetime | 备份日期 | timestamp | 0 |  |  | null | 备份日期 |
| 3 | fdata_tag | 内容_详情 | text | 0 |  |  | null | 内容_详情 |
| 4 | fsnapshottype | 快照类型 | varchar | 50 |  | √ | ' ' | 快照类型,枚举: 0 :用户备份快照 1 :试算快照 2 :系统备份快照 |
| 5 | fdata | 内容 | text | 0 |  |  | null | 内容 |
| 6 | fistrial | 是否试算快照（废弃） | bpchar | 1 |  | √ | '0' | 是否试算快照（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_lic_snapshot_createtime |  | fcreatetime |
| 2 | pk_t_lic_snapshot |  | fid |
