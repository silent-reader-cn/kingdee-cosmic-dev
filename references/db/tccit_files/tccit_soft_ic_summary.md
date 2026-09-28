# 软件、集成电路企业优惠底稿-tccit_soft_ic_summary

## 软件、集成电路企业优惠底稿-主表 t_tccit_soft_ic_sum

- **表名称：** 软件、集成电路企业优惠底稿-主表
- **表名：** t_tccit_soft_ic_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 4 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 5 | fsyyhzc | 适用优惠政策 | varchar | 50 |  | √ | ' ' | 适用优惠政策,枚举: 1 :延续适用原有优惠政策 2 :适用新出台优惠政策 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_soft_ic_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_soft_ic_sum |  | fid |
