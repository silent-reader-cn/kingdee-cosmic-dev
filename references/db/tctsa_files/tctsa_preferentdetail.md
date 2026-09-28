# 优惠明细-tctsa_preferentdetail

## 单据体-子表 t_tctsa_predetail_entry

- **表名称：** 单据体-子表
- **表名：** t_tctsa_predetail_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 3 | fstatisticprotid | 优惠项目 | int8 | 64 |  | √ | 0 | [统计项目 tctsa_statistic_project](../tctsa_files/tctsa_statistic_project.md) |
| 4 | famountincome | 税基优惠 | numeric | 23 | 10 | √ | 0 | 税基优惠 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpreferenttax | 税额优惠 | numeric | 23 | 10 | √ | 0 | 税额优惠 |
| 7 | fpreferenttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 5 :三免三减半 6 :超五百万部分减半 7 :两免三减半 8 :五免五减半 9 :其他 10 :500万以内免税，超500万减半 11 :加计100% 12 :2000万以内免税，超2000万减半 13 :十年内免税 14 :研发费用加计扣除 15 :按10%抵免税额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_predetail_entry |  | fentryid |
| 2 | idx_tctsa_predetail_entry_fk |  | fid |

---

## 优惠明细-主表 t_tctsa_preferentdetail

- **表名称：** 优惠明细-主表
- **表名：** t_tctsa_preferentdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbusinesssource | 业务来源 | varchar | 50 |  | √ | ' ' | 业务来源,枚举: 0 :纳税申报 1 :事项填报 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdiscountamount | 优惠金额合计 | numeric | 23 | 10 |  | null | 优惠金额合计 |
| 9 | ftaxitemname | 税目 | varchar | 50 |  | √ | ' ' | 税目 |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ftaxationsysid | 税收制度 | int8 | 64 |  | √ | 0 | [税收制度 bd_taxationsys](../basedata_files/bd_taxationsys.md) |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | ftype | 申报表类型 | varchar | 50 |  | √ | ' ' | 申报表类型,枚举: zzsybnsr :一般纳税人增值税 zzsxgmnsr :小规模增值税 qysdsjb :预缴申报 qysdsnb :汇算清缴 qysdsnb_fzjg :分支机构汇算清缴 qysds_hdzs_jb :核定预缴申报 qysds_hdzs_nb :核定汇算清缴 yhs :印花税 fcs :房产税 cztdsys :城镇土地使用税 fcscztdsys :房产和城镇土地使用税 fcsprice :从价计征房产税 fcshire :从租计征房产税 fjsf :附加税费 xfs :烟类消费税 xfsjypf :卷烟批发消费税 zzsybnsr_ybhz :一般企业汇总申报（一般纳税人总机构 ccxws :财产行为税 dkdj :代扣代缴 kjqysds :扣缴企业所得税 szys_a :水资源税A szys_b :水资源税B zzsybnsr_zjg :一般纳税人总机构汇总申报 zzsybnsr_hz_zjg :一般企业汇总申报仅汇总 zzsybnsr_yz_zjg :一般企业汇总申报预征方式总机构 zzsybnsr_fzjg :一般纳税人分支机构汇总申报 zzsybnsr_yz_fzjg :一般企业汇总申报预征方式分支机构 |
| 16 | factualdiscount | 实际优惠金额 | numeric | 23 | 10 |  | null | 实际优惠金额 |
| 17 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 18 | ftaxcategoryid | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 19 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 20 | fbillno | 申报表编号 | varchar | 30 |  | √ | ' ' | 申报表编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fdatatype | 数据来源 | varchar | 50 |  | √ | ' ' | 数据来源,枚举: 1 :系统生成 2 :数据引入 : |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctsa_preferentdetail |  | fid |
| 2 | idx_tctsa_prefdet_tax |  | forgid,ftaxationsysid,ftaxcategoryid |
