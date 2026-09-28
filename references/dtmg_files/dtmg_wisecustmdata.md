# 数据迁移WISE自定义数据-dtmg_wisecustmdata

## 数据迁移WISE自定义数据-主表 t_dtmg_wisecustmdata

- **表名称：** 数据迁移WISE自定义数据-主表
- **表名：** t_dtmg_wisecustmdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetailkey | 子分录标识 | varchar | 50 |  | √ | ' ' | 子分录标识 |
| 3 | fobjecttypenumber | 业务单据编码 | varchar | 50 |  | √ | ' ' | 业务单据编码 |
| 4 | fdataid | 数据主键 | varchar | 50 |  | √ | ' ' | 数据主键 |
| 5 | fentrykey | 分录标识 | varchar | 50 |  | √ | ' ' | 分录标识 |
| 6 | fobjecttype | 业务单据 | varchar | 50 |  | √ | ' ' | 业务对象 bos_objecttype |
| 7 | fdetailid | 子分录主键 | varchar | 50 |  | √ | ' ' | 子分录主键 |
| 8 | fdata | 业务自定义数据 | varchar | 2000 |  | √ | ' ' | 业务自定义数据 |
| 9 | fentryid | 分录主键 | varchar | 50 |  | √ | ' ' | 分录主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dtmg_wisecustmdata |  | fid |
| 2 | idx_dtmg_wisecustmdata_data |  | fdataid |
