# 土地增值税税源基础信息二维表-tcret_tdzzs_base_tax

## 土地增值税税源基础信息二维表-主表 t_tcret_tdzzs_base_tax

- **表名称：** 土地增值税税源基础信息二维表-主表
- **表名：** t_tcret_tdzzs_base_tax

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fqssysmj | 清算时已售面积 | numeric | 23 | 10 | √ | 0 | 清算时已售面积 |
| 3 | fphone | 电话 | varchar | 50 |  | √ | ' ' | 电话 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 5 | ffptzzysmj | 其中:非普通住宅已售面积 | numeric | 23 | 10 | √ | 0 | 其中:非普通住宅已售面积 |
| 6 | fqshsyksmj | 清算后剩余可售面积 | numeric | 23 | 10 | √ | 0 | 清算后剩余可售面积 |
| 7 | fewblname | 二维表名称 | varchar | 50 |  | √ | ' ' | 二维表名称 |
| 8 | fzksmj | 总可售面积 | numeric | 23 | 10 | √ | 0 | 总可售面积 |
| 9 | fpronumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 10 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 11 | fptzzysmj | 其中:普通住宅已售面积 | numeric | 23 | 10 | √ | 0 | 其中:普通住宅已售面积 |
| 12 | fpostcode | 邮政编码 | varchar | 50 |  | √ | ' ' | 邮政编码 |
| 13 | fproaddress | 项目地址 | varchar | 550 |  | √ | ' ' | 项目地址 |
| 14 | fproname | 项目名称 | varchar | 400 |  | √ | ' ' | 项目名称 |
| 15 | fzyczmj | 自用和出租面积 | numeric | 23 | 10 | √ | 0 | 自用和出租面积 |
| 16 | fqtlxfdcysmj | 其中:其他类型房地产已售面积 | numeric | 23 | 10 | √ | 0 | 其中:其他类型房地产已售面积 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tcret_tdzzs_base_tax1 |  | fewblxh,fsbbid |
| 2 | pk_tcret_tdzzs_base_tax |  | fid |
