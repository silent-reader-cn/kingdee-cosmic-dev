# 协同附件查询-tnd_biddoc_query

## 协同附件查询-主表 t_src_biddoc

- **表名称：** 协同附件查询-主表
- **表名：** t_src_biddoc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forigin | 发起方 | varchar | 30 |  | √ | ' ' | 发起方,枚举: 1 :采购方端 2 :供应商端 3 :两端公用 |
| 3 | fparentid | 父单据ID | varchar | 50 |  | √ | ' ' | 父单据ID |
| 4 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | ' ' |  |
| 5 | fbizstatus | fbizstatus | bpchar | 1 |  | √ | ' ' |  |
| 6 | fentitykey | 组件标识 | varchar | 50 |  | √ | ' ' | 组件标识 |
| 7 | fisquickpur | fisquickpur | bpchar | 1 |  | √ | '0' |  |
| 8 | fmanagetype | fmanagetype | bpchar | 1 |  | √ | ' ' |  |
| 9 | fbillno | fbillno | varchar | 30 |  | √ | ' ' |  |
| 10 | fpentitykey | 父单据标识 | varchar | 50 |  | √ | ' ' | 父单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_src_biddoc_fentitykey |  | fentitykey |
| 2 | idx_src_biddoc_fparentid |  | fparentid |
| 3 | pk_src_biddoc |  | fid |
| 4 | idx_src_biddoc_fbillno |  | fbillno |
