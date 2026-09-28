# 水资源税源明细（暂存）-tcwat_source_detail_tp

## 水资源税源明细（暂存）-主表 t_tcwat_source_detail_tp

- **表名称：** 水资源税源明细（暂存）-主表
- **表名：** t_tcwat_source_detail_tp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqslqjxx | 取水量区间（下限） | numeric | 23 | 10 | √ | 0 | 取水量区间（下限） |
| 3 | fgqjse | 各区间税额 | numeric | 23 | 10 | √ | 0 | 各区间税额 |
| 4 | fsybl | 适用倍率 | numeric | 23 | 10 | √ | 0 | 适用倍率 |
| 5 | fsysl | 适用税率 | numeric | 23 | 10 | √ | 0 | 适用税率 |
| 6 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 申报表ID |
| 7 | fbqqsqgjl | 本期取水区各间量 | numeric | 23 | 10 | √ | 0 | 本期取水区各间量 |
| 8 | fwblbsjs | 未办理取水许可按标准税率倍数计税 | numeric | 23 | 10 | √ | 0 | 未办理取水许可按标准税率倍数计税 |
| 9 | fqslqjsx | 取水量区间（上限） | numeric | 23 | 10 | √ | 0 | 取水量区间（上限） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcwat_source_detail_tp |  | fsbbid |
| 2 | pk_tcwat_source_detail_tp |  | fid |
