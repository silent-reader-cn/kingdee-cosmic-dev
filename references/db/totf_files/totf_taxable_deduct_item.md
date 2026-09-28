# 应税服务减除项目清单台账-totf_taxable_deduct_item

## 应税服务减除项目清单台账-主表 t_totf_taxable_deductitem

- **表名称：** 应税服务减除项目清单台账-主表
- **表名：** t_totf_taxable_deductitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccountorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fvouchertype | 凭证种类 | varchar | 50 |  | √ | ' ' | 凭证种类 |
| 4 | ffilldate | 填表日期 | timestamp | 0 |  |  | null | 填表日期 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fenddate | 税（费）款所属期止 | timestamp | 0 |  |  | null | 税（费）款所属期止 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fkpfnsrsbh | 开票方纳税人识别号 | varchar | 50 |  | √ | ' ' | 开票方纳税人识别号 |
| 11 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fbusdimensionmap | 业务维度映射（计税方案） | int8 | 64 |  | √ | 0 | [计税方案 itp_proviston_plan](../tctb_files/itp_proviston_plan.md) |
| 16 | fvouchernumber | 凭证号码 | varchar | 50 |  | √ | ' ' | 凭证号码 |
| 17 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 18 | fstartdate | 税（费）款所属期起 | timestamp | 0 |  |  | null | 税（费）款所属期起 |
| 19 | fsbbid | 申报表 | int8 | 64 |  | √ | 0 | [纳税申报表基础资料 bdtaxr_nsrxx](../bdtaxr_files/bdtaxr_nsrxx.md) |
| 20 | fbusdimension | 业务维度 | int8 | 64 |  | √ | 0 | null 001 |
| 21 | fdatasource | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: dataimport :数据引入 handadd :手工新增 |
| 22 | fkpfdwmc | 开票方单位名称 | varchar | 50 |  | √ | ' ' | 开票方单位名称 |
| 23 | fitemname | 服务项目名称 | varchar | 50 |  | √ | ' ' | 服务项目名称 |
| 24 | ftaxoffice | 税务机关 | int8 | 64 |  | √ | 0 | [税务机关 bastax_taxorgan](../bastax_files/bastax_taxorgan.md) |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_taxc_taxdeduct_org_date |  | forgid,fstartdate,fenddate |
| 2 | pk_totf_taxable_deductitem |  | fid |
