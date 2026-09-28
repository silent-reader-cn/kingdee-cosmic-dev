# 税种信息变更记录表-tctb_tax_change_record

## 税种信息变更记录表-主表 t_tctb_tax_change_record

- **表名称：** 税种信息变更记录表-主表
- **表名：** t_tctb_tax_change_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flevytype | 征收方式 | varchar | 30 |  | √ | ' ' | 征收方式,枚举: czzs :查账征收 aqhz :按期汇总 hdzs :核定征收 |
| 3 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | ffarmdeducttype | 农产品核定扣除 | varchar | 50 |  | √ | ' ' | 农产品核定扣除,枚举: none :不适用 in-out :投入产出法 |
| 6 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftype | 申报表类型 | varchar | 36 |  | √ | ' ' | 模板类型 tctb_template_type |
| 9 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 11 | fmaintableid | 税务信息主表id | varchar | 50 |  | √ | ' ' | 税务信息主表id |
| 12 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fdeadline | 缴纳期限 | varchar | 30 |  | √ | ' ' | 缴纳期限,枚举: acsb :按次申报 aysb :按月申报 ajsb :按季申报 |
| 14 | ftaxpayertype | 纳税人类型 | varchar | 30 |  | √ | ' ' | 纳税人类型,枚举: ybnsr :一般纳税人 xgmnsr :小规模纳税人 |
| 15 | fenable | 启用 | varchar | 30 |  | √ | ' ' | 启用,枚举: 0 :禁用 1 :启用 |
| 16 | ftaxtype | 税种 | varchar | 30 |  | √ | ' ' | 税种,枚举: zzs :增值税 qysds :企业所得税 yhs :印花税 fjsf :附加税费 fcscztdsys :房产税和城镇土地使用税 xfs :消费税 szys :水资源税 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tctb_tax_change_record |  | fstartdate,fenddate,ftaxtype |
| 2 | t_tctb_tax_change_record_pkey |  | fid |
