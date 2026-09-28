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
| 6 | fdimentionindex | fdimentionindex | varchar | 100 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fskssqz | fskssqz | timestamp | 0 |  |  | null |  |
| 10 | fsbqj | fsbqj | timestamp | 0 |  |  | null |  |
| 11 | ftaxtype | ftaxtype | int8 | 64 |  | √ | 0 |  |
| 12 | fbillno | fbillno | varchar | 100 |  | √ | ' ' |  |
| 13 | fchannel | fchannel | varchar | 50 |  | √ | ' ' |  |
| 14 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 15 | fdeclarechannel | fdeclarechannel | int8 | 64 |  | √ | 0 |  |
| 16 | fbillstatus | fbillstatus | varchar | 50 |  | √ | ' ' |  |
| 17 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 18 | fexecutestatus | fexecutestatus | varchar | 50 |  | √ | ' ' |  |
| 19 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 20 | ftaskcontext | ftaskcontext | varchar | 255 |  | √ | ' ' |  |
| 21 | fskssqq | fskssqq | timestamp | 0 |  |  | null |  |
| 22 | ftaskcontext_tag | ftaskcontext_tag | text | 0 |  |  | null |  |
| 23 | fpiclog | fpiclog | varchar | 255 |  | √ | ' ' |  |
| 24 | ftype | ftype | varchar | 50 |  | √ | ' ' |  |
| 25 | fdeallog | fdeallog | varchar | 255 |  | √ | ' ' |  |
| 26 | fsbbid | fsbbid | varchar | 50 |  | √ | ' ' |  |
| 27 | fexecutetype | fexecutetype | varchar | 50 |  | √ | ' ' |  |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 29 | flogdetail | flogdetail | varchar | 1000 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tsate_declare_record |  | fid |
| 2 | idx_t_taste_declare_record_3 |  | fdimentionindex |
| 3 | idx_t_tsate_declare_record_1 |  | fsbbid |
| 4 | idx_tsate_declare_record |  | forgid,ftype,fskssqq,fskssqz |
| 5 | idx_t_tsate_declare_record_2 |  | fcreatetime,fexecutetype |
