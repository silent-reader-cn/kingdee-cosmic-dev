# 税费种核定信息-tsate_taxtype_verify

## 税费种核定信息-主表 t_tctb_taxtype_verify

- **表名称：** 税费种核定信息-主表
- **表名：** t_tctb_taxtype_verify

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fzsxm | 征收项目 | int8 | 64 |  | √ | 0 | 税种 bd_taxcategory |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | 税务组织信息 bastax_taxorg |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 5 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | flevytype | 征收方式 | varchar | 50 |  | √ | ' ' | 征收方式,枚举: zxsb :自行申报 dkdj :代扣代缴 wtdz :委托代征 |
| 7 | fzspm | 征收品目 | int8 | 64 |  | √ | 0 | 征收品目 tpo_zspm |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | feffectivedate | 认定有效期起 | timestamp | 0 |  |  | null | 认定有效期起 |
| 11 | fcomparestatus | 差异比对结果 | varchar | 50 |  | √ | ' ' | 差异比对结果,枚举: comparing :比对中 diff :有差异 same :无差异 nodata :无比对数据 fail :比对失败 |
| 12 | fupdatestatus | 更新状态 | varchar | 50 |  | √ | ' ' | 更新状态,枚举: undo :未更新 updating :更新中 updated :更新成功 fail :更新失败 without :无需更新 |
| 13 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 14 | fkjzd | 会计制度 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |
| 15 | finfotype | 信息类型 | varchar | 50 |  | √ | ' ' | 信息类型,枚举: 0 :税务信息 1 :财报信息 |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | ftaxlimit | 纳税期限 | varchar | 50 |  | √ | ' ' | 纳税期限,枚举: year :年 season :季 month :月 single :次 halfyear :半年 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | ftkjzd | 会计制度 | varchar | 50 |  | √ | ' ' | 会计制度 |
| 22 | fbbmc | 报表名称 | int8 | 64 |  | √ | 0 | 报表类型 tpo_reporttype |
| 23 | fexpirydate | 认定有效期止 | timestamp | 0 |  |  | null | 认定有效期止 |
| 24 | ftbbmc | 报表名称 | varchar | 100 |  | √ | ' ' | 报表名称 |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_taxtype_verify |  | fid |
| 2 | idx_tctb_verify_org |  | forgid |
