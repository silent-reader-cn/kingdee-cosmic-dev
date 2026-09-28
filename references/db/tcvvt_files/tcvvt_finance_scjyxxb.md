# 生产经营信息表-tcvvt_finance_scjyxxb

## 生产经营信息表-主表 t_tcvvt_finance_scjyxxb

- **表名称：** 生产经营信息表-主表
- **表名：** t_tcvvt_finance_scjyxxb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 |
| 3 | fyml | 用煤量(吨) | numeric | 23 | 10 | √ | 0 | 用煤量(吨) |
| 4 | fyjqnscjyzk | 预期全年生产经营状况 | varchar | 1000 |  | √ | ' ' | 预期全年生产经营状况 |
| 5 | fzjycp | 主经营产品 | varchar | 1000 |  | √ | ' ' | 主经营产品 |
| 6 | fzycpqmkcl | 主营产品期末库存量 | numeric | 23 | 10 | √ | 0 | 主营产品期末库存量 |
| 7 | fzycpljcl | 主营产品累计产量 | numeric | 23 | 10 | √ | 0 | 主营产品累计产量 |
| 8 | fydl | 用电量(万千瓦时) | numeric | 23 | 10 | √ | 0 | 用电量(万千瓦时) |
| 9 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 10 | fzycpljxl | 主营产品累计销量 | numeric | 23 | 10 | √ | 0 | 主营产品累计销量 |
| 11 | fyjxjscjyzk | 预期下季生产经营状况 | varchar | 1000 |  | √ | ' ' | 预期下季生产经营状况 |
| 12 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 13 | fysl | 用水量(吨) | numeric | 23 | 10 | √ | 0 | 用水量(吨) |
| 14 | fmqscjyzk | 目前生产经营状况 | varchar | 1000 |  | √ | ' ' | 目前生产经营状况 |
| 15 | fzycppjjg | 主营产品平均价格(元) | numeric | 23 | 10 | √ | 0 | 主营产品平均价格(元) |
| 16 | fzycpnckcl | 主营产品年初库存量 | numeric | 23 | 10 | √ | 0 | 主营产品年初库存量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tcvvt_scjyxxb |  | fsbbid,fewblxh |
| 2 | pk_tcvvt_finance_scjyxxb |  | fid |
