# 一键报税日志弹窗-tsate_msg_yjbs

## 一键报税日志弹窗-主表 t_tsate_declare_record

- **表名称：** 一键报税日志弹窗-主表
- **表名：** t_tsate_declare_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdetaillog_tag | fdetaillog_tag | text | 0 |  |  | null |  |
| 3 | fdetaillog | fdetaillog | varchar | 255 |  | √ | ' ' |  |
| 4 | ftasktype | ftasktype | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 9 | fsbqj | fsbqj | timestamp | 0 |  |  | null |  |
| 10 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 11 | fbillno | fbillno | varchar | 100 |  | √ | ' ' |  |
| 12 | fchannel | fchannel | varchar | 50 |  | √ | ' ' |  |
| 13 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 14 | fdeclarechannel | fdeclarechannel | int8 | 64 |  | √ | 0 |  |
| 15 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 16 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 17 | fexecutestatus | fexecutestatus | varchar | 50 |  | √ | ' ' |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 20 | fpiclog | fpiclog | varchar | 255 |  | √ | ' ' |  |
| 21 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 22 | fdeallog | fdeallog | varchar | 255 |  | √ | ' ' |  |
| 23 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 24 | fexecutetype | fexecutetype | varchar | 50 |  | √ | ' ' |  |
| 25 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 26 | flogdetail | flogdetail | varchar | 1000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_record |  | fid |
| 2 | idx_t_tsate_declare_record_1 |  | fsbbid |
| 3 | idx_tsate_declare_record |  | forgid,ftype,fskssqq,fskssqz |
