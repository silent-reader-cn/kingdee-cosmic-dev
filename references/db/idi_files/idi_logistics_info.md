# 物流信息-idi_logistics_info

## 详细物流信息-子表 t_idi_logistics_data

- **表名称：** 详细物流信息-子表
- **表名：** t_idi_logistics_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstatus | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态 |
| 3 | fdataid | fdataid | int8 | 64 |  | √ | 0 | id |
| 4 | fcontext | 操作说明 | varchar | 255 |  | √ | ' ' | 操作说明 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fareacode | 行政区域编号 | varchar | 30 |  | √ | ' ' | 行政区域编号 |
| 7 | fftime | 操作时间 | varchar | 30 |  | √ | ' ' | 操作时间 |
| 8 | fareaname | 行政区域名称 | varchar | 30 |  | √ | ' ' | 行政区域名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_logistics_data_fid |  | fid |
| 2 | pk_t_idi_logistics_data |  | fdataid |

---

## 物流信息-主表 t_idi_logistics_info

- **表名称：** 物流信息-主表
- **表名：** t_idi_logistics_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstate | 物流状态 | varchar | 50 |  | √ | ' ' | 物流状态 |
| 3 | fcompanycode | 快递公司编号 | varchar | 30 |  | √ | ' ' | 快递公司编号 |
| 4 | fsendtime | 发件时间 | varchar | 50 |  | √ | ' ' | 发件时间 |
| 5 | fkuaidinum | 快递单号 | varchar | 30 |  | √ | ' ' | 快递单号 |
| 6 | fkuadicomname | 快递公司名称 | varchar | 30 |  | √ | ' ' | 快递公司名称 |
| 7 | fischeck | 是否签收 | bpchar | 1 |  | √ | ' ' | 是否签收,枚举: 0 :未签收 1 :已签收 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_idi_logistics_info_kdnum |  | fkuaidinum |
| 2 | pk_t_idi_logistics_info |  | fid |
