# 预留释放记录（废弃）-sbs_reserve_release

## 预留释放记录（废弃）-主表 t_sbs_reserve_release

- **表名称：** 预留释放记录（废弃）-主表
- **表名：** t_sbs_reserve_release

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freleaseqty | 基本释放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本释放数量 |
| 3 | freleaseunit2ndqty | 辅助释放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助释放数量 |
| 4 | freleaseunit3rdqty | 次辅释放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 次辅释放数量 |
| 5 | fop | 操作 | varchar | 10 |  | √ | ' ' | 操作 |
| 6 | freserveid | 预留记录ID | int8 | 64 |  | √ | 0 | 预留记录ID |
| 7 | fbillid | 单据ID | int8 | 64 |  | √ | 0 | 单据ID |
| 8 | fentryid | 分录ID | int8 | 64 |  | √ | 0 | 分录ID |
| 9 | freservereleaseqty | 释放数量 | numeric | 23 | 10 | √ | 0.0000000000 | 释放数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_sbs_reserve_release_pkey |  | fid |
| 2 | idx_sbs_rs_re_feid |  | fentryid |
| 3 | idx_sbs_rs_re_fbid |  | fbillid |
