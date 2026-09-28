# 应税服务减除项目清单台账-totf_taxable_deduct_item

## 应税服务减除项目清单台账-主表 t_totf_taxable_deductitem

- **表名称：** 应税服务减除项目清单台账-主表
- **表名：** t_totf_taxable_deductitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fvouchertype | 凭证种类 | varchar | 50 |  | √ | ' ' | 凭证种类 |
| 4 | ffilldate | 填表日期 | timestamp | 0 |  |  | null | 填表日期 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fvouchernumber | 凭证号码 | varchar | 50 |  | √ | ' ' | 凭证号码 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fenddate | 费款所属期止 | timestamp | 0 |  |  | null | 费款所属期止 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fstartdate | 费款所属期起 | timestamp | 0 |  |  | null | 费款所属期起 |
| 15 | fsbbid | 申报表ID | int8 | 64 |  | √ | 0 | 纳税申报表基础资料 bdtaxr_nsrxx |
| 16 | fkpfdwmc | 开票方单位名称 | varchar | 50 |  | √ | ' ' | 开票方单位名称 |
| 17 | fitemname | 服务项目名称 | varchar | 50 |  | √ | ' ' | 服务项目名称 |
| 18 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | 税务机关 bastax_taxorgan |
| 19 | fkpfnsrsbh | 开票方纳税人识别号 | varchar | 50 |  | √ | ' ' | 开票方纳税人识别号 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_taxdeduct_org_date |  | forgid,fstartdate,fenddate |
| 2 | pk_totf_taxable_deductitem |  | fid |
