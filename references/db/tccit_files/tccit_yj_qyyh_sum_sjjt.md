# 预缴区域优惠底稿-tccit_yj_qyyh_sum_sjjt

## 预缴区域优惠底稿-主表 t_tccit_yj_qyyh_sum_sjjt

- **表名称：** 预缴区域优惠底稿-主表
- **表名：** t_tccit_yj_qyyh_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fftsde | 分摊所得额 | numeric | 23 | 10 | √ | 0 | 分摊所得额 |
| 4 | ftaxorg | 组织id | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fjmse | 减免税额 | numeric | 23 | 10 | √ | 0 | 减免税额 |
| 6 | fftrate | 分摊比例 | numeric | 23 | 10 | √ | 0 | 分摊比例 |
| 7 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | forgid | 申报组织 | int8 | 64 |  | √ | 0 | 申报组织 |
| 9 | ftaxorgname | 分支机构名 | varchar | 100 |  | √ | ' ' | 分支机构名 |
| 10 | fcompanytype | 企业类型 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 11 | fjmrate | 减免比例 | numeric | 23 | 10 | √ | 0 | 减免比例 |
| 12 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_qyyh_org_qq_qz |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_yj_qyyh_sum_sjjt |  | fid |
