# 应税服务扣除项目清单-tcvat_ybnsr_ysfwkcxmqd

## 应税服务扣除项目清单-主表 t_tcvat_ybnsr_ysfwkcxmqd

- **表名称：** 应税服务扣除项目清单-主表
- **表名：** t_tcvat_ybnsr_ysfwkcxmqd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 |
| 3 | ftype | 凭证种类 | varchar | 50 |  | √ | ' ' | 凭证种类 |
| 4 | finvoicenumber | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 5 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 6 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 7 | fkpfdwmc | 开票方单位名称 | varchar | 50 |  | √ | ' ' | 开票方单位名称 |
| 8 | fkjrq | 开具日期 | timestamp | 0 |  |  | null | 开具日期 |
| 9 | fkpfnsrsbh | 开票方纳税人识别号 | varchar | 50 |  | √ | ' ' | 开票方纳税人识别号 |
| 10 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |
| 11 | ffwxmmc | 服务项目名称 | varchar | 100 |  | √ | ' ' | 服务项目名称 |
| 12 | fyxkcxmje | 允许扣除项目金额 | numeric | 23 | 10 | √ | 0 | 允许扣除项目金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcvat_ybnsr_ysfwkcxmqd |  | fid |
| 2 | idx_taxc_ysfwkcxmqd_ewbxh_sbid |  | fsbbid,fewblxh |
