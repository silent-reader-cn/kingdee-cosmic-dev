# 广告宣传费底稿单据-tccit_advert_script

## 广告宣传费底稿单据-主表 t_tccit_advert_script

- **表名称：** 广告宣传费底稿单据-主表
- **表名：** t_tccit_advert_script

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fskssqz | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fmoney | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | foriginalmoney | 原获取金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原获取金额 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_advert_script |  | fid |
| 2 | idx_tccit_advert_script |  | forgid,fskssqq,fskssqz |
