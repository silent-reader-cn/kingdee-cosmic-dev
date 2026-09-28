# 应税服务减除项目清单-totf_whsyjsf_ysfwjcxmqd

## 应税服务减除项目清单-主表 t_totf_whsyjsf_ysfwjcxmqd

- **表名称：** 应税服务减除项目清单-主表
- **表名：** t_totf_whsyjsf_ysfwjcxmqd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouchertype | 凭证种类 | varchar | 50 |  | √ | ' ' | 凭证种类 |
| 3 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :合计 2 :2 |
| 4 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 5 | fvouchernumber | 凭证号码 | varchar | 50 |  | √ | ' ' | 凭证号码 |
| 6 | fkpfdwmc | 开票方单位名称 | varchar | 50 |  | √ | ' ' | 开票方单位名称 |
| 7 | fitemname | 服务项目名称 | varchar | 50 |  | √ | ' ' | 服务项目名称 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fkpfnsrsbh | 开票方纳税人识别号 | varchar | 50 |  | √ | ' ' | 开票方纳税人识别号 |
| 10 | fewblname | 二维表行名称 | varchar | 50 |  | √ | ' ' | 二维表行名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_ysfwjcxm_sbbid_ewbxh |  | fsbbid,fewblxh |
| 2 | pk_totf_whsyjsf_ysfwjcxmqd |  | fid |
